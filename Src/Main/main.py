import sys
import os

sys.dont_write_bytecode = True


SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import customtkinter as ctk
from UI.Ui import UI
import webbrowser


class Main:
    def __init__(self, app):
        app.title("Facebook Scraper")
        app.geometry("1500x600")

        
        icon_path = os.path.join(SRC_PATH, "Images", "appicon.ico")
        if os.path.exists(icon_path):
            app.wm_iconbitmap(icon_path)


        self.bg_color = "#272C3F"
        app.configure(fg_color=self.bg_color)




        self.window = UI(app)


if __name__ == "__main__":
    
    app = ctk.CTk()
    root = Main(app)
    app.mainloop()
