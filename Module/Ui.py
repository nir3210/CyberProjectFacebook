import sys
sys.dont_write_bytecode = True

import customtkinter as ctk
from customtkinter import CTkLabel, CTkFrame, CTkEntry, CTkButton

class UI:
    def __init__(self, app):
        self.app = app
        self.user_name = None
        self.password = None
        self.user_name_ui = None
        self.password_ui = None
        self.active_frame = None




        def login_ui(self):
            self.active_frame = CTkFrame(self.app, fg_color= '#262C3C')
            self.active_frame.pack(pady=10)

            self.user_name_ui =  CTkEntry(
                self.active_frame,

                fg_color= '#262C3C',
                text_color= '#ffffff',
                font=('Arial', 25),
                width=200
        )

            self.user_name_ui.pack(pady=10, padx=10)

        login_ui(self)
