"""
The inventory store scenario project utilizes a dictionary-based approach to develop a robust system for managing and tracking inventory in a retail store. 
It includes functionalities for adding, updating, removing, and viewing inventory items, as well as generating reports on stock levels and sales performance.
"""

#Type your code here
inventory = {}

ProductNO1 = "Iphone"
ProductNO1_quantity = 10
ProductNO1_price = 70000
ProductNO1_realiseYear = 2022
ProductNO2 = "sumsang"
ProductNO2_quantity = 13
ProductNO2_price = 84000
ProductNO2_realiseYear = 2021

inventory["ProductNO1"]=ProductNO1
inventory["ProductNO1_quantity"]=ProductNO1_quantity
inventory["ProductNO1_price"]=ProductNO1_price
inventory["ProductNO1_realiseYear"]=ProductNO1_realiseYear
inventory["ProductNO2"]=ProductNO2
inventory["ProductNO2_quantity"]=ProductNO2_quantity
inventory["ProductNO2_price"]=ProductNO2_price
inventory["ProductNO2_realiseYear"]=ProductNO2_realiseYear



print("ProductNO1" in inventory)
print("ProductNO2" in inventory)
print("ProductNO1_realiseYear" in inventory)
print("ProductNO2_realiseYear" in inventory)

del inventory ["ProductNO1_realiseYear"]
del inventory ["ProductNO2_realiseYear"]

print(inventory)
