# - In this file, you have to add your tests on Customer module.
# - See, app/customer.py
# - Test customer creation, loading, updating and deletion
# - Use mocks

from app.customer import Customer
from unittest.mock import MagicMock
import pytest


def test_failed_load_customer():
    # Create a mock database object
    mock_database = MagicMock()

    # Configure the mock database to return None (customer does not exist)
    mock_database.get_customer.return_value = None

    # Define the customer_id for the test
    customer_id = "1213123123"

    # Verify that a ValueError is raised when creating a Customer instance
    with pytest.raises(ValueError, match="Customer does not exist."):
        Customer(database=mock_database, customer_id=customer_id)


def test_successful_load_customer():
    # Create a mock database object
    mock_database = MagicMock()

    # Configure the mock database to return customer details
    mock_database.get_customer.return_value = ("1213123123",
                                               "John Doe", "123 Main St")

    # Define the customer_id for the test
    customer_id = "1213123123"

    # Create a Customer instance
    customer = Customer(database=mock_database, customer_id=customer_id)

    # Assert that the customer details are loaded correctly
    assert customer.customer_id == customer_id
    assert customer.name == "John Doe"
    assert customer.address == "123 Main St"
