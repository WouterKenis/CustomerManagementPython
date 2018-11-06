from Customer import Customer
import sqlite3


conn = sqlite3.connect('customers.db')
c = conn.cursor()
c.execute("DROP TABLE customers")
c.execute("""CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
          FirstName text,
          LastName text,
          Address text
          )""")

conn.commit()

conn.close()

def refreshDatabase():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()

    c.execute("SELECT * from customers")

    data = c.fetchall()

    for row in data:
        print(f"Customer: {row[0]} - First name: {row[1]} - Last name: {row[2]} - Address: {row[3]}")

    conn.close()


def printDatabase():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()

    c.execute("SELECT * from customers")

    data = c.fetchall()

    for row in data:
        print(f"Customer: {row[0]} - First name: {row[1]} - Last name: {row[2]} - Address: {row[3]}")

    conn.close()

def getRowCount():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()

    c.execute("SELECT * from customers")

    data = c.fetchall()

    count = 0;
    for row in data:
        count = count + 1

    conn.close()

    return count

print("Welcome to your CustomerManagement package.")
while True:
    action = input("Input 'add' to add data, 'del' to delete data or 'show' to show your customer list.\n")

    if action not in ["add", "del", "show"]:
        print("Invalid input.")
        continue

    elif action == "add":
        firstName = input("Please provide the first name of the customer.\n")
        lastName = input("Please provide the last name of the customer.\n")
        address = input("Please provide the address of the customer.\n")

        customer = Customer(firstName, lastName)
        customer.setAddress(address)

        conn = sqlite3.connect('customers.db')
        c = conn.cursor()
        params = (customer.getFirstName(), customer.getLastName(), customer.getAddress())
        c.execute("INSERT INTO customers VALUES (NULL, ?, ?, ?)", params)

        conn.commit()
        conn.close()

        print("Done.")

    elif action == "del":

        count = getRowCount()
        if count == 0:
            print("There are no customers in the list.")
        else:
            print("These are your current customers:")

            printDatabase()

            index = input("Provide the number of the customer you would to remove.")
            index = int(index)

            conn = sqlite3.connect('customers.db')
            c = conn.cursor()
            c.execute(f"DELETE from customers where id = {index}")

            if c.rowcount == 0:
                print("Customer not found")

            else:
                print("Done.")
                conn.commit()
                #refreshDataBase()

            conn.close()

    elif action == "show":

        conn = sqlite3.connect('customers.db')
        c = conn.cursor()
        count = c.arraysize
        print(count)
        conn.close()

        if count == 0:
            print("There are no customers in the list.")
        else:
            printDatabase()

