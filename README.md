# Expense Tracker
[![Build-sphinx-docs](https://github.com/lawal-hash/documentation-ExpenseTracker/actions/workflows/sphnix.yml/badge.svg?branch=main)](https://github.com/lawal-hash/documentation-ExpenseTracker/actions/workflows/sphnix.yml) [![CodeQL](https://github.com/lawal-hash/documentation-ExpenseTracker/actions/workflows/github-code-scanning/codeql/badge.svg?branch=main)](https://github.com/lawal-hash/documentation-ExpenseTracker/actions/workflows/github-code-scanning/codeql)[![pages-build-deployment](https://github.com/lawal-hash/documentation-ExpenseTracker/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://github.com/lawal-hash/documentation-ExpenseTracker/actions/workflows/pages/pages-build-deployment)


ExpenseTracker, a Python application, assesses and highlights object-oriented programming (OOP) skills in financial expense management. Comprising two pivotal classes, Expense and ExpenseDB, it models individual expenses with attributes like a unique identifier, title, amount, and timestamps in Coordinated Universal Time (UTC). The Expense class features methods for  updating details, and efficient conversion to a dictionary. As a manager for Expense objects, the ExpenseDB class facilitates addition, removal, retrieval of expenses.

## Run Locally

Clone the project

```bash
  git clone https://github.com/lawal-hash/ExpenseTracker.git
```

Install dependencies

```bash
  pip install poetry
  cd ExpenseTracker
  poetry install --no-root
  poetry shell
```

## Usage/Examples

```python
from src.expense import Expense
from src.expensedb import ExpenseDatabase


def main():
    expense_one = Expense(title="Spain", amount=80.00)
    expense_two = Expense(title="UK", amount=180.00)
    expense_three = Expense(title="Malaga", amount=300.00)


    expense_db = ExpenseDatabase()

    for expense in [expense_one, expense_two, expense_three]:
        expense_db.add_expense(expense)

if __name__ == "__main__":
    main()

```

```python
python main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
