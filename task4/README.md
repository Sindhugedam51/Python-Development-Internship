# 🌐 Task 4 - Basic Web Scraper

## 📌 Objective

Develop a Python program that scrapes data from a website using the **Requests** and **BeautifulSoup** libraries. The application fetches web page content, extracts useful information such as news headlines, and displays it to the user.

---

## 🚀 Features

- 🌍 Connects to a live website
- 📥 Fetches webpage content using HTTP requests
- 🔍 Extracts news headlines from HTML
- 📋 Displays the latest headlines
- ⚠️ Handles network and connection errors gracefully

---

## 🛠️ Technologies Used

- Python 3
- Requests Library
- BeautifulSoup4

---

## 📦 Required Libraries

Install the required libraries before running the program.

```bash
pip install requests beautifulsoup4
```

---

## 📁 Project Structure

```
Task-4-Basic-Web-Scraper/
│── web_scraper.py
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Python-Development-Internship.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Task-4-Basic-Web-Scraper
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Program

```bash
python web_scraper.py
```

---

## 💻 Sample Output

```text
============================================================
               LATEST BBC NEWS HEADLINES
============================================================

1. AI is transforming education worldwide
2. Global markets continue to rise
3. Scientists discover new species
4. Technology companies announce innovations
5. Health experts release new guidelines
6. Sports championship begins today
7. Climate summit concludes successfully
8. New space mission launched
9. Researchers develop advanced AI model
10. Weather updates across Europe
```

> **Note:** The output will change every time you run the program because it fetches the latest data from the website.

---

## ⚠️ Error Handling

### No Internet Connection

```text
Error while connecting to the website.
HTTPSConnectionPool(host='www.bbc.com', port=443): Max retries exceeded...
```

### Invalid Website URL

```text
Error while connecting to the website.
404 Client Error: Not Found
```

---

## 🧠 Concepts Used

- Web Scraping
- HTTP Requests
- HTML Parsing
- Exception Handling
- Loops
- Functions

---

## 📚 Learning Outcomes

- Learned how to send HTTP requests using the Requests library.
- Understood HTML parsing using BeautifulSoup.
- Extracted useful information from web pages.
- Implemented exception handling for network-related errors.
- Built a simple real-world web scraping application.

---

## 🔮 Future Enhancements

- 💾 Save scraped headlines to a text file.
- 📄 Export data to CSV or Excel.
- 🌐 Allow users to enter a custom website URL.
- 🔍 Scrape article links along with headlines.
- 🖥️ Create a graphical user interface (GUI) using Tkinter.

---

## 👨‍💻 Author

**Sindhu Gedam**

B.Tech Computer Science and Engineering (CSE)

Python Developer | Aspiring Software Engineer

---

## ⭐ If you found this project useful, please consider giving it a star on GitHub!
