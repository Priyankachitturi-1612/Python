catalogue = {
    "P001": {"name": "Notebook", "price": 45, "category": "Stationery"},
    "P002": {"name": "Pen", "price": 10, "category": "Stationery"},
    "P003": {"name": "Bag", "price": 800, "category": "Accessories"},
    "P004": {"name": "Bottle", "price": 250, "category": "Accessories"},
    "P005": {"name": "Headphones", "price": 1200, "category": "Electronics"},
    "P006": {"name": "Mouse", "price": 500, "category": "Electronics"},
    "P007": {"name": "Keyboard", "price": 700, "category": "Electronics"},
    "P008": {"name": "Calculator", "price": 350, "category": "Stationery"}
}

cart = {}

while True:

    print("\n===== SHOPPING CART =====")
    print("1. View Catalogue")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

  
    if choice == "1":

        print("\n===== PRODUCT CATALOGUE =====")

        for product_id, product in catalogue.items():
            print(product_id, "-", product["name"],
                  "|", product["category"],
                  "| ₹", product["price"])

   
    elif choice == "2":

        product_id = input("Enter product ID: ")

        if product_id not in catalogue:
            print("Product ID does not exist.")

        else:
            quantity = int(input("Enter quantity: "))

            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity

            print("Item added to cart.")

   
    elif choice == "3":

        product_id = input("Enter product ID: ")

        if product_id in cart:
            del cart[product_id]
            print("Item removed from cart.")
        else:
            print("Item is not in the cart.")

 
    elif choice == "4":

        if len(cart) == 0:
            print("Cart is empty.")

        else:
            print("\n===== YOUR CART =====")

            subtotal = 0

            for product_id, quantity in cart.items():

                product = catalogue[product_id]

                line_total = product["price"] * quantity
                subtotal += line_total

                print(product["name"], "x", quantity,
                      "₹", f"{line_total:.2f}")

            print("-------------------------")
            print("Subtotal ₹", f"{subtotal:.2f}")


    elif choice == "5":

        if len(cart) == 0:
            print("Cart is empty.")

        else:

            print("\n======= YOUR BILL =======")

            subtotal = 0

            categories = set()

            for product_id, quantity in cart.items():

                product = catalogue[product_id]

                line_total = product["price"] * quantity
                subtotal += line_total

                categories.add(product["category"])

                print(product["name"], "x", quantity,
                      "₹", f"{line_total:.2f}")

            if subtotal > 500:
                discount = subtotal * 10 / 100
            else:
                discount = 0

            total = subtotal - discount

            print("-------------------------")
            print("Subtotal  ₹", f"{subtotal:.2f}")
            print("Discount  ₹", f"{discount:.2f}")
            print("-------------------------")
            print("Total     ₹", f"{total:.2f}")
            print("=========================")

            print("Categories:", categories)

            cart.clear()

            print("Thank you for shopping!")


    elif choice == "6":

        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice.")
