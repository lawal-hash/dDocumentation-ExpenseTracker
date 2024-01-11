from typing import Dict, Union
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel, UUID4, validate_call


class Expense(BaseModel):
    """
    Expense class to represent an individual financial expense.
    """

    title: str
    amount: float
    id: UUID4 = uuid4()
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = created_at

    def __repr__(self) -> str:
        return f"Expense(title={self.title}, amount={self.amount})"

    @validate_call(validate_return=True)
    def update(
        self, title: Union[str, None] = None, amount: Union[float, None] = None
    ) -> None:
        """update the title and/or amount of the expense.
        The updated_at attribute should be automatically set
        to the current UTC timestamp whenever an update occurs.

        Args:
            title (str, optional): the title of the expense. Defaults to None.
            amount (float, optional): the amount of the expense. Defaults to None.
        """
        if title:
            self.title = title
            self.updated_at = datetime.utcnow()
            print(f"Title successfully updated to  {title}")

        if amount:
            self.amount = amount
            self.updated_at = datetime.utcnow()
            print(f"Amount successfully updated to {amount}")

    @validate_call(validate_return=True)
    def to_dict(self) -> Dict:
        """
        Returns:
            Dict: a dictionary representation of the expense.
        """
        return {
            "id": str(self.id),
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
