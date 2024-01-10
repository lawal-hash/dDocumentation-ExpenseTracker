from typing import Dict
from uuid import uuid4
import logging
from datetime import datetime
from pydantic import BaseModel, validate_call

class Expense(BaseModel):
    """
    Expense class to represent an individual financial expense.
    """
    title : str
    amount: float
    id : str = str(uuid4())
    created_at : datetime = datetime.utcnow().isoformat()
    updated_at : datetime = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"Expense(title={self.title}, amount={self.amount})"
    @validate_call
    def update(self, title: str = None, amount: float = None) -> None:
        """update the title and/or amount of the expense.
        The updated_at attribute should be automatically set
        to the current UTC timestamp whenever an update occurs.

        Args:
            title (str, optional): the title of the expense. Defaults to None.
            amount (float, optional): the amount of the expense. Defaults to None.
        """
        # TODO : type hint str|None
        if title:
            self.title = title
            self.updated_at = datetime.utcnow().isoformat()
            print(f"Title successfully updated to  {title}")

        if amount:
            self.amount = amount
            self.updated_at = datetime.utcnow().isoformat()
            print(f"Amount successfully updated to {amount}")
            
    def to_dict(self) -> Dict:
        """
        Returns:
            Dict: a dictionary representation of the expense.
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
