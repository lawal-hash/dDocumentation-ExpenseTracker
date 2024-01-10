import logging
from typing import Dict, List
from pydantic import BaseModel, validate_call
from .expense import Expense


class ExpenseDatabase(BaseModel):
    """
    Manages a collection of Expense objects
    """
    expenses : List = []
    
    def __repr__(self) -> str:
        return "ExpenseDatabase()"

    def __len__(self) -> int:
        return len(self.expenses)

    @validate_call
    def add_expense(self, expense: Expense) -> None:
        """Adds an expense to the database.

        Args:
            expense (Expense): the expense to add to the database.
        """
        self.expenses.append(expense)
        print(f"{expense} successfully added to ExpenseDatabase")

    @validate_call
    def remove_expense(self, expense_id: str) -> None:
        """Removes an expense from the database.

        Args:
            expense_id (str): A unique identifier for an expense.
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense_id)
                return None
        print(f"Expense ID: {expense_id} successfully removed from ExpenseDatabase")

    @validate_call
    def get_expense_by_id(self, expense_id: str) -> Expense:
        """Retrieves an expense from the database by its unique identifier.

        Args:
            expense_id (str): A unique identifier for an expense.
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense

    @validate_call
    def get_expense_by_title(self, expense_title: str) -> List:
        """Retrieves a list of expenses from the database by their title.

        Args:
            expense_title (str): The title of the expense.

        Returns:
            List: A list of expenses with the given title.
        """
        return [
                expense for expense in self.expenses if expense.title == expense_title
            ]


    def to_dict(self) -> List[Dict]:
        """
        Returns a list of dictionaries representing the expenses in the database.

        Returns:
            List[Dict]: A list of dictionaries representing the expenses in the database.
        """
        return [expense.to_dict() for expense in self.expenses]
