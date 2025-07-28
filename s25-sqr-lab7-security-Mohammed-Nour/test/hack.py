from app import code as c  # Ensure this import statement correctly imports your updated code
import pytest
# Verifies that hash and verification are matching each other for SHA256
def test_collision():
    data1 = bytes.fromhex(
    'd131dd02c5e6eec4693d9a0698aff95c' '2fcab58712467eab4004583eb8fb7f89' 
    '55ad340609f4b30283e488832571415a' '085125e8f7cdc99fd91dbdf280373c5b' 
    'd8823e3156348f5bae6dacd436c919c6' 'dd53e2b487da03fd02396306d248cda0' 
    'e99f33420f577ee8ce54b67080a80d1e' 'c69821bcb6a8839396f9652b6ff72a70'
    )

    data2 = bytes.fromhex(
    'd131dd02c5e6eec4693d9a0698aff95c' '2fcab50712467eab4004583eb8fb7f89' 
    '55ad340609f4b30283e4888325f1415a' '085125e8f7cdc99fd91dbd7280373c5b' 
    'd8823e3156348f5bae6dacd436c919c6' 'dd53e23487da03fd02396306d248cda0' 
    'e99f33420f577ee8ce54b67080280d1e' 'c69821bcb6a8839396f965ab6ff72a70'
    )
    hasher = c.Hasher()
    hash1 = hasher.password_hash(data1)
    hash2 = hasher.password_hash(data2)
    assert hash1 != hash2, "The hash1 should not be equal to hash2"


def test_similar_hashing():

    hasher = c.Hasher()

    password = "abcd"

    hash_pass = hasher.password_hash(password)
    
    assert hash_pass != hasher.password_hash(password), "hasher generates the same hash for the same passowrd"

def test_television_purchase():
    tv_item = c.Item(type='product', description='tv', amount=1000.00, quantity=1)
    payment = c.Item(type='payment', description='invoice_4', amount=1e19, quantity=1)
    payback = c.Item(type='payment', description='payback_4', amount=-1e19, quantity=1)
    order_4 = c.Order(id='4', items=[payment, tv_item, payback])
    assert c.validorder(order_4) == 'Order ID: 4 - Payment imbalance: $-1000.00'

def test_valid_payments():
    small_item = c.Item(type='product', description='accessory', amount=3.3, quantity=1)
    payment_1 = c.Item(type='payment', description='invoice_5_1', amount=1.1, quantity=1)
    payment_2 = c.Item(type='payment', description='invoice_5_2', amount=2.2, quantity=1)
    order_5 = c.Order(id='5', items=[small_item, payment_1, payment_2])
    assert c.validorder(order_5) == 'Order ID: 5 - Full payment received!'

def test_total_amount_limit():
    num_items = 12
    items = [c.Item(type='product', description='tv', amount=99999, quantity=num_items)]
    for i in range(num_items):
        items.append(c.Item(type='payment', description='invoice_' + str(i), amount=99999, quantity=1))
    order_1 = c.Order(id='1', items=items)
    assert c.validorder(order_1) == 'Total amount payable for an order exceeded'

    # Put payments before products
    items = items[1:] + [items[0]]
    order_2 = c.Order(id='2', items=items)
    assert c.validorder(order_2) == 'Total amount payable for an order exceeded'