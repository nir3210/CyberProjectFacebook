import sys
import os
sys.dont_write_bytecode = True

import customtkinter as ctk
import threading
import webbrowser

SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from UI.Ui import UI
from Modules.facebook import scrape_facebook_marketplace


class Main:
    def __init__(self, app):
        app.title("Facebook Scraper")
        app.after(0, lambda: app.state('zoomed'))
        self.scrape_thread = None
        self.stop_flag = False
        self.items_scraped = 0


        icon_path = os.path.join(SRC_PATH, "Images", "appicon.ico")
        if os.path.exists(icon_path):
            app.wm_iconbitmap(icon_path)

        self.bg_color = "#272C3F"
        app.configure(fg_color=self.bg_color)

        self.window = UI(app, self)

    def threaded_scraper(self):
        try:
            if self.window.get_mode() == 'fb':
                category = self.search_callback()
                if category == "":
                    self.stop_flag = True
                    self.window.change_start_stop_button("Start")
                    self.window.no_category_error()

                else:
                    scrape_facebook_marketplace(self.stop_flag_callback, self.add_listing_to_ui, category)
            else:
                print("amazon")
                self.window.change_start_stop_button("Start")
        except Exception as e:
            print("Scraper stopped:", e)

    def stop_flag_callback(self):
        return self.stop_flag

    def search_callback(self):
        return self.window.search.get()

    def start_scraper(self):
        if self.scrape_thread is None or not self.scrape_thread.is_alive():
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

    def add_listing_to_ui(self, title, price, link, city=None):
        self.window.app.after(0, lambda: self.safe_add_listing(title, price, link, city))

    def safe_add_listing(self, title, price, link, city):
        if city:
            self.label = ctk.CTkLabel(
                self.window.my_frame,
                text=f"Title: {title} | Price: {price} | City: {city}",
                text_color="white",
                font=("ansi", 20)
            )
            self.label.bind("<Button-1>", lambda e: self.window.callback(link))
            self.label.pack(anchor="w", pady=5)

        else:
            self.label = ctk.CTkLabel(
                self.window.my_frame,
                text=f"Title: {title} | Price: {price}",
                text_color="white",
                font=("ansi", 20)
            )
            self.label.bind("<Button-1>", lambda e: self.window.callback(link))
            self.label.pack(anchor="w", pady=5)

        self.items_scraped += 1
        self.window.items_scraped_ui.configure(text=f"Items scraped: {self.window.items_scraped}")


if __name__ == "__main__":
    app = ctk.CTk()
    root = Main(app)
    app.mainloop()
