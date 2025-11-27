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
        self.sidebar = None


        self.create_start_ui()



        

    def create_start_ui (self):
        self.sidebar = ctk.CTkFrame(
            self.app,
            width=200,
            corner_radius=10,
            bg_color='#343B54',
            fg_color='#343B54'
        )
        self.sidebar.pack(side="left", fill="y")

        self.sidebar_top_text = ctk.CTkLabel(
            self.sidebar,
            bg_color=self.bg_color,
            text='Mods',
            fg_color='#343B54',
            text_color='#ffffff',
            font=("ansi", 25),
            width=200
        )

        self.facebook_button = CTkButton(
            self.sidebar,
            bg_color=self.bg_color,
            text="Facebook",
            fg_color="#7D66F3",
            text_color="#ffffff",
            hover_color="#5C4BB3",
            background_corner_colors=("#343B54", "#343B54", "#343B54", "#343B54"),
            font=("ansi", 25),
            width=200
        )

        self.sidebar_top_text.pack(pady=10, padx=10)
        self.facebook_button.pack(pady=10, padx=10)


