class Customer:

    address = "";


    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


    def getAddress(self):
        return self.address

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def setAddress(self, address):
        self.address = address

