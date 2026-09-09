#Define the menu of restaurant
menu = {
    'Pizza':50,
    'Pasta':40,
    'Burger':60,
    'Salad':30,
    'coffee':20,

}

#Greet
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs50\nPasta: Rs40\nBurger: Rs60\nSalad:Rs 30\ncoffee\n:20")

order_total = 0
#20 + 30 =60

item_1=input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1] #0 +40
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Orderd item {item_1} is not avaiabale yet!")

    another_order =input("Do you want to add another item? (Yes/No)")
    if another_order == "Yes":
        item_2=("Enter the name of second item =")
        if item_2 in menu:
            order_total +=[item_2]
            print(f"Item{item_2} has been added to order")
        else:
            print(f"Order item {item_2} is not avaialable!")

print(f"The total amount of items to pay is {order_total}")
            