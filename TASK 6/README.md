# 📊 Task 6 - Word Count Tool

## 📌 Objective

Develop a Python application that analyzes a text file and provides useful statistics such as the total number of words, lines, and characters. The application also performs word frequency analysis to identify the most commonly used words in the text.

---

## 🚀 Features

- 📄 Reads text from a file
- 🔢 Counts the total number of words
- 📏 Counts the total number of characters
- 📑 Counts the total number of lines
- 📊 Displays the top 10 most frequently used words
- ⚠️ Handles file-related exceptions gracefully
- 🖥️ Simple menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- Collections Module (`Counter`)
- String Module
- File Handling

---

## 📁 Project Structure

```
Task-6-Word-Count-Tool/
│── word_count.py
│── sample.txt
│── README.md
```

---

## 📄 Sample Input File (sample.txt)

```text
Python is an easy programming language.

Python is widely used for web development.

Python is also used in Artificial Intelligence.

Learning Python is fun and interesting.
```

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Python-Development-Internship.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Task-6-Word-Count-Tool
```

### Step 3: Run the Program

```bash
python word_count.py
```

---

## 💻 Sample Output

### Main Menu

```text
========== WORD COUNT TOOL ==========
1. Analyze File
2. Exit

Enter your choice: 1
```

---

### File Analysis

```text
========== FILE ANALYSIS ==========

Total Characters : 148
Total Words      : 22
Total Lines      : 7

Top 10 Most Common Words
-----------------------------------
python          4
is              4
used            2
an              1
easy            1
programming     1
language        1
widely          1
for             1
web             1
```

---

### File Not Found

```text
========== WORD COUNT TOOL ==========
1. Analyze File
2. Exit

Enter your choice: 1

❌ File not found.
```

---

## 🧠 Concepts Used

- File Handling
- String Manipulation
- Collections (`Counter`)
- Exception Handling
- Functions
- Loops
- Conditional Statements

---

## 📚 Learning Outcomes

- Learned how to read text files in Python.
- Performed text analysis using Python.
- Counted words, characters, and lines efficiently.
- Implemented word frequency analysis using the `Counter` class.
- Improved understanding of exception handling and string processing.

---

## 🔮 Future Enhancements

- 📈 Display a graphical representation of word frequency using Matplotlib.
- 💾 Export the analysis report to a text or CSV file.
- 📂 Allow users to select any text file for analysis.
- 🚫 Ignore common stop words such as "the", "is", and "and".
- 🖥️ Develop a GUI version using Tkinter.

---

## 👨‍💻 Author

**Sindhu Gedam**

B.Tech Computer Science and Engineering (CSE)

Python Developer | Aspiring Software Engineer

---

## ⭐ If you found this project useful, please consider giving it a star on GitHub!
