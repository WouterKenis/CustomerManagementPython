from Customer import Customer
import sqlite3





# c.execute("""CREATE TABLE customers (
#           FirstName text,
#           LastName text,
#           Address text
#           )""")


#customers = []

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
        #customers.append(customer)

        conn = sqlite3.connect('customers.db')
        c = conn.cursor()
        params = (customer.getFirstName(), customer.getLastName(), customer.getAddress())
        c.execute("INSERT INTO customers VALUES (?, ?, ?)", params)

        conn.commit()

        conn.close()

        print("Done.")

    elif action == "del":

        conn = sqlite3.connect('customers.db')
        c = conn.cursor()
        count = c.execute("SELECT COUNT(*) from customers")

        conn.close()
        if count == 0:
            print("There are no customers in the list.")
        else:
            print("These are your current customers:")

            # for customer in customers:
            #     print(f"Customer: {customers.index(customer) + 1} - First name: {customer.getFirstName()} - Last name: {customer.getLastName()} - Address: {customer.getAddress()}")

            conn = sqlite3.connect('customers.db')
            c = conn.cursor()
            count = c.execute("SELECT * from customers")
            print(c.fetchall())
            conn.close()

            index = input("Provide the number of the customer you would to remove.")

            index = int(index)
            #if index > len(customers) or index <= 0:
            if action:
                print("Customer not found.")
            else:
                #del customers[int(index) - 1]
                print("Done.")

    elif action == "show":
        conn = sqlite3.connect('customers.db')
        c = conn.cursor()
        count = c.execute("SELECT COUNT(*) from customers")

        conn.close()
        if count == 0:
            print("There are no customers in the list.")

        else:
            # for customer in customers:
            #     print(f"First name: {customer.getFirstName()} - Last name: {customer.getLastName()} - Address: {customer.getAddress()}")

            conn = sqlite3.connect('customers.db')
            c = conn.cursor()
            count = c.execute("SELECT * from customers")
            print(c.fetchall())
            conn.close()
