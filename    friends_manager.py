friends = []

while True:
    print("\n1. Add Friend")
    print("2. Remove Friend")
    print("3. Show Friends")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter friend name: ")
        friends.append(name)
        print(f"{name} added!")

    elif choice == "2":
        name = input("Enter name to remove: ")
        if name in friends:
            friends.remove(name)
            print(f"{name} removed!")
        else:
            print("Friend not found")

    elif choice == "3":
        print("\nCurrent Friends List:")
        print(friends)

    elif choice == "4":
        print("Exiting…")
        break

    else:
        print("Invalid choice")

