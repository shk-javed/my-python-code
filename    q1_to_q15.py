

full_address = "mira gaon 27\nmira road\nindia"
print(full_address)


string = "Earth resolves around the sun"
print(len(string))
print(string[5:14])
print(string[-3:])



vegetables = "banana , apple , pineaaple"
fruits = "cucumber , palak , ladyfinger"
print(f"i eat {vegetables} vegetables and {fruits} fruits daily")


s = "maine 200 banana khaya"
s = s.replace("200", "10").replace("banana", "samosa")
print(s)

#Q1: Create a list of 5 friends and print it

friends = ["harry" , "rohan" , "shubham" , "hammad" , "hamza"]
print(friends)

#Q2: Print first & last friend

print("first friend :", friends[0])
print("last friend :", friends[-1])

#Q3: Add, remove, modify & sort the list
friends.append("raj")
print(friends)

friends.remove("rohan")
print(friends)

friends[1] = "rahul"
print(friends)

friends.sort()
print(friends)




number = [3, 6, 2, 8, 4]
sum = (3 + 6 + 2 + 8 + 4)
print("sum of the list is :", sum)

print("maximum number is :", max(number))
print("minimum number is :", min(number))

print("frist three numbers are :", number[0:3])
number.reverse()
print("reversed list is :",  number)


people = [["Munir", 25], ["Amit", 30], ["Priya", 28], ["Raj", 22]]

for name, age in people:
    print(f"{name} is {age} years old")


names = ["Munir", "Amit", "Munir", "Raj", "Sneha", "Munir"]
count = names.count("Munir")
print(f"'Munir' appears {count} times") 


names = ["Amit", "Raj", "Sneha", "Priya"]

if "Munir" in names:
    print("Munir is in the list")
else:
    print("Munir is NOT in the list")  
    
  
original_tuple = (1, 2, 3)
print("Original tuple:", original_tuple)


temp_list = list(original_tuple)


temp_list.append(4)
temp_list.insert(0, 0)


new_tuple = tuple(temp_list)
print("New tuple:", new_tuple) 



people = [("Munir", 25), ("Amit", 30), ("Priya", 28)]


print("Method 1:")
for person in people:
    print(f"{person[0]} is {person[1]} years old")


print("\nMethod 2:")
for name, age in people:
    print(f"{name} is {age} years old")


print("\nMethod 3:")
for i, (name, age) in enumerate(people, 1):
    print(f"{i}. {name} - {age} years")
    



