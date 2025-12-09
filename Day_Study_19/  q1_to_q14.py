

people = {
    "Munir": 25,
    "Amit": 30,
    "Priya": 28,
}

print(people)

for key in people:
    print(key)
    
    
for value in people.values():
    print(value)
    
people["Raj"] = 22
print(people)

people.update({"Amit": 31})
print(people)


del people["Priya"]
print(people)

# Amit ki age find karo
if "Amit" in people:
    print(f"Found: Name: Amit | Age: {people['Amit']}")
    
    
    
    
# Set of 5 numbers
numbers = {10, 20, 30, 40, 50}
print(numbers)
print(type(numbers))



# Step 1: Create a set
my_set = {10, 20, 30, 40, 50}
print("Original set:", my_set)

# Step 2: Add a number using add() method
my_set.add(60)
print("After adding 60:", my_set)

# Step 3: Add another number
my_set.add(70)
print("After adding 70:", my_set)


set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print(f"Set A: {set_A}")
print(f"Set B: {set_B}")

union_result = set_A.union(set_B)
print(f"Union (A.union(B)): {union_result}")
