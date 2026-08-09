from database import connection, cursor

def add_product():
    print("\n===== Add Product =====")
    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    query = """
    INSERT INTO products
    (product_name, category, price, quantity)
    VALUES (%s, %s, %s, %s)
    """

    values = (product_name, category, price, quantity)

    cursor.execute(query, values)

    connection.commit()
    print("\nProduct Added Successfully!")


from database import connection, cursor


def view_products():

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    if products:

        print("\nProduct List")

        for product in products:
            print("Product ID :", product[0])
            print("Product Name :", product[1])
            print("Category :", product[2])
            print("Price :", product[3])
            print("Quantity :", product[4])
            print("-------------------------")

    else:
        print("No products found.")


def search_product():

    product_id = int(input("Enter Product ID: "))

    query = "SELECT * FROM products WHERE product_id = %s"

    cursor.execute(query, (product_id,))

    product = cursor.fetchone()

    if product:

        print("\nProduct Found")
        print("Product ID :", product[0])
        print("Product Name :", product[1])
        print("Category :", product[2])
        print("Price :", product[3])
        print("Quantity :", product[4])

    else:
        print("Product not found.")


def update_product():

    product_id = int(input("Enter Product ID: "))

    new_product_id = int(input("Enter New Product ID: "))
    new_price = float(input("Enter New Price: "))
    new_quantity = int(input("Enter New Quantity: "))


    query = """
    UPDATE products
    SET product_id = %s, price = %s, quantity = %s
    WHERE product_id = %s
    """

    values = (new_product_id, new_price, new_quantity, product_id)

    cursor.execute(query, values)

    connection.commit()

    print("Product Updated Successfully!")


def delete_product():

    product_id = int(input("Enter Product ID: "))

    query = "DELETE FROM products WHERE product_id = %s"

    values = (product_id,)

    cursor.execute(query, values)

    connection.commit()

    print("Product Deleted Successfully!")