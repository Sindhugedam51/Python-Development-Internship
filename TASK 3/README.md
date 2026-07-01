# 📂 Task 3 - Basic File Handling

## 📌 Objective

Develop a Python program that reads data from a text file, performs operations like finding and replacing specific words, 
and saves the modified content back to the file. The program also handles file-related exceptions gracefully.

---

## 🚀 Features

- 📖 Read text from a file
- 🔍 Find and replace specific words
- 💾 Save the updated content to the same file
- ⚠️ Handle file-related exceptions
- 🖥️ Simple menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- File Handling
- Exception Handling
- String Manipulation

---

## 📁 Project Structure

```
Task-3-Basic-File-Handling/
│── file_handler.py
│── sample.txt
│── README.md
```

---

## 📄 Sample Input File (sample.txt)

```text
Python is an easy programming language.
Python is used for web development.
Python is also used in Artificial Intelligence.
Learning Python is fun.
```

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/yourusername/Python-Development-Internship.git
```

2. Navigate to the project folder.

```bash
cd Task-3-Basic-File-Handling
```

3. Run the program.

```bash
python file_handler.py
```

---

## 💻 Sample Output

### Menu

```text
========== BASIC FILE HANDLING ==========
1. View File
2. Find & Replace Word
3. Exit

Enter your choice: 1
```

---

### View File

```text
----- FILE CONTENT -----

Python is an easy programming language.
Python is used for web development.
Python is also used in Artificial Intelligence.
Learning Python is fun.

------------------------
```

---

### Find and Replace

**Input**

```text
Enter your choice: 2

Enter the word to replace: Python
Enter the new word: Java
```

**Output**

```text
✅ Word replaced successfully!
```

---

### Updated File

```text
Java is an easy programming language.
Java is used for web development.
Java is also used in Artificial Intelligence.
Learning Java is fun.
```

---

### File Not Found

```text
========== BASIC FILE HANDLING ==========
1. View File
2. Find & Replace Word
3. Exit

Enter your choice: 1

❌ Error: File not found.
```

---

## 🧠 Concepts Used

- File Handling (`open()`)
- Read and Write Operations
- Exception Handling (`try-except`)
- String Methods (`replace()`)
- Functions
- Conditional Statements
- Loops

---

## 📚 Learning Outcomes

- Learned how to read and write files in Python.
- Implemented word search and replacement.
- Handled file-related exceptions effectively.
- Built a menu-driven Python application.

---

## 👨‍💻 Author

**Sindhu Gedam**

B.Tech CSE Student | Python Developer 
