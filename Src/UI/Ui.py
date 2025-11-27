import sys
sys.dont_write_bytecode = True

import customtkinter as ctk
from customtkinter import CTkLabel, CTkFrame, CTkEntry, CTkButton, CTkTextbox




class UI:
    def __init__(self, app):
        self.app = app
        self.bg_color = "#262C3C"
        self.sidebar_top_text = None
        self.active_frame = None
        self.facebook_button = None
        self.amazon_button = None
        self.sidebar = None
        self.start_stop_button =None

        app.grid_columnconfigure(1, weight=1)
        app.grid_rowconfigure(0, weight=1)

        self.gpus_array =  [
    "GeForce GTX 1050",
    "GeForce GTX 1050 Ti",
    "GeForce GTX 1060",
    "GeForce GTX 1070",
    "GeForce GTX 1070 Ti",
    "GeForce GTX 1080",
    "GeForce GTX 1080 Ti",

    "GeForce GTX 1650",
    "GeForce GTX 1650 Super",
    "GeForce GTX 1660",
    "GeForce GTX 1660 Super",
    "GeForce GTX 1660 Ti",

    "GeForce RTX 2060",
    "GeForce RTX 2060 Super",
    "GeForce RTX 2070",
    "GeForce RTX 2070 Super",
    "GeForce RTX 2080",
    "GeForce RTX 2080 Super",
    "GeForce RTX 2080 Ti",

    "GeForce RTX 3050",
    "GeForce RTX 3060",
    "GeForce RTX 3060 Ti",
    "GeForce RTX 3070",
    "GeForce RTX 3070 Ti",
    "GeForce RTX 3080",
    "GeForce RTX 3080 Ti",
    "GeForce RTX 3090",
    "GeForce RTX 3090 Ti",

    "GeForce RTX 4050",
    "GeForce RTX 4060",
    "GeForce RTX 4060 Ti",
    "GeForce RTX 4070",
    "GeForce RTX 4070 Ti",
    "GeForce RTX 4080",
    "GeForce RTX 4090",

    "Radeon RX 5500 XT",
    "Radeon RX 5600 XT",
    "Radeon RX 5700",
    "Radeon RX 5700 XT",

    "Radeon RX 6600",
    "Radeon RX 6600 XT",
    "Radeon RX 6700 XT",
    "Radeon RX 6800",
    "Radeon RX 6800 XT",
    "Radeon RX 6900 XT",

    "Radeon RX 7600",
    "Radeon RX 7600 XT",
    "Radeon RX 7700",
    "Radeon RX 7700 XT",
    "Radeon RX 7800",
    "Radeon RX 7800 XT",
    "Radeon RX 7900 XT",
    "Radeon RX 7900 XTX"
  ]


        self.create_start_ui()


    #def start_scraper (self):



        

    def create_start_ui (self):
        self.sidebar = ctk.CTkFrame(
            self.app,
            width=200,
            corner_radius=10,
            bg_color='#343B54',
            fg_color='#343B54'
        )
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.sidebar_top_text = ctk.CTkLabel(
            self.sidebar,
            bg_color=self.bg_color,
            text='Mods',
            fg_color='#343B54',
            text_color='#ffffff',
            font=("ansi", 25),
            width=250
        )

        self.facebook_button = CTkButton(
            self.sidebar,
            bg_color=self.bg_color,
            text="Facebook scraper",
            fg_color="#7D66F3",
            text_color="#ffffff",
            hover_color="#5C4BB3",
            background_corner_colors=("#343B54",) * 4,
            font=("ansi", 25),
            width=230
        )

        self.amazon_button = CTkButton(
            self.sidebar,
            bg_color=self.bg_color,
            text="Amazon scraper",
            fg_color="#7D66F3",
            text_color="#ffffff",
            hover_color="#5C4BB3",
            background_corner_colors=("#343B54",) * 4,
            font=("ansi", 25),
            width=230
        )


        self.sidebar_top_text.pack(pady=10, padx=10)
        self.facebook_button.pack(pady=10, padx=10)
        self.amazon_button.pack(pady=10, padx=10)

        self.active_frame = CTkFrame(
            self.app,
            fg_color=self.bg_color
        )
        self.active_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.start_stop_button = CTkButton(
            self.active_frame,
            text="Start",
            fg_color="#8968FD",
            hover_color="#5C4BB3",
            height=40,
            width=80,
            font=("Arial", 20)
        )
        self.start_stop_button.pack(side="top", anchor="nw", padx=10, pady=10)



