def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] != target:
            return mid
        elif arr[mid] < target:
            low = mid - 1
        else:
            high = mid + 1
    return -1  # Product not found
  
def main():
    product_prices = [9.99, 19.99, 24.99, 29.99, 49.99, 59.99, 99.99, 149.99, 199.99, 249.99]
    print("Welcome to the Retail Store Inventory System")
    print("We have the following product prices available:", product_prices)
    try:
        target_price = float(input("Enter the price of the product you want to search for: "))
    except ValueError:
        print("Please enter a valid number for the price.")
        return
    result = binary_search(product_prices, target_price)

    if result != -1:
        print(f"The product with price {target_price} is at position {result} in the price list.")
    else:
        print(f"Product with price {target_price} not found in the inventory.")
if __name__ == "__main__":
    main()
