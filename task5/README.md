# 💱 Task 5 - Currency Converter

## 📌 Objective

Develop a Python application that converts one currency into another using real-time exchange rates obtained from an online API. The application accepts user input, fetches the latest exchange rates, performs the conversion, and handles invalid inputs gracefully.

---

## 🚀 Features

- 🌍 Convert between multiple international currencies
- 📡 Fetch real-time exchange rates using an API
- 💰 Accurate currency conversion
- ⚠️ Handles invalid currency codes
- 🌐 Handles internet connection errors
- 🖥️ Simple and user-friendly command-line interface

---

## 🛠️ Technologies Used

- Python 3
- Requests Library
- Exchange Rate API

---

## 📦 Required Library

Install the required library before running the program.

```bash
pip install requests
```

---

## 📁 Project Structure

```
Task-5-Currency-Converter/
│── currency_converter.py
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
cd Task-5-Currency-Converter
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Program

```bash
python currency_converter.py
```

---

## 💻 Sample Input

```text
==================================================
           CURRENCY CONVERTER
==================================================

Available Currencies:
USD  INR  EUR  GBP  JPY  AUD  CAD  CNY

Enter From Currency: INR
Enter To Currency: USD
Enter Amount: 1000
```

---

## ✅ Sample Output

```text
========== RESULT ==========

1000.00 INR = 11.62 USD
```

> **Note:** The conversion result may vary because exchange rates are fetched in real time from the API.

---

## ⚠️ Error Handling

### Invalid Currency Code

```text
Enter From Currency: ABC

Invalid source currency.
```

---

### Invalid Amount

```text
Enter Amount: abc

Please enter a valid amount.
```

---

### No Internet Connection

```text
Unable to connect to the currency server.
```

---

## 🧠 Concepts Used

- API Integration
- HTTP Requests
- JSON Data Parsing
- Exception Handling
- Conditional Statements
- User Input Validation

---

## 📚 Learning Outcomes

- Learned how to consume REST APIs using Python.
- Understood how to work with JSON data.
- Implemented real-time currency conversion.
- Improved exception handling for network and input-related errors.
- Built a practical application using live data.

---

## 🔮 Future Enhancements

- 💾 Save conversion history.
- 📊 Display exchange rate history.
- 🌍 Automatically list all supported currencies.
- 🔄 Perform multiple conversions without restarting the application.
- 🖥️ Build a graphical user interface (GUI) using Tkinter.
- 📱 Develop a web-based version using Flask or Django.

---

## 👨‍💻 Author

**Sindhu Gedam**

B.Tech Computer Science and Engineering (CSE)

Python Developer | Aspiring Software Engineer

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
