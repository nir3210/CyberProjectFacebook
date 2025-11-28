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

        app.grid_columnconfigure(1, weight=1)
        app.grid_rowconfigure(0, weight=1)

        self.create_start_ui()

    def threaded_scraper(self):
        try:
            category = self.search_callback()
            scrape_facebook_marketplace(self.stop_flag_callback, self.add_listing_to_ui, category)
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

    def add_listing_to_ui(self, title, price, link, city):
        label = ctk.CTkLabel(
            self.my_frame,
            text=f"title: {title} | price: {price} | city: {city}",
            text_color="white",
            font=("Arial", 20)
        )
        label.bind("<Button-1>", lambda e:self.callback(link))
        label.pack(anchor="w", pady=5)

    def create_start_ui(self):
        self.sidebar = ctk.CTkFrame(
            self.app,
            width=200,
            corner_radius=100,
            bg_color="#343B54",
            fg_color="#343B54"
        )
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.sidebar_top_text = CTkLabel(
            self.sidebar,
            bg_color="#343B54",
            text="Mods",
            fg_color="#343B54",
            text_color="#ffffff",
            font=("ansi", 25),
            width=250
        )
        self.sidebar_top_text.pack(pady=(20,60), padx=10)

        self.facebook_button = CTkButton(
            self.sidebar,
            bg_color="#343B54",
            text="Facebook scraper",
            fg_color="#7D66F3",
            text_color="#ffffff",
            hover_color="#5C4BB3",
            background_corner_colors=("#343B54",) * 4,
            corner_radius=100,
            font=("ansi", 25),
            width=250,
            height=40
        )
        self.facebook_button.pack(pady=10, padx=10)

        self.amazon_button = CTkButton(
            self.sidebar,
            bg_color="#343B54",
            text="Amazon scraper",
            fg_color="#7D66F3",
            text_color="#ffffff",
            hover_color="#5C4BB3",
            background_corner_colors=("#343B54",) * 4,
            corner_radius=100,
            font=("ansi", 25),
            width=250,
            height=40
        )
        self.amazon_button.pack(pady=10, padx=10)

        self.exit_button = CTkButton(
            self.sidebar,
            text="Exit",
            fg_color="#8968FD",
            hover_color="#5C4BB3",
            height=40,
            width=100,
            font=("Arial", 25),
            corner_radius=100,
            command=exit
        )
        self.exit_button.pack(side="bottom", pady=25, padx=100)

        self.active_frame = CTkFrame(
            self.app,
            fg_color=self.bg_color
        )
        self.active_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.top_bar = ctk.CTkFrame(self.active_frame, fg_color=self.bg_color)
        self.top_bar.pack(fill="x", pady=10, padx=10)

        self.search = ctk.CTkEntry(
            self.top_bar,
            fg_color="#0C1826",
            border_color='#0C1826',
            corner_radius=100,
            height=45,
            width=300,
            placeholder_text="Category",
            font=("Arial", 25)
        )
        self.search.pack(side="left", padx=10)

        self.start_stop_button = CTkButton(
            self.top_bar,
            text="Start",
            fg_color="#8968FD",
            hover_color="#5C4BB3",
            height=40,
            width=120,
            font=("Arial", 25),
            corner_radius=100,
            command=self.start_scraper
        )
        self.start_stop_button.pack(side="left", padx=10)



        self.my_frame = ctk.CTkScrollableFrame(
            self.active_frame,
            width=300,
            height=200,
            fg_color='#0C1826',
            corner_radius=10
        )
        self.my_frame.pack(fill='both', expand=True, padx=20, pady=20)
