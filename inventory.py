
#========Define "Shoe" class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return(int(self.cost))

    def get_quantity(self):
        return(int(self.quantity))

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============
# Define function to read the shoe data from the inventory file into the shoe list
# Use try ... except logic to deal with possibility of file not being found
def read_shoes_data():
    try:
        with open("inventory.txt","r") as inventory:
            for index,line in enumerate(inventory):
                if index > 0:
                    line_list = line.split(",")
                    item = Shoe(line_list[0],line_list[1],line_list[2],line_list[3],line_list[4].strip("\n"))
                    shoe_list.append(item)
    except FileNotFoundError:
        print("File inventory.txt not found.")

# Define function for manually adding shoe data
# Use try ... except logic to ensure that quantity and cost variables are convertible to numbers
# This will ensure later functions don't break
def capture_shoes():
    country = input("Enter the shoe's country:\n")
    code = input("Enter the shoes code:\n")
    product = input("Enter the product name for the shoe:\n")
    cost = input("Enter the cost of the shoe:\n")
    quantity = input("Enter th quantity of the shoe:\n")
    try:
        cost_check = float(cost)
        quantity_check = float(quantity)
        new_shoe = Shoe(country,code,product,cost,quantity)
        shoe_list.append(new_shoe)
    except ValueError:
        print("Your entries for cost and quantity must be numbers. Please try again.")

# Define funciton to print shoe info
def view_all():
    for shoe in shoe_list:
        print(shoe.__str__())

# Define function to find shoe with least stock and offer option to restock
def re_stock():
    # Initiate quantities list
    quantities = []
    for shoe in shoe_list:
        quantities.append(shoe.get_quantity())
    least_index = quantities.index(min(quantities))
    least_shoe = shoe_list[least_index]
    choice = input(f"""Shoe {least_shoe.product} has the least quantity in stock.
    Currently we only have {least_shoe.quantity} in stock.
    Would you like to add another {least_shoe.quantity}? Please enter \"yes\" or \"no\"""")
    if choice.lower() == "yes":
        least_shoe.quantity = str(least_shoe.get_quantity()*2)
        shoe_list[least_index] = least_shoe

# Define function to search shoe list by code
def seach_shoe():
    seach_code = input("Please enter the code of a shoe to search for")
    # Initiate codes list
    codes = []
    for shoe in shoe_list:
        codes.append(shoe.code)
    try:
        seach_index = codes.index(seach_code)
        print("The details for the shoe you searched for are below:")
        print(shoe_list[seach_index].__str__())
    except ValueError:
        print("The code you enterd does not match any shoe in the stocklist")

# Define function which lists the value of each shoe's stock
def value_per_item():
    print("The value of each shoe in stock is as follows:")
    for shoe in shoe_list:
        print(f"{shoe.product}:     {shoe.get_quantity() * shoe.get_cost()}")

# Define a function to advertise the shoe with the most quantity of stock
def highest_qty():
    # Initiate quantities list
    quantities = []
    for shoe in shoe_list:
        quantities.append(shoe.get_quantity())
    most_index = quantities.index(max(quantities))
    most_shoe = shoe_list[most_index]
    print(f"""The details of the shoe with the most stock are as follows: 
    {most_shoe.__str__()}
    This shoe is for SALE!
    """)

#==========Main Menu=============
# List program functionality to user
while True:
    choice = input("""
Please select an option from those below:
rs      --      read shoes from the inventory.txt file
cs      --      capture info about a new shoe in the stocklist on file
va      --      view the details of all shoes in stock
re      --      identify the shoe with least stock and restock
ss      --      search the stocklist by code
vv      --      view the value of stock for each item
hq      --      identify the shoe with the most stock to be advertised through sale
e       --      exit the program
""").lower()
    if choice == "rs":
        read_shoes_data()
    elif choice == "cs":
        capture_shoes()
    elif choice == "va":
        view_all()
    elif choice =="re":
        re_stock()
    elif choice == "ss":
        seach_shoe()
    elif choice =="vv":
        value_per_item()
    elif choice == "hq":
        highest_qty()
    elif choice == "e":
        break
    else:
        print("You have not entered a valid input. Please try again.") 