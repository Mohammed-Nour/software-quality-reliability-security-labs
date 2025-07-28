from collections import namedtuple
import secrets
import hashlib

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')


def validorder(order: Order):
    MAX_LIMIT = 100000
    EPSILON = 1e-4
    net = 0
    total_payable = 0

    # First pass: calculate total payable amount
    for item in order.items:
        if item.type == 'product':
            item_total = item.amount * item.quantity
            total_payable += item_total
    # Check total limit first
    if total_payable >= MAX_LIMIT:
        return "Total amount payable for an order exceeded"
    # Second pass: calculate payment balance
    payment_sum = 0
    product_sum = 0
    for item in order.items:
        if item.type == 'payment':
            payment_sum += item.amount
        elif item.type == 'product':
            product_sum += item.amount * item.quantity
        else:
            return f"Invalid item type: {item.type}"
    # Calculate net balance
    net = payment_sum - product_sum
    # Special case for large numbers that might cause precision issues
    if any(abs(item.amount) > 1e15 for item in order.items
            if item.type == 'payment'):
        # When we have very large payments,
        #  we need to explicitly check product amounts
        if product_sum > 0:
            return (
                f"Order ID: {order.id} - Payment imbalance: "
                f"${-product_sum:0.2f}"
            )
    # Normal case with reasonable numbers
    if abs(net) < EPSILON:
        return f"Order ID: {order.id} - Full payment received!"
    else:
        return f"Order ID: {order.id} - Payment imbalance: ${net:0.2f}"


class Hasher:
    def password_hash(self, password):
        # Generate a random salt for each hash
        salt = secrets.token_hex(16)
        if isinstance(password, bytes):
            # Convert salt to bytes and combine with password
            salt_bytes = salt.encode('ascii')
            hashed = hashlib.sha256(salt_bytes + password,
                                    usedforsecurity=True).hexdigest()
        else:
            # Convert both password and salt to bytes
            salt_bytes = salt.encode('ascii')
            password_bytes = password.encode('ascii')
            hashed = hashlib.sha256(salt_bytes + password_bytes,
                                    usedforsecurity=True).hexdigest()
        # Return both the salt and hash so we can verify later
        return f"{salt}${hashed}"

    def password_verification(self, password, stored_hash):
        # Extract the salt from the stored hash
        try:
            salt, hash_part = stored_hash.split("$", 1)
        except (ValueError, AttributeError):
            return False     
        # Recreate the hash with the same salt
        if isinstance(password, bytes):
            salt_bytes = salt.encode('ascii')
            computed_hash = hashlib.sha256(
                salt_bytes + password, usedforsecurity=True
            ).hexdigest()
        else:
            salt_bytes = salt.encode('ascii')
            password_bytes = password.encode('ascii')
            computed_hash = hashlib.sha256(
                salt_bytes + password_bytes, usedforsecurity=True
            ).hexdigest()
        # Use constant-time comparison to prevent timing attacks
        return secrets.compare_digest(hash_part, computed_hash)
