"""
Author: Zack Hankin
Started: 18/01/2023
"""
from __future__ import annotations

import pytest

from rosa_health_tracker.data.entry import *


@pytest.fixture()
def default_entry():
    """
    Pytest fixture returning an Entry(left=5, right=5).
    """
    return Entry(left=5, right=5)
