from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Entry:
    """
    Representation of a day.
    """
    date: date = field(default=None)
    left: int = field(default=0)
    right: int = field(default=0)

    @property
    def total(self):
        """
        Sum of left and right.

        Returns:
            int:
        """
        return self.left + self.right

    def set_date_string(self, date_string: str) -> Entry:
        """

        Args:
            date_string: str: new date in string form.

        Returns:
            self
        """
        match date_string.lower():
            case 'today':
                self.date = date.today()
            case _:
                self.date = date.fromisoformat(date_string)

        return self

    def add(self, amount: int = 1, *, is_left: bool = False, is_right: bool = False) -> Entry:
        """
        Add an amount to either left and/or right.

        Args:
            amount: int: Amount to increase by. Default is 1.
            is_left: bool: Left side. Defaults to False.
            is_right: bool: Right side. Default is False

        Returns:
            self
        """
        if amount < 1:
            raise ValueError("Amount must be greater than 0")
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer")
        if not isinstance(is_left, bool):
            raise TypeError("Left must be bool")
        if not isinstance(is_right, bool):
            raise TypeError("Right must be bool")

        if is_left:
            self.left += int(amount)
        if is_right:
            self.right += int(amount)
        return self
