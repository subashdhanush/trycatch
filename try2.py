try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old.")
except ValueError:
    print("❌ Please enter a number.")
