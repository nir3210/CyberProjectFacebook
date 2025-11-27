import sys
sys.dont_write_bytecode = True

import customtkinter as ctk
from Src.UI.Ui import UI

class Main:
    def __init__(self, app):
        app.title("Facebook scraper")
        app.geometry("1000x600")
        app.wm_iconbitmap("Src/Images/appicon.ico")
        self.bg_color = "#262C3C"
        app.configure(fg_color=self.bg_color)

        mode_ui = UI(app)


if __name__ == "__main__":
    app = ctk.CTk()
    root = Main(app)
    app.mainloop()