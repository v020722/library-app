# 📚 Library Management System (Console-Based)

## 📝 Overview

This Python-based **Library Management System** is an object-oriented console application that allows users to:
- Register and log in as **borrowers**
- Borrow and return **library items**
- Pay fines
- View and manage library inventory as an **administrator**

It supports various item types including **Books**, **Audiobooks**, and **Periodicals**, and uses a **Binary Search Tree** for organizing the catalog.

---

## 🔧 Features

### 👤 Borrower
- Register and login with credentials
- Rent and return items
- View list of currently rented items
- Pay library fines

### 👨‍💼 Administrator
- Authenticate via username and password
- Add and remove items in the library
- Display the library catalog (sorted by title)
- View registered borrowers and their rentals

---

## 🗃️ System Structure

### 📁 Key Modules

- `main.py` – Runs the main menu and coordinates borrower/admin operations.
- `book_class.py` – Book item class.
- `audiobook_class.py` – Audiobook class extending Book, with narrator and duration.
- `item_class.py` – Base class for all library items.
- `borrower_class.py` – Borrower class with rental and fine functionalities.
- `administrator_class.py` – Admin with login and catalog control.
- `librarytree_class.py` – Binary Search Tree implementation for library catalog.
- `borrowerlist_class.py` – Doubly linked list of borrowers.
- `borrowers.csv` – CSV file to import borrower data at startup.

---

## 🔄 Library Catalog

Uses a **Binary Search Tree** (BST) to:
- Insert new items in alphabetical order of title
- Search for items efficiently
- Remove items while maintaining BST structure
- Display the entire catalog in-order (alphabetically)

---

## 🧪 Sample Items Added by Default

```python
Book("The Adventures of Sally", ...)
Book("Classroom Chronicles: A Journey Through Education", ...)
Periodical("People", ...)
Audiobook("Escape Room", ...)
```

---

## 💾 Borrower CSV Format

Your CSV file should contain headers like:

```
first_name,last_name,account_number,username,password
```

Each row defines a borrower, which will be loaded on program start.

---

## 🚀 How to Run

1. Ensure Python 3 is installed.
2. Place your `borrowers.csv` file in the desired path.
3. Run the program:
   ```bash
   python main.py
   ```
4. Input the path to the CSV file when prompted:
   ```
   Enter the full path to the CSV file containing borrower data:
   ```

---

## 🧠 OOP Concepts Demonstrated

- **Inheritance**: `Book`, `Audiobook`, `Periodical` extend from `Item`.
- **Encapsulation**: User data is managed securely within classes.
- **Polymorphism**: Shared methods like `display_details()` behave differently based on item type.
- **Data Structures**:
  - **Binary Search Tree** for item catalog
  - **Doubly Linked List** for borrower management
  - **Linked List** for borrowed item tracking

---

## 👩‍💻 Developed By

**Vijeta d/o Senthil Nathan**
