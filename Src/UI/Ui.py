import sys
sys.dont_write_bytecode = True

import os
import customtkinter as ctk
from customtkinter import CTkLabel, CTkButton, CTkFrame, CTkSwitch, StringVar
import tkinter as tk
import webbrowser

class UI:

    def __init__(self, app, main_instance):
        self.app = app
        self.bg_color = "#262C3C"
        self.main = main_instance

        self.search = None
        self.label = None
        self.items_scraped = 0
        self.mode = 'fb'
        self.hold_esc = None
        self.is_dark_ui_on = False
        self.debug = False
        self.debug_var = ctk.StringVar(value="off")

        app.grid_columnconfigure(1, weight=1)
        app.grid_rowconfigure(0, weight=1)

        self.create_start_ui()

    def set_fb(self):
        self.mode = 'fb'
        print("facebook mode")

    def set_az(self):
        self.mode = 'az'
        print("amazon mode")

    def change_start_stop_button(self, text):
        self.start_stop_button.configure(text=text)

    def no_category_error(self):
        self.label = ctk.CTkLabel(
            self.my_frame,
            text="Please Enter A Category Name! Please Try again.",
            font=("ansi", 20),
            text_color="white"
        )
        self.label.pack(anchor='w', pady=3)

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode

    def clear_listing(self):
        for lay in self.my_frame.winfo_children():
            lay.destroy()

        self.items_scraped = 0
        self.items_scraped_ui.configure(text=f"Items scraped: {self.items_scraped}")

    def callback(self,url):
        webbrowser.open_new_tab(url)

    def enter_key(self, event=None):
        self.main.start_scraper()

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

    def degug_on_off(self):
        if self.debug:
            self.debug = False
        else:
            self.debug = True

    def return_debug_state(self):
        return self.debug

    def dark_overlay(self):
        self.is_dark_ui_on = True
        self.exit_overlay = ctk.CTkToplevel(self.app, fg_color="#000000")
        self.exit_overlay.attributes("-alpha", 0.3)
        self.exit_overlay.overrideredirect(True)
        self.exit_overlay.geometry(f"{self.app.winfo_width()}x{self.app.winfo_height()}+{self.app.winfo_rootx()}+{self.app.winfo_rooty()}")
        self.exit_overlay.lift()
        self.exit_overlay.grab_set()

    def close_exit_overlay(self):
        if self.exit_overlay:
            self.exit_overlay.destroy()
            self.is_dark_ui_on = False

    def exit_ui(self, event=None):
        if not self.is_dark_ui_on:
            self.dark_overlay()
            self.exit_frame = ctk.CTkFrame(self.exit_overlay, height=150, width=350, fg_color="#000", corner_radius=15)
            self.exit_frame.place(relx=0.5, rely=0.5, anchor="center")

            self.exit_frame.grid_rowconfigure(0, weight=1)
            self.exit_frame.grid_rowconfigure(1, weight=1)
            self.exit_frame.grid_columnconfigure(0, weight=1)
            self.exit_frame.grid_columnconfigure(1, weight=1)

            lay = ctk.CTkLabel(self.exit_frame, text="Do you want to quit the app", fg_color="#000", text_color="white", font=("ansi", 25))
            lay.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

            exit_dir = {
                "yesbtn":[
                    self.exit_frame,
                    "Yes",
                    40, 100,
                    exit,
                    "#000"
                ],
                "nobtn":[
                    self.exit_frame,
                    "No",
                    40, 100,
                    self.close_exit_overlay,
                    "#000"
                ]
            }
            for ver, values in exit_dir.items():
                parent, text, height, width, command, bg_corner_color = values
                button = self.make_Button(parent, text, height, width, command, bg_corner_color)
                setattr(self, ver, button)


            self.yesbtn.grid(row=1, column=0, pady=5, padx=5)
            self.nobtn.grid(row=1, column=1, pady=5, padx=5)
        else:
            self.close_exit_overlay()

    def create_start_ui(self):
        self.sidebar = ctk.CTkFrame(
            self.app,
            width=300,
            corner_radius=100,
            bg_color="#343B54",
            fg_color="#343B54"
        )
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.active_frame = CTkFrame(self.app, fg_color=self.bg_color)
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
                self.exit_ui,
                "#343B54"
            ],
            "start_stop_button":[
                self.top_bar,
                "Start",
                40,
                120,
                lambda: self.main.start_scraper(),
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


        self.debug_button = ctk.CTkSwitch(
            self.sidebar,
            text="Debugging",
            command=self.degug_on_off,
            font=("ansi",25),
            switch_height=25,
            switch_width=50,
            text_color="white",
            button_hover_color="#5C4BB3",
            button_color="#6561EA",
            progress_color="#343278",
            fg_color="#0C1826",
            variable=self.debug_var,
            onvalue="on",
            offvalue="off"
        )

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
            self.debug_button:[10, 10, None],
            self.exit_button:[25, 100, "bottom"],
            self.search:[None, 10, "left"],
            self.start_stop_button:[None, 10, "left"],
            self.items_scraped_ui:[None, 10, "left"],
            self.clear:[None, 10, "right"],
        }

        for ver, values in self.pack_ary.items():
            pady, padx, side = values
            self.make_pack(ver, pady, padx, side)

        #bind
        self.app.bind('<Return>', self.enter_key)
        self.app.bind("<Escape>", self.exit_ui)