# Library Inventory CLI

## Project Overview
This is a simple Command Line Interface (CLI) based Library Management System built using Python. It allows users to manage a small library inventory by adding books, issuing them, returning them, searching by title, and viewing all stored books. Data is stored in a JSON file to maintain persistence between runs.

The project is structured in a modular way using separate folders for the CLI logic, the library logic, and test files.

## Features
- Add a new book to the library
- Prevent duplicate ISBN entries
- Issue a book
- Return a book
- Search books by title
- View all books in the inventory
- Data persistence using `library.json`
- Logging using `library.log`

## Folder Structure

requirements.txt  

CLI  
└── main.py  

Library  
├── book.py  
├── inventory.py  
└── __init__.py  

Test  
└── test.py  

# Quick Start

**Requirements**

- Ensure Python 3.x is installed on your machine.

**Setup**

1. Download or clone this repository.

2. Open a terminal and go to the project folder:


# How to Use

Launch the program by executing `main.py` from the CLI folder.

# Running Tests (Bonus)

This project includes unit tests to verify the logic of the Book class. To run the tests:
```
python -m unittest Test/test.py
```

# Author

Name: SAURABH
Date: 7/12/25
