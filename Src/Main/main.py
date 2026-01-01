import sys
import os
sys.dont_write_bytecode = True
# needed for the gui , daemon
import customtkinter as ctk
import threading
import webbrowser

SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH) # set current path to src

#all the local imports
from UI.Ui import UI
from Modules.facebook import scrape_facebook_marketplace
from Modules.amazon import amazonScrape

class Main:
    def __init__(self, app):
        app.title("Facebook Scraper")
        app.after(0, lambda: app.state('zoomed')) # Set app to fullscreen (zoomed) , might change it to user prefrence in the future
        self.scrape_thread = None
        self.stop_flag = False
        self.items_scraped = 0


        icon_path = os.path.join(SRC_PATH, "Images", "appicon.ico") # src path + \Images\appicon
        if os.path.exists(icon_path):
            app.wm_iconbitmap(icon_path) # set app icon to the app

        # init the gui
        self.bg_color = "#272C3F"
        app.configure(fg_color=self.bg_color)

        self.window = UI(app, self)

    def threaded_scraper(self):
        try:
            debug = self.is_debug_on() if True else False # (headless)
            if self.window.get_mode() == 'fb':

                category = self.search_callback()
                if category == "":
                    self.stop_flag = True
                    self.window.change_start_stop_button("Start")
                    self.window.no_category_error()

                else:
                    scrape_facebook_marketplace(self.stop_flag_callback, self.add_listing_to_ui, category , debug)
            else:
                print("amazon")
                category = self.search_callback()
                if category == "":
                    self.stop_flag = True
                    self.window.change_start_stop_button("Start")
                    self.window.no_category_error()
                    
                else:
                    amazonScrape(self.stop_flag_callback, self.add_listing_to_ui_amazon ,category, debug)
                    
                self.window.change_start_stop_button("Start")
        except Exception as e:
            print("Scraper stopped:", e)

    def stop_flag_callback(self):
        return self.stop_flag

    def search_callback(self):
        return self.window.search.get()

    def start_scraper(self):
        if self.scrape_thread is None or not self.scrape_thread.is_alive(): # check if the thread exists
            
            print("Starting scraper...")
            self.stop_flag = False
            self.window.change_start_stop_button("Stop")

            self.scrape_thread = threading.Thread(
                target=self.threaded_scraper,
                daemon=True
            )
            self.scrape_thread.start()

        else:
            print("Stopping scraper...")
            self.stop_flag = True
            self.window.start_stop_button.configure(text="Start")

    def add_listing_to_ui(self, title, price, link, city):
        self.window.app.after(0, lambda: self.safe_add_listing(title, price, link, city))

    def safe_add_listing(self, title, price, link, city):
        if city:
            self.label = ctk.CTkLabel(
                self.window.my_frame,
                text=f"Title: {title} | Price: {price} | City: {city}",
                text_color="white",
                font=("ansi", 20)
            )
            self.label.bind("<Button-1>", lambda e: self.window.callback(link)) # basically just opening the link with webrowser
            self.label.pack(anchor="w", pady=5)

        self.window.items_scraped += 1
        self.window.items_scraped_ui.configure(text=f"Items scraped: {self.window.items_scraped}")

    def add_listing_to_ui_amazon(self, title, price, link):
        self.window.app.after(0, lambda: self.safe_add_listing_amazon(title, price, link))

    def safe_add_listing_amazon(self, title, price, link):
        self.label = ctk.CTkLabel(
            self.window.my_frame,
            text=f"Title: {title} | Price: {price}",
            text_color="white",
            font=("ansi", 20)
        )
        self.label.bind("<Button-1>", lambda e: self.window.callback(link))
        self.label.pack(anchor="w", pady=5)

        self.window.items_scraped += 1
        self.window.items_scraped_ui.configure(text=f"Items scraped: {self.window.items_scraped}")


    def is_debug_on(self):
        return self.window.return_debug_state()


# main loop
if __name__ == "__main__":
    app = ctk.CTk()
    root = Main(app)
    app.mainloop()
