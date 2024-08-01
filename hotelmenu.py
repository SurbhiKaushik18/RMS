menu={
    'pizza':40,
    'pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}
print("Welcome to PYTHON Restrauant.")

print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80 ")

order_total = 0

item1=input("Enter the name of item you want to order = ")
if item in menu:
    order_total+=menu[item1]
    print("Your item {item1} has ben added to your order")
else:
    print("Ordered item {item1} is not available yet")

another_order=input("Do you want to add another item? (Yes/No)")

if another_order==Yes:
    print("Enter the name of item you want to order = ")
    
