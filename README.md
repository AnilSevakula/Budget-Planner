# Simple Budget Planner
A command-line Python application to help you track your income and expenses.

#### Video Demo: 
#### Description:

Simple Budget Planner is a Python command-line application that allows users to manage their personal finances by tracking income and daily expenses. This tool was created as a final project for CS50’s Introduction to Programming with Python.

The goal of the project was to simulate a real-world budget tracking tool using fundamental programming concepts such as conditionals, loops, file I/O, error handling, and functions. It helps users input their monthly income, categorize their expenses, edit or delete them as needed, and view a detailed summary of their spending habits.

---

## Project Structure

- **`budget_planner.py`** – This is the main application file. It contains all the core logic for running the program including:
  - `load_data()` to read and load saved data from a text file.
  - `add_expense()` to allow users to input and categorize a new expense.
  - `set_income()` to update or set the income amount.
  - `delete_expense()` and `edit_expense()` to modify or remove existing entries.
  - `view_expenses()` and `view_summary()` to view detailed listings and summaries of the financial data.
  - `clear()` to delete all data if needed.
  - A `main()` function to serve as the CLI menu loop.

- **`data.txt`** – This file is automatically created and updated by the program. It serves as the data storage for income and expenses. The first line contains the income, and each subsequent line contains an expense in the format `category,amount`.

- **`test_project.py`** – A Python unittest file that verifies the correctness of core logic functions like saving and loading data, adding expenses, and managing entries without affecting the live data file.

- **`README.md`** – This file you are currently reading. It documents the purpose, functionality, and structure of the project.

---

## Design Decisions

One key design decision was to use a simple text file (`data1.txt`) for data storage instead of a database or CSV/JSON format. This was intentional to keep the project aligned with the concepts taught in CS50P. The program ensures that data is preserved across sessions by appending or rewriting this file depending on the user’s actions.

To make the application user-friendly and resilient, robust error handling was added, particularly around user input. Invalid inputs (like strings instead of numbers or negative values) are handled gracefully with informative prompts.

The function `write_all_data()` was created to encapsulate file-writing logic and reduce redundancy when updating data after edits or deletions. This also makes the code more modular and easier to test.

---

## Usage

To run the program, simply execute the Python file:

```bash
python project.py
