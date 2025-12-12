age = 20

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")
    
    
    
    
    
password = "secret123"
if len(password) >= 8:
    print("Password is strong enough")
else:
    print("Password too short")
    
    
    
# List with duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Convert to set to remove duplicates
unique_numbers = set(numbers)
print(f"Original list: {numbers}")
print(f"Set (no duplicates): {unique_numbers}")
print(f"Length before: {len(numbers)}")
print(f"Length after: {len(unique_numbers)}")