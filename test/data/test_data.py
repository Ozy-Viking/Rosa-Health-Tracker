"""
Testing for data
"""
import pytest

from rosa_health_tracker.data.entry import *


def test_entry_null():
    entry = Entry()
    assert entry.left == 0
    assert entry.right == 0


def test_entry_right():
    entry = Entry(right=5)
    assert entry.right == 5
    assert entry.total == 5


def test_entry_left():
    entry = Entry(left=5)
    assert entry.left == 5
    assert entry.total == 5


def test_entry_both(default_entry: Entry):
    entry = default_entry
    assert entry.left == 5
    assert entry.right == 5
    assert entry.total == 10


def test_entry_set_date_string_today():
    entry = Entry()
    entry.set_date_string('today')
    assert entry.date == date.today()


def test_entry_set_date_string_date():
    entry = Entry()
    year = 2023
    month = 11
    day = 12
    entry.set_date_string(f'{year}{month}{day}')
    assert entry.date == date(year, month, day)


def test_entry_add_1_left(default_entry: Entry):
    entry = default_entry
    assert entry.left == 5 and entry.right == 5
    entry.add(is_left=True)
    assert entry.left == 6


def test_entry_add_1_right(default_entry: Entry):
    entry = default_entry
    assert entry.left == 5 and entry.right == 5
    entry.add(is_right=True)
    assert entry.right == 6


def test_entry_add_5_left(default_entry: Entry):
    entry = default_entry
    assert entry.left == 5 and entry.right == 5
    entry.add(5, is_left=True)
    assert entry.left == 10


def test_entry_add_5_right(default_entry: Entry):
    entry = default_entry
    assert entry.left == 5 and entry.right == 5
    entry.add(5, is_right=True)
    assert entry.right == 10


def test_entry_add_errors(default_entry: Entry):
    entry = default_entry
    with pytest.raises(ValueError):
        entry.add(-5, is_right=True)
    with pytest.raises(TypeError):
        entry.add('5', is_right=True)  # type: ignore
    with pytest.raises(TypeError):
        entry.add(is_right=1)  # type: ignore
    with pytest.raises(TypeError):
        entry.add(is_left=1)  # type: ignore


def test_entry_legs(default_entry: Entry):
    entry = Entry(left=5, right=5)
    assert entry.legs == (5, 5)
    entry.add(1, is_left=True)
    assert entry.legs == (6, 5)
