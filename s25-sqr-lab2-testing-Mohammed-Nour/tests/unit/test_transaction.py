# - In this file, you have to add your tests on Transaction module.
# - See, app/transaction.py
# - Test transaction with different types - deposit, withdraw and transfer
# - Use mocks accordingly

import pytest
from unittest.mock import MagicMock
from app.transaction import Transaction


@pytest.fixture
def mock_database():
    """Fixture to create a mock database instance for testing."""
    db = MagicMock()
    return db


def test_deposit(mock_database):
    """Test the deposit method of the Transaction class."""
    mock_database.get_account.return_value = (1, 1, "checking", 1000)

    transaction = Transaction(mock_database)
    transaction.deposit(1, 500)  # Deposit 500

    mock_database.update_account_balance.assert_called_once_with(1, 1500)
    mock_database.add_transaction.assert_called_once_with(None, 1, 500,
                                                          "deposit")


def test_withdraw(mock_database):
    """Test the withdraw method of the Transaction class."""
    mock_database.get_account.return_value = (1, 1, "checking", 1000)

    transaction = Transaction(mock_database)
    transaction.withdraw(1, 500)  # Deposit 500

    mock_database.update_account_balance.assert_called_once_with(1, 500)
    mock_database.add_transaction.assert_called_once_with(1, None, 500,
                                                          "withdrawal")
