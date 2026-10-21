# NESTED DICTIONARY
# WITH PRODUCT NAME PRODUCT QTY PRODUCT PRICE AND SALESMAN NAME 
# WITHOUT DIFF DICTIONARY NAME


products = {
    101: {
        "Product Name": "Laptop",
        "Product Qty": 2,
        "Product Price": 50000,
        "Salesman Name": "Rahul"
    },
    102: {
        "Product Name": "Mouse",
        "Product Qty": 5,
        "Product Price": 500,
        "Salesman Name": "Amit"
    },
      103: {
        "Product Name": "Keyboard",
        "Product Qty": 3,
        "Product Price": 1200,
        "Salesman Name": "Neha"
    },
    104: {
        "Product Name": "Monitor",
        "Product Qty": 4,
        "Product Price": 15000,
        "Salesman Name": "Raj"
    }
}


def add_product():
    pid = int(input("Enter Product ID: "))

    if pid in products:
        print("Product ID already exists. Cannot add product.")
        return

    product_name = input("Enter Product Name: ")
    product_qty = int(input("Enter Product Quantity: "))
    product_price = float(input("Enter Product Price: "))
    salesman_name = input("Enter Salesman Name: ")

    products[pid] = {
        "Product Name": product_name,
        "Product Qty": product_qty,
        "Product Price": product_price,
        "Salesman Name": salesman_name
    }

    print("Product Added Successfully!")


while True:

    print("\n===== MENU =====")
    print("0. Exit")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Display Products")
    print("6. Sorting")
    print("7. Minimum Sales")
    print("8. Maximum Sales")
    print("9. Top 3 Records - High Sales")
    print("10. Last 3 Records - Least Sales")

    choice = int(input("Enter your choice: "))

    match choice:

        case 0:
            print("Program Terminated")
            break

        case 1:
            add_product()

        case 2:
            print("Display Product")

        case 6:
            sorted_products = sorted(
                products.items(),
                key=lambda x: x[1]["Product Price"]
            )

            print("\nProducts Sorted by Price:")
            for pid, details in sorted_products:
                print(pid, details)

        case 7:
            minimum = min(
                products.items(),
                key=lambda x: x[1]["Product Price"]
            )

            print("\nMinimum Sale:")
            print(minimum)

        case 8:
            maximum = max(
                products.items(),
                key=lambda x: x[1]["Product Price"]
            )

            print("\nMaximum Sale:")
            print(maximum)

        case _:
            print("Invalid Choice")