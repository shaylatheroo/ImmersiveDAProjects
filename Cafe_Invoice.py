'''
Ever wonder what actually happens during lunch? There's actually a Behind-The-Door Break Room Cafe where all the instructors show off what they brought in for lunch. Create an invoice store that would take orders from our makeshift Behind-The-Door Break Room Cafe.

Requirements:

Create a function for the invoice class that will contain the invoice items and a date and customer name, address and account number
Create a function for items with the following properties:
Name
Price
Quantity
Taxable (TRUE or FALSE)
Implement a loop functionality that allows users to enter in as many items as they want until the user enters "no" to stop.
Prompt the user for their state. Based on the state they enter, charge them the following sales tax rates:

MD - 6.00%
DC - 5.30%
VA - 5.75%
Other states - 5.00%
Note: Only calculate the sales tax if TAXABLE is set to TRUE for that item.

Calculate the cost for each item (price * quantity)
Calculate the sub-total (the sum of each item's cost)
Calculate the sales tax (only if taxable is TRUE for the item)
Calculate the total amount (subtotal + sales tax)
Format all decimals to two decimal places. (**see this website to format numbers in Python (Links to an external site.))

Expected Output


Enter your name: Dave Wolf
Enter your address: 123 Only street, Only MD
Enter the date: 12/09/18
Enter your account number: 123

Enter item name: salad
Price: 8.50
Quantity: 6
Taxable (true or false): true
Enter your sate: DC
Add another item: y

Enter item name: burger
Price: 9.95
Quantity: 5
Taxable (true or false): false
Add another item: y

Enter item name: cola
Price: 3.45
Quantity: 8
Taxable (true or false): true
Enter your sate: DC
Add another item: y

Enter item name: honeybun
Price: 12.75
Quantity: 5
Taxable (true or false): true
Enter your sate: DC
Add another item: n

-----------------------------------------------------
Customer name: Dave Wolf
Address: 123 Only street, Only MD
Date: 12/09/18
Account number: 123
-----------------------------------------------------

Item Name     Quantity       Price          Cost           Taxable        
=========================================================================
salad          6              8.50           51.00          true           
burger         5              9.95           49.75          false          
cola           8              3.45           27.60          true           
honeybun       5              12.75          63.75          true           

Subtotal: $192.10
Sales Tax: $7.54

-------------------------------------------------------------------------
Total: $199.64
'''

def salesTaxCalc(itemState):
    if itemState.upper()=='MD':
        taxRate = 0.06
    elif itemState.upper()=='DC':
        taxRate = 0.053
    elif itemState.upper()=='VA':
        taxRate = 0.0575
    else:
        taxRate = 0.05
    return taxRate

customerName = input("Enter your name: ")
customerAddress = input("Enter your address: ")
purchaseDate = input("Enter the date: ")
customerAccount = input("Enter your account number: ")

itemContainer = {}
subtotal = 0
salesTax = 0
collectItems = True
while collectItems==True:
    itemName = input("Enter item name: ")
    itemPrice = input("Price: ")
    itemQuantity = input("Quantity: ") 
    itemSubtotal = float(itemPrice) * int(itemQuantity)
    itemTaxable = input("Taxable (true or false): ")
    itemState = input("Enter your state: ")
    itemContainer[itemName] = [itemQuantity, itemPrice, itemSubtotal, itemTaxable]
    
    subtotal += itemSubtotal
    if itemTaxable.lower()=='true':
        salesTax += salesTaxCalc(itemState) * itemSubtotal
    
    exitItem = input("Add another item (yes or no): ")
    if exitItem.lower()=='no':
        collectItems = False

totalPaid = subtotal + salesTax

print("-----------------------------------------------------")
print("Customer name: " + customerName)
print("Address: " + customerAddress)
print("Date: " + purchaseDate)
print("Account number: " + customerAccount)
print("-----------------------------------------------------")
print('{:<16s}{:<16s}{:<16s}{:<16s}{:<9s}'.format('Item Name','Quantity','Price','Cost','Taxable'))
print("=========================================================================")

for x, y in itemContainer.items():
    print('{:<16s}{:<16s}{:<16s}{:<16s}{:<9s}'.format(x,str(int(y[0])),"$"+"{:.2f}".format(float(y[1])),"$"+"{:.2f}".format(float(y[2])),y[3]))

print("Subtotal: $"+"{:.2f}".format(subtotal))
print("Sales Tax: $"+"{:.2f}".format(salesTax))
print("-------------------------------------------------------------------------")
print("Total: $"+"{:.2f}".format(totalPaid))