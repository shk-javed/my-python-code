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





if (10>5>2):
    print("Chained comparison is True")
else:
    print("Chained comparison is False")
    
    
    
    
# Age check for driving license
age = 25
if 18 <= age <= 65:
    print("Eligible for driving license")

# Temperature range check  
temperature = 22.5
if 20 <= temperature <= 25:
    print("Comfortable room temperature")

# Score grading
marks = 85
if 90 <= marks <= 100:
    grade = "A+"
elif 80 <= marks < 90:
    grade = "A"  # ✅ This will execute
    
    
    
    
