# Practice: Arithmetic, Comparison, Logical operators

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Remainder: {num1 % num2}")

# Comparison
print(f"Is num1 greater than num2? {num1 > num2}")

# Logical example: check if number is between 1-100
n = int(input("Enter a number to check (1-100 range): "))
is_valid = n >= 1 and n <= 100
print(f"Is {n} in valid range? {is_valid}")