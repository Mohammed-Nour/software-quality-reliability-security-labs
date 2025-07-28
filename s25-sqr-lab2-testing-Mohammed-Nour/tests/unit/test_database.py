# - In this file, you have to add your tests on Database module.
# - See, app/database.py
# - Test most of the methods
# - Use mocks in proper parts
from unittest.mock import MagicMock, patch
import pytest
from app.database import Database


@pytest.fixture
def mock_db():
    """
    Pytest fixture to create a mock database connection.
    Uses patch to replace sqlite3.connect with a mock connection.
    """
    with patch("sqlite3.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        yield Database()


def test_add_customer(mock_db):
    """
    Test the add_customer method to ensure it correctly inserts a customer
    and returns the last inserted ID.
    """
    mock_db.conn.cursor().lastrowid = 1
    customer_id = mock_db.add_customer("John Doe", "123 Main St")
    assert customer_id == 1  # Ensure returned ID is correct
    mock_db.conn.cursor().execute.assert_called_with(
        """
        INSERT INTO customers (name, address) VALUES (?, ?)
        """, ("John Doe", "123 Main St")
    )


def test_get_customer(mock_db):
    """
    Test get_customer method to ensure it retrieves the correct customer data.
    """
    mock_db.conn.cursor().fetchone.return_value = (1, "John Doe",
                                                   "123 Main St")
    customer = mock_db.get_customer(1)
    assert customer == (1, "John Doe", "123 Main St")
    mock_db.conn.cursor().execute.assert_called_with(
        "SELECT * FROM customers WHERE customer_id = ?", (1,))


def test_update_customer(mock_db):
    """
    Test update_customer method to ensure it
    updates customer details correctly.
    """
    mock_db.update_customer(1, "Jane Doe", "456 Elm St")
    mock_db.conn.cursor().execute.assert_called_with(
        """
        UPDATE customers SET name = ?, address = ? WHERE customer_id = ?
        """, ("Jane Doe", "456 Elm St", 1)
    )


def test_delete_customer(mock_db):
    """
    Test delete_customer method to ensure it removes the correct customer.
    """
    mock_db.delete_customer(1)
    mock_db.conn.cursor().execute.assert_called_with(
        """
        DELETE FROM customers WHERE customer_id = ?
        """, (1,)
    )


def test_get_all_customers(mock_db):
    """
    Test get_all_customers method to ensure it retrieves all customers.
    """
    mock_db.conn.cursor().fetchall.return_value = [
        (1, "John Doe", "123 Main St"), (2, "Jane Doe", "456 Elm St")]
    customers = mock_db.get_all_customers()
    assert customers == [
        (1, "John Doe", "123 Main St"), (2, "Jane Doe", "456 Elm St")]
    mock_db.conn.cursor().execute.assert_called_with(
        "SELECT * FROM customers ORDER BY customer_id ASC")


def test_close(mock_db):
    """
    Test the close method to ensure the database connection is properly closed.
    """
    mock_db.close()
    mock_db.conn.close.assert_called_once()
