import os
import tempfile
import pytest
from project import (
    load_data, add_expense, set_income, delete_expense,
    edit_expense, write_all_data, view_expenses,
    view_summary, clear
)

TEST_FILE = "data.txt"


def test_write_all_data_and_load_data():
    income = 2000
    expenses = [("rent", 800), ("food", 150)]
    write_all_data(income, expenses)

    loaded_income, loaded_expenses = load_data()
    assert loaded_income == 2000
    assert loaded_expenses == [("rent", "800"), ("food", "150")]


def test_add_expense(monkeypatch):
    income = 1000
    expenses = []

    monkeypatch.setattr("builtins.input", lambda _: "shopping" if not expenses else "300")
    monkeypatch.setattr("builtins.input", lambda _: "300")
    expenses = []
    # Write income first to test append
    write_all_data(income, expenses)

    inputs = iter(["shopping", "300"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_expense(expenses)
    assert expenses[-1] == ("shopping", 300.0)

    _, loaded = load_data()
    assert loaded[-1] == ("shopping", "300.0")


def test_set_income(monkeypatch):
    expenses = [("food", 100)]
    inputs = iter(["2500"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    income = set_income(expenses)
    assert income == 2500

    loaded_income, loaded_expenses = load_data()
    assert loaded_income == 2500
    assert loaded_expenses[0] == ("food", "100")


def test_delete_expense(monkeypatch):
    income = 3000
    expenses = [("food", 200), ("travel", 300)]
    write_all_data(income, expenses)

    monkeypatch.setattr("builtins.input", lambda _: "1")
    delete_expense(income, expenses)

    assert len(expenses) == 1
    assert expenses[0][0] == "travel"

    loaded_income, loaded_expenses = load_data()
    assert loaded_income == 3000
    assert loaded_expenses == [("travel", "300")]


def test_edit_expense(monkeypatch):
    income = 4000
    expenses = [("groceries", 250), ("rent", 1200)]
    write_all_data(income, expenses)

    inputs = iter(["1", "2", "300"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    edit_expense(income, expenses)
    assert expenses[0] == ("groceries", 300.0)

    _, loaded_expenses = load_data()
    assert loaded_expenses[0] == ("groceries", "300.0")


def test_view_expenses(capsys):
    expenses = [("food", 100), ("books", 200)]
    view_expenses(expenses)
    output = capsys.readouterr().out
    assert "food : 100" in output
    assert "books : 200" in output


def test_view_summary(capsys):
    income = 5000
    expenses = [("rent", 1000), ("rent", 500), ("food", 300)]
    view_summary(income, expenses)
    output = capsys.readouterr().out
    assert "rent : 1500.0" in output
    assert "food : 300.0" in output
    assert "Total Expenses: 1800.0" in output
    assert "Balance: 3200.0" in output


def test_clear():
    write_all_data(1000, [("abc", 100)])
    clear()
    assert os.path.exists(TEST_FILE)
    with open(TEST_FILE, "r") as file:
        assert file.read() == ""
