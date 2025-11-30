import sys
sys.dont_write_bytecode = True

import sys, os, threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Modules.facebook import scrape_facebook_marketplace
import customtkinter as ctk
from customtkinter import CTkLabel, CTkButton, CTkFrame
import webbrowser

class UI:

    def __init__(self, app):
        self.app = app
        self.bg_color = "#262C3C"

        self.scrape_thread = None
        self.stop_flag = False
        self.search = None
        self.label = None
        self.items_scraped = 0
        self.mode = 'fb'
        self.hold_esc = None

        app.grid_columnconfigure(1, weight=1)
        app.grid_rowconfigure(0, weight=1)

        self.create_start_ui()

    def set_fb(self):
        self.mode = 'fb'
        print("facebook mode")

    def set_az(self):
        self.mode = 'az'
        print("amazon mode")

    def clear_listing(self):
        for lay in self.my_frame.winfo_children():
            lay.destroy()

        self.items_scraped = 0
        self.items_scraped_ui.configure(text=f"Items scraped: {self.items_scraped}")

    def threaded_scraper(self):
        try:
            if self.mode == 'fb':
                category = self.search_callback()
                scrape_facebook_marketplace(self.stop_flag_callback, self.add_listing_to_ui, category)
            else:
                print("amazon")
        except Exception as e:
            print("Scraper stopped:", e)

    def stop_flag_callback(self):
        return self.stop_flag

    def search_callback(self):
        return self.search.get()

    def callback(self,url):
        webbrowser.open_new_tab(url)

    def start_scraper(self):
        if self.scrape_thread is None or not self.scrape_thread.is_alive():
            print("Starting scraper...")
            self.stop_flag = False
            self.start_stop_button.configure(text="Stop")

            self.scrape_thread = threading.Thread(
                target=self.threaded_scraper,
                daemon=True
            )
            self.scrape_thread.start()

        else:
            print("Stopping scraper...")
            self.stop_flag = True
            self.start_stop_button.configure(text="Start")

    def enter_key(self, event=None):
        self.start_scraper()
        
    def esc_press(self, event=None):
        self.hold_esc = self.app.after(1000, self.exit_key)
        
    def esc_release(self, event=None):
        if self.hold_esc is not None:
            self.app.after_cancel(self.hold_esc)
            self.hold_esc = None
        
    def exit_key(self):
        sys.exit()
        

    def add_listing_to_ui(self, title, price, link, city):
        self.label = ctk.CTkLabel(
            self.my_frame,
            text=f"Title: {title} | Price: {price} | City: {city}",
            text_color="white",
            font=("ansi", 20)
        )
        self.label.bind("<Button-1>", lambda e:self.callback(link))
        self.label.pack(anchor="w", pady=5)
        self.items_scraped += 1

        self.items_scraped_ui.configure(text=f"Items scraped: {self.items_scraped}")

    def make_Button(self, parent, text, height, width, command, bg_corner_color = "#262C3C"):
        return CTkButton(
            parent,
            text=text,
            fg_color="#6561EA",
            hover_color="#5C4BB3",
            background_corner_colors=(bg_corner_color,) * 4,
            corner_radius=100,
            font=('ansi', 25),
            width=width,
            height=height,
            command=command
        )

    def make_pack(self, ver, pady=None, padx=None, side=None):
        ver.pack(pady=pady, padx=padx, side=side)

    def create_start_ui(self):
        self.sidebar = ctk.CTkFrame(
            self.app,
            width=300,
            corner_radius=100,
            bg_color="#343B54",
            fg_color="#343B54"
        )
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.active_frame = CTkFrame(
            self.app,
            fg_color=self.bg_color
        )
        self.active_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.top_bar = ctk.CTkFrame(self.active_frame, fg_color=self.bg_color)
        self.top_bar.pack(fill="x", pady=10, padx=10)

        self.my_frame = ctk.CTkScrollableFrame(
            self.active_frame,
            width=300,
            height=200,
            fg_color="#0C1826",
            corner_radius=20
        )
        self.my_frame.pack(fill='both', expand=True, padx=20, pady=(20,0))


        #Label
        self.sidebar_top_text = CTkLabel(
            self.sidebar,
            text="Mods:",
            text_color="#ffffff",
            font=("ansi", 25),
        )

        self.items_scraped_ui = ctk.CTkLabel(
            self.top_bar,
            text=f"Items scraped: {self.items_scraped}",
            text_color='#71869C',
            font=('ansi', 18)
        )

        #Button
        self.button_ary = {
            "facebook_button":[
                self.sidebar,
                "Facebook scraper",
                40,
                250,
                self.set_fb,
                "#343B54"
            ],
            "amazon_button":[
                self.sidebar,
                "Amazon scraper",
                40,
                250,
                self.set_az,
                "#343B54"
            ],
            "exit_button":[
                self.sidebar,
                "Exit",
                40,
                100,
                exit,
                "#343B54"
            ],
            "start_stop_button":[
                self.top_bar,
                "Start",
                40,
                120,
                self.start_scraper,
                None
            ],
            "clear":[
                self.top_bar,
                "Clear",
                40,
                120,
                self.clear_listing,
                None
            ]
        }

        for ver, values in self.button_ary.items():
            parent, text, height, width, command, bg_corner_color = values
            button = self.make_Button(parent, text, height, width, command, bg_corner_color)
            setattr(self, ver, button)

        #Entry
        self.search = ctk.CTkEntry(
            self.top_bar,
            fg_color="#0C1826",
            border_color="#0C1826",
            corner_radius=100,
            height=45,
            width=300,
            placeholder_text="Category",
            text_color='white',
            font=("Arial", 25)
        )

        #pack
        self.pack_ary = {
            self.sidebar_top_text:[(10,60), 10, None],
            self.facebook_button:[10, 10, None],
            self.amazon_button:[10, 10, None],
            self.exit_button:[25, 100, "bottom"],
            self.search:[None, 10, "left"],
            self.start_stop_button:[None, 10, "left"],
            self.items_scraped_ui:[None, 10, "left"],
            self.clear:[None, 10, "right"],
        }

        for ver, values in self.pack_ary.items():
            pady, padx, side = values
            self.make_pack(ver, pady, padx, side)

        self.app.bind('<Return>', self.enter_key)
        self.app.bind("<KeyPress-Escape>", self.esc_press)
        self.app.bind("<KeyRelease-Escape>", self.esc_release)