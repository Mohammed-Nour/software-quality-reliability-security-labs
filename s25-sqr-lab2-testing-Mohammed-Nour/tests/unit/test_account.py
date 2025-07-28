# - In this file, you have to add your tests on Account module.
# - See, app/account.py
# - Test account creation and deletion
# - Use mocks


from app.account import Account
from unittest.mock import MagicMock


def test_create_account():
    # Create a mock database object
    mock_database = MagicMock()

    # Set up the return value for the mock database's add_account method
    mock_database.add_account.return_value = 75000000239847

    # Create an instance of Account with the mock database
    customer_id = "1213123123"
    account_type = "checking"
    balance = 500.0
    account = Account(database=mock_database, customer_id=customer_id,
                      account_type=account_type, balance=balance)

    # Assert that the account_id is set correctly
    assert account.account_id == 75000000239847

    # Assert that the mock database's add_account method was called with the
    mock_database.add_account.assert_called_once_with(customer_id,
                                                      account_type, balance)


def test_delete_account():
    # Create a mock database object
    mock_database = MagicMock()

    # Create an instance of Account with the mock database
    account = Account(database=mock_database)

    # Call delete_account on the instance
    account_id = 75000000239847
    assert account.delete_account(account_id) is None

    # Assert that the mock database's delete_account
    # method was called with the correct account_id
    mock_database.delete_account.assert_called_once_with(account_id)
