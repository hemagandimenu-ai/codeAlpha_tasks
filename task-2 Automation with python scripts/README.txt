# 📧 Task 2 - Email Address Extractor

## 📌 Project Overview

The **Email Address Extractor** is a Python automation script developed as part of the **CodeAlpha Python Programming Internship**.

This project automates the process of extracting email addresses from a text file. Instead of manually searching through a document, the program scans the file, identifies all valid email addresses using **Regular Expressions (Regex)**, and saves them into a separate text file.

This automation helps save time, reduces manual effort, and improves accuracy when processing large amounts of text data.

---

# 🎯 Objective

The main objective of this project is to automate the task of extracting email addresses from text files using Python.

The program performs the following operations:

- Reads data from a text file.
- Searches for valid email addresses.
- Extracts all email addresses automatically.
- Saves the extracted email addresses into a new text file.
- Displays the extracted email addresses on the console.

---

# ✨ Features

- 📄 Reads text from an input file.
- 📧 Extracts all valid email addresses.
- 💾 Saves extracted emails into another file.
- 🔍 Uses Regular Expressions (Regex).
- ⚡ Fast and efficient.
- 🖥️ Easy-to-use console application.
- 📂 Supports multiple email addresses in one file.

---

# 🛠 Technologies Used

- Python 3
- Regular Expressions (`re`)
- File Handling

---

# 📚 Python Concepts Used

- Variables
- Strings
- Lists
- File Handling
- Regular Expressions
- Loops
- Conditional Statements
- Functions (optional)

---

# 📁 Project Structure

```
Task-2-Email-Extractor/
│
├── main.py
├── input.txt
├── extracted_emails.txt
└── README.md
```

---

# ⚙️ How It Works

1. The user stores text inside **input.txt**.
2. The Python program reads the contents of the file.
3. A Regular Expression searches for valid email addresses.
4. All matched email addresses are stored in a list.
5. The extracted email addresses are written into **extracted_emails.txt**.
6. The program displays the extracted emails and the total count.

---

# ▶️ How to Run the Project

### Step 1

Clone the repository

```bash
git clone https://github.com/your-username/codeAlpha_tasks.git
```

### Step 2

Navigate to the project folder

```bash
cd Task-2-Email-Extractor
```

### Step 3

Run the program

```bash
python main.py
```

---

# 📥 Sample Input

Contents of **input.txt**

```
Hello Team,

Please contact us at support@gmail.com.

For HR queries:
hr@company.org

Sales:
sales@yahoo.com

Thank You.
```

---

# 📤 Sample Output

Console Output

```
===== Email Address Extractor =====

Email addresses found:

support@gmail.com
hr@company.org
sales@yahoo.com

Total Emails Extracted: 3

Saved successfully to extracted_emails.txt
```

---

# 📄 Output File

Contents of **extracted_emails.txt**

```
support@gmail.com
hr@company.org
sales@yahoo.com
```

---

# 🧠 Regular Expression Used

```python
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

This Regular Expression identifies valid email addresses by matching:

- Username
- @ symbol
- Domain name
- Domain extension

---

# 🚀 Future Enhancements

- Remove duplicate email addresses.
- Export emails to CSV or Excel.
- Validate email addresses.
- Extract phone numbers.
- Build a graphical user interface (GUI).
- Allow users to choose the input file.

---

# 📈 Learning Outcomes

By completing this project, I learned:

- Python File Handling
- Regular Expressions (Regex)
- Automation using Python
- Reading and Writing Files
- Working with Lists and Strings
- Organizing Python Projects
- Creating Professional GitHub Repositories

---

# 👩‍💻 Author

**Hemanjlai Gandimenu**

B.Tech Computer Science & Engineering Student

GitHub: https://github.com/hemagandimenu-ai

---

## ⭐ Acknowledgement

This project was developed as part of the **CodeAlpha Python Programming Internship** to practice Python automation, file handling, and regular expressions.
