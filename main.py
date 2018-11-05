from Customer import Customer

customers = []

print("Welcome to your CustomerManagement package.")
while True:
    action = input("Input 'add' to add data, 'del' to delete data or 'show' to show your customer list.")

    if action not in ["add", "del", "show"]:
        print("Invalid input.")
        continue

    elif action == "add":
        firstName = input("Please provide the first name of the customer")
        lastName = input("Please provide the last name of the customer")
        address = input("Please provide the address of the customer")

        customer = Customer(firstName, lastName)
        customer.setAddress(address)
        customers.append(customer)

    elif action == "del":

        if len(customers) == 0:
            print("There are no customers in the list.")
        else:
            print("These are your current customers:")
            for customer in customers:
                print(f"Customer: {customers.index(customer) + 1} - customerFirst name: {customer.getFirstName()} - Last name: {customer.getLastName()} - Address: {customer.getAddress()}")

            index = input("Provide the number of the customer you would to remove.")

            index = int(index)
            if index - 1 > len(customers) or index <= 0:
                print("Customer not found.")
            else:
                del customers[int(index) - 1]
                print("Done.")

    elif action == "show":
        if len(customers) == 0:
            print("There are no customers in the list.")

        else:
            for customer in customers:
                print(f"First name: {customer.getFirstName()} - Last name: {customer.getLastName()} - Address: {customer.getAddress()}")