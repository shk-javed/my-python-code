import random
number = random.randint(1, 10)
attempts = 3

for i in range(attempts):
    guess = int(input(f"Guess {i+1}/{attempts}: "))
    if guess == number:
        print("🎉 Correct!")
        break
    print("❌ Wrong! Try again" if i < attempts-1 else f"😢 The number was {number}")