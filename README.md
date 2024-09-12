# Finance Tool
This financial tool is an all-in-one personal finance management tool. It helps users track financial transactions, manage personal budgets efficiently, and perform calculations.

# Features

1. Transaction Tracker:
   - Logs financial transactions (e.g. income, expenses).
   - Provides a history of past transactions for easy review.
   - Categorizes transactions to help users track spending.
2. Budget Manager:
   - Allows users to set monthly/weekly budgets.
   - Tracks spending against the set budgets.
   - Alerts users when they are close to or exceeding their budget limits.
  
# Table of Contents

<details>
   <Summary>Table of Contents</Summary>

   - [Installation](#installation)
   - [Usage](#usage)
      - [Transaction Tracker](#transaction-tracker)
      - [Budget Manager](#budget-manager)
      - [Calculator](#calculator)
   - [Project Structure](#project-structure)
   - [Contributing](#contributing)
   - [License](#licesnse)
</details>

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kngk0/financeproject.git
   cd financeproject
2. **Install dependencies**:
   This project does not have external dependencies.
3. **Run the program**:
   ```bash
   python main.py

## Usage

## Transaction Tracker

The **Transaction Tracker** helps you record your financial transactions.

1. Choose "Transaction Tracker" from the main menu.
2. Add a transaction by specifying the amount, date, category, and type (income/expense).
3. View the transaction history or filter by date/category.

## Budget Manager

The **Budget Manager** allows you to set and manage a personal budget.

1. Select "Budget Manager" from the main menu.
2. Set your desired budget for a specified period (e.g., monthly)
3. Add expenses and income; the Budget Manager will track your progress.
4. The app will notify you if you're nearing or exceeding your set budget.

## Calculator

The **Calculator** allows you to perform basic arithmetic operations.

1. Start the calculator from the main menu.
2. Enter the arithmetic expression you would like to calculate.
3. The result will be displayed instantly.

## Project Structure

Here's an overview of the project structure:

- **finance tool/**
   - **finance.py**: The entry point for the application
   - **transactionTracking/**
      - `transactionTracking.py`: Manages transactions and stores data.
      - `__init__.py`: Initializes the transaction tracker module.
   - **budgetManagement/**
      - `budgetManagement.py`: Handles budget-related tasks.
      - `__init__.py`: Initializes the budget manager module.
  - **calculator/**
     - `calculator.py`: Handles arithmetic operations.
     - `__init__.py`: Initializes the calculator module
   - **docs/**
      - `README.md`: Documentation for the project.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch)
6. Open a pull request.

## License

This project is licensed under the MIT License

## Future Improvements

- Add data persistence to save transaction and budget data between sessions.
- Implement advanced budgeting features like recurring transactions.
- Develop a graphical user interface (GUI) for ease of use.
- Expand the calculator with scientific functions.
