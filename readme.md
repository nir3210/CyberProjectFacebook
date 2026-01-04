🚀 Facebook & Amazon Marketplace Scraper
<p align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python 3.9+ compatible" />
<img src="https://img.shields.io/badge/GUI-CustomTkinter-green" alt="GUI built with CustomTkinter" />
<img src="https://img.shields.io/badge/Status-Educational%20Use-orange" alt="For educational use only" />
</p>
<p align="center">
A <strong>modular Python scraping application</strong> with a clean and modern <strong>GUI</strong>, built to gather product listings from both <strong>Facebook Marketplace</strong> and <strong>Amazon</strong>.
</p>

This project was developed with maintainability, readability, and extensibility at its core. It's the perfect starting point for anyone looking to dive into web scraping, automation, and building GUI-driven tools.
📚 Table of Contents

    ✨ Features

    🧱 Project Structure

    ⚙️ Requirements

    🚀 Installation & Usage

    🔐 Facebook Authentication

    📦 Output

    🧠 Design Philosophy

    🛠️ Extending the Project

    ⚠️ Disclaimer

    👤 Author

✨ Features

    🖥️ Modern & Intuitive GUI: Built with the sleek CustomTkinter library.

    🛒 Multi-Platform Support: Scrapes both Facebook Marketplace and Amazon product listings.

    🍪 Secure Authentication: Uses cookie-based authentication for Facebook, so you never have to store your password in the code.

    🧩 Clean Architecture: A modular design that's easy to understand and build upon.

    📄 JSON Data Export: All scraped data is neatly saved into a structured JSON file.

    ➕ Easily Extendable: The codebase is designed to make adding new marketplaces a breeze.

🧱 Project Structure

Here’s a look at how the project is organized. The clear separation of concerns makes it easy to find what you're looking for!
code Text

    
Facebook Scraper/
│
├── requirements.txt        # All the Python packages you'll need
├── Src/
│   ├── Main/
│   │   └── main.py         # The entry point that starts the application
│   │
│   ├── UI/
│   │   └── Ui.py           # The heart of the user interface (CustomTkinter)
│   │
│   ├── Modules/
│   │   ├── amazon.py       # All the logic for scraping Amazon
│   │   ├── facebook.py     # All the logic for scraping Facebook
│   │   └── login.py        # Handles the cookie-based authentication
│   │
│   ├── Settings/
│   │   └── cookies.json    # Your secret key! (Facebook session cookies)
│   │
│   └── Images/
│       └── appicon.ico     # The application's icon
│
└── Amazon/
    └── results.json        # An example of what scraped Amazon data looks like

  

⚙️ Requirements

Before you get started, make sure you have the following installed:

    Python 3.9+ (this is the recommended version).

    Google Chrome (the latest version is best).

    ChromeDriver: This is crucial! Make sure its version matches your installed Chrome version.

Once you have those, install the necessary Python packages with a single command:
code Bash

    
pip install -r requirements.txt

  

🚀 Installation & Usage

Getting the scraper up and running is simple. Just follow these steps:

    Clone the repository:
    code Bash

    
git clone <your-repository-url>

  

Navigate into the project directory:
code Bash

    
cd Facebook-Scraper

  

Run the application:
code Bash

        
    python Src/Main/main.py

      

That's it! The GUI should launch, and you'll be ready to start scraping.
🔐 Facebook Authentication

Scraping Facebook Marketplace requires you to be logged in. To do this securely and without hardcoding your credentials, this tool uses your browser's session cookies.
🔑 How it Works

The application reads your session cookies from the following file:
Src/Settings/cookies.json

By using cookies, the scraper can access Facebook as if it were you, without ever needing your username or password.
📝 How to Get Your Cookies

    Log in to your Facebook account in Google Chrome.

    Open the Developer Tools by pressing F12 or Ctrl+Shift+I.

    Go to the Application tab, and on the left-hand side, find Cookies -> https://www.facebook.com.

    Use a browser extension like "Get cookies.txt" or "EditThisCookie" to export your cookies in JSON format.

    Save the exported data into a file named cookies.json inside the Src/Settings/ folder.

    ⚠️ IMPORTANT: Treat your cookies.json file like a password. NEVER share it with anyone, as it grants full access to your Facebook account.

📦 Output

All the data you scrape is saved in a clean, easy-to-read JSON format. You can find an example of the output here:

Amazon/results.json

Each product entry in the JSON file typically includes:

    Product title

    Price

    A direct URL to the listing

    Other useful metadata (this varies depending on the platform)

🧠 Design Philosophy

This project was built on a few core principles to make it as robust and user-friendly as possible:

    🧩 Modular: Each marketplace has its own dedicated module, keeping the code organized.

    🔍 Separation of Concerns: The UI, scraping logic, and settings are all kept separate, making the code easier to manage and debug.

    📖 Readable Code: Clean, commented, and easy-to-understand code is a top priority.

    🚀 Future-Proof: The architecture is designed to make it simple to add more features or support new websites in the future.

🛠️ Extending the Project

Want to add a scraper for another site, like eBay or Etsy? It's easy!

    Create a new Python file in the Src/Modules/ directory (e.g., ebay.py).

    Write the scraping logic for the new marketplace in that file.

    Connect your new module to the UI layer in Src/UI/Ui.py so you can trigger it from the app.

    Make sure it exports the results in the same JSON format.

⚠️ Disclaimer

This project is intended for educational and personal use only.

    Be aware that web scraping may be against the Terms of Service of some websites.

    Please use this tool responsibly and respect the websites you are scraping.

    The author is not responsible for any misuse of this tool or for any account bans that may occur. Use it at your own risk.

👤 Author

l1nc0lnwtff & nir3210

If you're using this project to learn, I encourage you to dive in, modify the code, and make it your own. That's the best way to grow your skills!

⭐ If you find this project useful or interesting, please consider giving it a star on GitHub!

Happy scraping! 🚀