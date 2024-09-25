from binary_search import binary_search

# Bug reproduction script to test the binary search logic
product_prices = [9.99, 19.99, 24.99, 29.99, 49.99, 59.99, 99.99, 149.99, 199.99, 249.99]
target_price = 24.99
result = binary_search(product_prices, target_price)
if result != -1:
    print(f"The product with price {target_price} is at position {result} in the price list.")
else:
    print(f"Product with price {target_price} not found in the inventory.")
