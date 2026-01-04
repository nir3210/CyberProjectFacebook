<p align="center">
  A <strong>modular Python scraping application</strong> with a clean and modern <strong>GUI</strong>
</p>

This project is designed to be the perfect starting point for anyone looking to dive into web scraping, automation, and building cool GUI-driven tools. We hope it will be a great learning experience, especially since it can be hard to find scraping projects that are both **updated** and **actively maintained**.

---

## 📚 Table of Contents

* [✨ Features](#-features)
* [⚙️ Requirements](#️-requirements)
* [🚀 Getting Started: How to Run This Thing](#-getting-started-how-to-run-this-thing)
* [🔐 Facebook Authentication](#-facebook-authentication)
* [📦 What You Get (The Output)](#-what-you-get-the-output)
* [🧱 Project Structure](#-project-structure)
* [🧠 Our Design Philosophy](#-our-design-philosophy)
* [🛠️ Make It Your Own](#️-make-it-your-own)
* [⚠️ A Friendly Disclaimer](#️-a-friendly-disclaimer)
* [👤 The Authors](#-the-authors)

---

## ✨ Features

*   🖥️ **Modern & Intuitive GUI**: A clean interface built with the sleek `CustomTkinter` library. No command-line fuss.
*   🛒 **Multi-Platform Support**: Scrapes both Facebook Marketplace and Amazon product listings right out of the box.
*   🍪 **Secure & Password-Free Login**: Uses cookie-based authentication for Facebook, so you never have to hardcode your credentials.
*   🧩 **Clean Architecture**: A modular design that's easy to understand, debug, and build upon.
*   📄 **Organized Data Export**: All scraped data is neatly saved into a structured JSON file, ready for your projects.
*   ➕ **Built to Grow**: The codebase is designed from day one to make adding new marketplaces a breeze.

---

## ⚙️ Requirements

Before you fire it up, make sure you have these things ready:

*   **Python 3.13+** (we recommend the latest version).
*   **Google Chrome** (the browser this tool is built for, you can change but meaning you have to tinker with the files a bit).
*   **ChromeDriver**: This is a big one! Make sure its version **exactly matches** your Chrome version to avoid headaches.

---

## 🚀 Getting Started: How to Run This Thing

Getting this scraper running is super straightforward. Just follow these steps, and you'll be up and running in a couple of minutes.

### Step 1: Clone the Repository

First, you need to get the code onto your machine. Open up your terminal or command prompt and run this command:

```bash
git clone https://github.com/nir3210/CyberProjectFacebook.git

This will create a new folder called CyberProjectFacebook with all the project files inside.

Step 2: Navigate into the Project Directory

Now, move into the folder you just created:

cd CyberProjectFacebook
Step 3: Install the Required Libraries

The project depends on a few Python libraries. We've made it easy to install them all at once. Just run:

pip install -r requirements.txt

This will read the requirements.txt file and install everything you need.

Step 4: Run the Application!

You're all set! To launch the GUI, run the main script:


python Src/Main/main.py

That's it! The application window should pop up, and you're ready to start scraping.

🔐 Facebook Authentication

To scrape Facebook Marketplace, the tool needs to be logged in. Instead of asking for your password, we use a safer, more modern approach: browser cookies.

🔑 How it Works

The application securely authenticates by reading your session cookies from the Src/Settings/cookies.json file. This allows the scraper to browse Facebook just like you would, without ever knowing your password.

📝 How to Get Your Cookies

Log in to your Facebook account in Google Chrome.

Open Developer Tools (press F12 or Ctrl+Shift+I).

Go to the Application tab. On the left side, expand the Cookies section and click on https://www.facebook.com.

Use a browser extension like Get cookies.txt (JSON) or EditThisCookie to easily export your cookies in JSON format.

Save that exported data into a file named cookies.json right inside the Src/Settings/ folder.

OR:
run src/Modules/login.py

⚠️ TREAT YOUR COOKIES LIKE A PASSWORD! Never share the cookies.json file with anyone. It gives them complete access to your Facebook account.

📦 What You Get (The Output)

All the data you scrape is saved in a clean, easy-to-read JSON format. Each product entry is neatly organized and typically includes:

The product's title

The listed price

A direct URL to the listing page

Other useful bits of info (which can vary by platform)

🧱 Project Structure

Here’s a roadmap of the project. We’ve kept things organized so you can easily find your way around.

Facebook-Scraper/
│
├── requirements.txt      # All the Python packages you'll need
│
└── Src/
    ├── Main/
    │   └── main.py       # The entry point that kicks everything off
    │
    ├── UI/
    │   └── Ui.py         # The heart of the user interface (CustomTkinter)
    │
    ├── Modules/
    │   ├── amazon.py     # All the logic for scraping Amazon
    │   ├── facebook.py   # All the logic for scraping Facebook
    │   └── login.py      # Handles the clever cookie-based authentication
    │
    ├── Settings/
    │   └── cookies.json  # Your secret key! (Facebook session cookies go here)
    │
    └── Images/
        └── appicon.ico   # The application's icon
🧠 Our Design Philosophy

We built this project with one main goal in mind:

🛠️ Make It Your Own

Want to add a scraper for another site, like eBay or Etsy? Go for it! We designed it for exactly that.

Create a new Python file in the Src/Modules/ directory (e.g., ebay_scraper.py).

Write your scraping logic inside that new file.

Hook up your new module to the UI in Src/UI/Ui.py by adding a new button or option.

Make sure your new scraper saves its data in the same, consistent JSON format.

⚠️ A Friendly Disclaimer

This project is intended for educational and personal use ONLY.

Please be aware that web scraping might be against the Terms of Service of some websites.

Use this tool responsibly and ethically. Don't overload websites with requests.

The authors are not responsible for any misuse of this tool or for any account bans that may occur. You're using this at your own risk.

👤 The Authors

l1nc0lnwtff & nir3210

If you're using this project to learn, we highly encourage you to dive in, break things, fix them, and make it your own. That's the absolute best way to grow your skills!

⭐ If you find this project helpful or interesting, please consider giving it a star on GitHub!

Happy scraping! 🚀

