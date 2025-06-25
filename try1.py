try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
    
except ValueError:
    print("❌ Please enter a valid number.")

except ZeroDivisionError:
    print("❌ Cannot divide by zero.")

except Exception as e:
    print("⚠️ Unexpected error:", e)    
 