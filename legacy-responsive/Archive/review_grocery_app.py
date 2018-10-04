
# an array to store shopping list
shopping_lists = []

class GroceryItem:
    def __init__(self,name,price,quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def updatePrice(self,new_price):
        self.price = new_price

    def __repr__(self):
        return f"Name = {self.name}, Price = {self.price}, Quantity = {self.quantity}"

another_grocery_item = GroceryItem("cookies",10,23)
another_grocery_item.updatePrice(100)
print(another_grocery_item.price)




class ShoppingList:
    def __init__(self,name):
        self.name = name
        self.address = ""
        self.store_number = ""
        self.shopping_list_card_number = ""
        self.items = []

# ask for shopping list
while True:

    shopping_list_name = input("Enter Shopping List Name or q to quit: ")
    shopping_list_address = input("Enter Shopping List Address ")
    shopping_list_store_number = input("Enter Shopping List Store Number ")

    if(shopping_list_name == "q"):
        break

    shopping_list = ShoppingList(shopping_list_name)
    shopping_list.address = shopping_list_address
    shopping_list.store_number = shopping_list_store_number

    # insert shopping list into the array
    #shopping_list_as_string = "{0} {1} {2}".format(shopping_list.name,shopping.address,shopping_list.store_number)

    shopping_lists.append(shopping_list)

    shopping_list.name = "Albertsons"

    # ask for grocery item
    while True:

        # ask for grocery items
        grocery_item_name = input("Enter Item Name: ")

        if(grocery_item_name == "q"):
            break

        # create a grocery item object
        grocery_item = GroceryItem(grocery_item_name,10)
        print(grocery_item)
        shopping_list.items.append(grocery_item)


#print(shopping_lists)
#print(len(shopping_lists))
