# - In this file, you have to write an E2E test on Bank project.
# - See, app/bank.py
# - For understanding purposes, you can interact with main.py
# - Create a real life usage scenario for this project and follow the order for testing components
# - Make sure that the test tests almost all of the functionalities of the project.
from app.bank import Bank


def test_bank():
    # Initialize Bank with an in-memory database
    bank = Bank(db_path=':memory:')

    # Step 1: Add a new customer (Alice)
    alice_id = bank.add_customer("Alice", "123 Street")
    assert alice_id is not None, "Failed to add Alice"

    # Verify Alice is in the customer list
    customers = bank.get_all_customers()
    assert len(customers) == 1, "Customer list should have one customer"
    assert customers[0][0] == alice_id, "Alice's ID mismatch"
    assert customers[0][1] == "Alice", "Alice's name mismatch"
    assert customers[0][2] == "123 Street", "Alice's address mismatch"

    # Step 2: Update Alice's details
    bank.update_customer_details(alice_id, "Alice Smith", "456 Avenue")
    updated_customers = bank.get_all_customers()
    updated_alice = next(c for c in updated_customers if c[0] == alice_id)
    assert updated_alice[1] == "Alice Smith", "Alice's name not updated"
    assert updated_alice[2] == "456 Avenue", "Alice's address not updated"

    # Step 3: Open two accounts for Alice (checking and savings)
    checking_id = bank.open_account(alice_id, "checking", 0.0)
    savings_id = bank.open_account(alice_id, "savings", 100.0)
    assert checking_id != savings_id, "Account IDs should be different"

    # Check Alice's accounts
    alice_accounts = bank.get_customer_accounts(alice_id)
    assert len(alice_accounts) == 2, "Alice should have two accounts"

    # Verify account details
    checking_account = bank.get_account(checking_id)
    assert checking_account is not None, "Checking account not found"
    assert checking_account[2] == "checking", "Checking account type mismatch"
    assert checking_account[3] == 0.0, "Checking account initial balance mismatch"

    savings_account = bank.get_account(savings_id)
    assert savings_account is not None, "Savings account not found"
    assert savings_account[2] == "savings", "Savings account type mismatch"
    assert savings_account[3] == 100.0, "Savings account initial balance mismatch"

    # Step 4: Deposit 1000 into checking account
    bank.deposit_to_account(checking_id, 1000.0)
    checking_account = bank.get_account(checking_id)
    assert checking_account[3] == 1000.0, "Deposit failed to update balance"

    # Check deposit transaction
    checking_transactions = bank.get_account_transactions(checking_id)
    assert len(checking_transactions) == 1, "Deposit transaction not recorded"
    assert checking_transactions[0][3] == 1000.0, "Deposit amount mismatch"
    assert checking_transactions[0][4] == "deposit", "Transaction type mismatch"

    # Step 5: Withdraw 200 from checking account
    bank.withdraw_from_account(checking_id, 200.0)
    checking_account = bank.get_account(checking_id)
    assert checking_account[3] == 800.0, "Withdrawal failed to update balance"

    # Check withdrawal transaction
    checking_transactions = bank.get_account_transactions(checking_id)
    assert len(checking_transactions) == 2, "Withdrawal transaction not recorded"
    assert checking_transactions[1][3] == 200.0, "Withdrawal amount mismatch"
    assert checking_transactions[1][4] == "withdrawal", "Transaction type mismatch"

    # Step 6: Add another customer (Bob)
    bob_id = bank.add_customer("Bob", "789 Road")
    assert bob_id is not None, "Failed to add Bob"

    # Verify Bob is in the customer list
    customers = bank.get_all_customers()
    assert len(customers) == 2, "Customer list should have two customers"

    # Step 7: Open an account for Bob
    bob_checking_id = bank.open_account(bob_id, "checking", 500.0)
    bob_account = bank.get_account(bob_checking_id)
    assert bob_account[3] == 500.0, "Bob's account initial balance mismatch"

    # Step 8: Transfer 300 from Alice's checking to Bob's checking
    bank.transfer_between_accounts(checking_id, bob_checking_id, 300.0)

    # Check Alice's checking balance after transfer
    alice_checking = bank.get_account(checking_id)
    assert alice_checking[3] == 500.0, "Alice's balance after transfer incorrect"

    # Check Bob's checking balance after transfer
    bob_checking = bank.get_account(bob_checking_id)
    assert bob_checking[3] == 800.0, "Bob's balance after transfer incorrect"

    # Check transactions for transfer
    alice_transactions = bank.get_account_transactions(checking_id)
    assert len(alice_transactions) == 3, "Transfer transaction not recorded in Alice's account"
    assert alice_transactions[2][3] == 300.0, "Transfer-out amount mismatch"
    assert alice_transactions[2][4] == "transfer", "Transaction type mismatch"

    bob_transactions = bank.get_account_transactions(bob_checking_id)
    assert len(bob_transactions) == 1, "Transfer transaction not recorded in Bob's account"
    assert bob_transactions[0][3] == 300.0, "Transfer-in amount mismatch"
    assert bob_transactions[0][4] == "transfer", "Transaction type mismatch"

    # Step 9: Close Alice's savings account
    bank.close_account(savings_id)
    alice_accounts = bank.get_customer_accounts(alice_id)
    assert len(alice_accounts) == 1, "Savings account not closed"
    assert savings_id not in [acc[0] for acc in alice_accounts], "Closed account still listed"

    # Verify the closed account is removed
    closed_account = bank.get_account(savings_id)
    assert closed_account is None, "Closed account still exists"

    # Step 10: Delete Bob and verify his accounts are closed
    bank.delete_customer(bob_id)
    customers = bank.get_all_customers()
    assert len(customers) == 1, "Bob was not deleted"
    assert bob_id not in [c[0] for c in customers], "Bob's record still exists"

    # Verify Bob's account is closed
    bob_account_closed = bank.get_account(bob_checking_id)
    assert bob_account_closed is None, "Bob's account not closed"

    # Close the database connection
    bank.close_connection()