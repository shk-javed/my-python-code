
balance = 10000  

print("=== WELCOME TO PYTHON BANK ===")
print(f"Current Balance: ₹{balance}")


deposit = float(input("\nEnter deposit amount: ₹"))
balance += deposit
print(f"After deposit: ₹{balance}")

withdraw = float(input("Enter withdrawal amount: ₹"))
if withdraw <= balance:
    balance -= withdraw
    print(f"After withdrawal: ₹{balance}")
else:
    print("Insufficient balance!")

# Interest calculation (5% per year)
interest = balance * 0.05
print(f"\nYearly interest (5%): ₹{interest:.2f}")
print(f"Final balance after interest: ₹{balance + interest:.2f}")