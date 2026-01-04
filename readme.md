
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python 3.9+ compatible" />
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-green" alt="GUI built with CustomTkinter" />
  <img src="https://img.shields.io/badge/Status-Educational%20Use-orange" alt="For educational use only" />
</p>

<p align="center">
  A <strong>modular Python scraping application</strong> with a clean and modern <strong>GUI</strong>, built to gather product listings from both <strong>Facebook Marketplace</strong> and <strong>Amazon</strong>.
</p>

We built this project with **maintainability**, **readability**, and **extensibility** at its core. It's the perfect starting point for anyone looking to dive into web scraping, automation, and building cool GUI-driven tools.
I hope it will be a good learning experience for anyone since there is not a lot of information of updated and maintained 

---

## 📚 Table of Contents

* [✨ Features](#-features)
* [🧱 Project Structure](#-project-structure)
* [⚙️ Requirements](#️-requirements)
* [🚀 Installation & Usage](#-installation--usage)
* [🔐 Facebook Authentication](#-facebook-authentication)
* [📦 Output](#-output)
* [🧠 Design Philosophy](#-design-philosophy)
* [🛠️ Extending the Project](#️-extending-the-project)
* [⚠️ Disclaimer](#️-disclaimer)
* [👤 Authors](#-authors)

---

## ✨ Features

*   🖥️ **Modern & Intuitive GUI**: Built with the sleek `CustomTkinter` library for a great user experience.
*   🛒 **Multi-Platform Support**: Scrapes both Facebook Marketplace and Amazon product listings right out of the box.
*   🍪 **Secure Authentication**: Uses cookie-based authentication for Facebook, so you never have to expose your password in the code.
*   🧩 **Clean Architecture**: A modular design that's easy to understand and even easier to build upon.
*   📄 **JSON Data Export**: All scraped data is neatly saved into a structured and machine-readable JSON file.
*   ➕ **Easily Extendable**: The codebase is designed from the ground up to make adding new marketplaces a breeze.

---

## 🧱 Project Structure

Here’s a look at how the project is organized. The clear separation of concerns makes it easy to find what you're looking for!

```text
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
    │   ├── amazon.py     # Logic for scraping Amazon
    │   ├── facebook.py   # Logic for scraping Facebook
    │   └── login.py      # Handles the cookie-based authentication
    │
    ├── Settings/
    │   └── cookies.json  # Your secret key! (Facebook session cookies)
    │
    └── Images/
        └── appicon.ico   # The application's icon
⚙️ Requirements

Before you get started, make sure you have the following installed:

Python 3.9+ (this is the recommended version).

Google Chrome (the latest version is always best).

ChromeDriver: This is crucial! Make sure its version exactly matches your installed Chrome version.

Once you've got those, installing the necessary Python packages is just one command away:

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt```

---

## 🚀 Installation & Usage

Getting the scraper up and running is super simple. Just follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd Facebook-Scraper
    ```

3.  **Run the application:**
    ```bash
    python Src/Main/main.py
    ```

That's it! The GUI should pop up, and you'll be ready to start scraping.

---

## 🔐 Facebook Authentication

Scraping Facebook Marketplace requires you to be logged in. To do this securely without ever hardcoding your credentials, this tool cleverly uses your browser's session cookies.

### 🔑 How it Works

The application reads your session cookies from the following file: `Src/Settings/cookies.json`. By using these cookies, the scraper can access Facebook as if it were you, without ever needing your username or password.

### 📝 How to Get Your Cookies

1.  Log in to your Facebook account in Google Chrome.
2.  Open the **Developer Tools** by pressing `F12` or `Ctrl+Shift+I`.
3.  Go to the **Application** tab, and on the left-hand side, find **Cookies** -> `https://www.facebook.com`.
4.  Use a browser extension like **"Get cookies.txt"** or **"EditThisCookie"** to export your cookies in **JSON format**.
5.  Save the exported data into a file named `cookies.json` inside the `Src/Settings/` folder.

> ⚠️ **IMPORTANT**: Treat your `cookies.json` file like a password. **NEVER** share it with anyone, as it grants full access to your Facebook account.

---

## 📦 Output

All the juicy data you scrape is saved in a clean, easy-to-read **JSON format**. Each product entry in the JSON file typically includes:

*   Product title
*   Price
*   A direct URL to the listing
*   Other useful metadata (this varies depending on the platform)

---

## 🧠 Design Philosophy

This project was built on a few core principles to make it as robust and developer-friendly as possible:

*   🧩 **Modular**: Each marketplace has its own dedicated module, keeping the code clean and organized.
*   🔍 **Separation of Concerns**: The UI, scraping logic, and settings are all kept separate, making the code much easier to manage and debug.
*   📖 **Readable Code**: Clean, commented, and easy-to-understand code is a top priority. No one likes spaghetti code!
*   🚀 **Future-Proof**: The architecture is designed to make it simple to add more features or support new websites down the road.

---

## 🛠️ Extending the Project

Want to add a scraper for another site, like eBay or Etsy? Go for it! It's designed for exactly that.

1.  Create a new Python file in the `Src/Modules/` directory (e.g., `ebay_scraper.py`).
2.  Write the scraping logic for the new marketplace in that file.
3.  Hook your new module into the UI layer in `Src/UI/Ui.py` so you can trigger it from the app.
4.  Make sure it exports the results in the same, consistent JSON format.

---

## ⚠️ Disclaimer

This project is intended for **educational and personal use only**.

*   Be aware that web scraping may be against the **Terms of Service** of some websites.
*   Please use this tool responsibly and always respect the websites you are scraping.
*   The authors are **not responsible** for any misuse of this tool or for any account bans that may occur. You are using this at your own risk.

---

## 👤 Authors

**l1nc0lnwtff** & **nir3210**

If you're using this project to learn, we encourage you to dive in, break things, fix them, and make it your own. That's the best way to grow your skills!

---

⭐ If you find this project useful or interesting, please consider giving it a star on GitHub!

Happy scraping! 🚀