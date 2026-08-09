from inventory import add_product, view_products, search_product, update_product, delete_product
from sales import sell_product, view_sales

def menu():

    while True:

        print("\n===================================")
        print(" SMART INVENTORY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Sell Product")
        print("7. View Sales")
        print("8. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            sell_product()

        elif choice == "7":
            view_sales()

        elif choice == "8":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


menu()