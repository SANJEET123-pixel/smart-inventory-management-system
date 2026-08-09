from database import connection, cursor

def sell_product():

    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity to Sell: "))

    query = "SELECT * FROM products WHERE product_id = %s"

    cursor.execute(query, (product_id,))

    product = cursor.fetchone()

    if product:

        stock = product[4]

        if quantity <= stock:

            price = product[3]

            total_amount = price * quantity

            print("Total Amount =", total_amount)

            new_stock = stock - quantity

            query = """
            UPDATE products
            SET quantity = %s
            WHERE product_id = %s
            """

            values = (new_stock, product_id)

            cursor.execute(query, values)

            connection.commit()

            query = """
            INSERT INTO sales(product_id, quantity_sold, total_amount)
            VALUES(%s, %s, %s)
                    """

            values = (product_id, quantity, total_amount)

            cursor.execute(query, values)

            connection.commit()

            print("Stock Updated Successfully")

        else:
            print("Not Enough Stock")

    else:
        print("Product Not Found")


def view_sales():

    cursor.execute("SELECT * FROM sales")

    sales = cursor.fetchall()

    if sales:

        print("\nSales List")

        for sale in sales:

            print("Sale ID :", sale[0])
            print("Product ID :", sale[1])
            print("Quantity Sold :", sale[2])
            print("Total Amount :", sale[3])
            print("Sale Date :", sale[4])
            print("----------------------------")
        
        connection.commit()

    else:

        print("No Sales Found")