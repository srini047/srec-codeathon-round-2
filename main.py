import os

from display import franchises
from contact import contacts
from product import products

final_bill = []
total = []

def clear_console():
    os.system('cls')

# Display Products
number = 0
for i in franchises:
    number += 1
    print(str(number) + " : " + i)

# Get Franchise Locatioon from User
choice = int(input('Enter the Franchise Location: '))

# Display Products in that Franchise
if (choice == 1):
    print(products[int(choice)-1])
    print(contacts[int(choice)-1])

    # Billing Logic
    for i in products[choice-1]:
        print(i)
        qty = int(input("Enter the Quantity: "))
        price = products[choice-1][i]
        final_bill.append({"Product" : i ,"Quantity" : qty, "Price" : price})
        total.append(qty * price)

elif (int(choice) == 2):
    print(products[int(choice)-1])
    print(contacts[int(choice)-1])

    # Billing Logic
    for i in products[choice-1]:
        print(i)
        qty = int(input("Enter the Quantity: "))
        price = products[choice-1][i]
        final_bill.append({"Product" : i ,"Quantity" : qty, "Price" : price})
        total.append(qty * price)

elif (int(choice) == 3):
    print(products[int(choice)-1])
    print(contacts[int(choice)-1])

    # Billing Logic
    for i in products[choice-1]:
        print(i)
        qty = int(input("Enter the Quantity: "))
        price = products[choice-1][i]
        final_bill.append({"Product" : i ,"Quantity" : qty, "Price" : price})    
        total.append(qty * price)

elif (int(choice) == 4):
    print(products[int(choice)-1])
    print(contacts[int(choice)-1])
    
    # Billing Logic
    for i in products[choice-1]:
        print(i)
        qty = int(input("Enter the Quantity: "))
        price = products[choice-1][i]
        final_bill.append({"Product" : i ,"Quantity" : qty, "Price" : price})
        total.append(qty * price)


elif (int(choice) == 5):
    print(products[int(choice)-1])
    print(contacts[int(choice)-1])

    # Billing Logic
    for i in products[choice-1]:
        print(i)
        qty = int(input("Enter the Quantity: "))
        price = products[choice-1][i]
        final_bill.append({"Product" : i ,"Quantity" : qty, "Price" : price})
        total.append(qty * price)


else:
    print("Enter a valid Franchise!!!")

# for i in final_bill:
#         print(i.keys() + print)

print(final_bill)
print("Total : " + str(sum(total)))

# Display Formatter
clear_console()
print('-'*10 + 'FINAL BILL' + '-'*10)
print("Franchise: " + franchises[choice-1])
for i in final_bill
