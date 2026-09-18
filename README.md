# Week 3: Object-Oriented Programming (OOP) & Standard Libraries

This repository covers **Week 3** of the Python Programming Course, focusing on building structured, modular programs using Object-Oriented Programming concepts and Python standard libraries.

---

## 📌 Topics Covered

* **Core OOP Concepts:** Classes, Objects, and Constructors (`__init__`)
* **Advanced OOP:** Inheritance and Polymorphism
* **Robust Programming:** Exception handling (`try`, `except`, `finally`)[cite: 1]
* **Python Built-in Modules:** `math`, `random`, and `datetime`[cite: 1]

---

## 📂 Assignments

### 1. Bank Account Class
A banking simulation implementing standard account operations[cite: 1]:
* `deposit(amount)`: Add funds to the account[cite: 1].
* `withdraw(amount)`: Deduct funds with balance validation[cite: 1].
* `display_balance()`: Show the current available balance[cite: 1].

### 2. Library Management System (OOP)
An inventory and user borrowing system to manage book lifecycle[cite: 1]:
* Add and remove books from the library catalog[cite: 1].
* Issue books to users and process returns[cite: 1].

### 3. Calculator Class with Exception Handling
A modular calculator performing arithmetic with error handling for edge cases, such as `ZeroDivisionError` and `ValueError`[cite: 1].

---

## 🚀 Mini Project: OOP-Based Billing System

A command-line retail checkout system demonstrating real-world class design and object interaction[cite: 1].

* **`Product` Class:** Models inventory items with attributes: `name`, `price`, and `quantity`[cite: 1].
* **`Bill` Class:** Manages the cart, computes line items, applies taxes, and calculates the final total[cite: 1].
* **Tabular Output:** Displays a clean, itemized receipt formatted for clarity[cite: 1].

---

## 🛠️ Getting Started

### Prerequisites
* Python 3.8+ installed (uses only standard library modules)[cite: 1]

### Run the Projects
Clone the repository and run any script directly:

```bash
git clone [https://github.com/your-username/week-3-python-oop.git](https://github.com/your-username/week-3-python-oop.git)
cd week-3-python-oop

# Run assignments
python assignments/bank_account.py
python assignments/library_system.py
python assignments/calculator.py

# Run mini project
python mini_project/billing_system.py
