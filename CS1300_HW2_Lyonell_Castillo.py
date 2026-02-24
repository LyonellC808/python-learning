# Run this code and explain what you observe:
a = 256
b = 256
print("a =", a, "id(a) =", id(a))
print("b =", b, "id(b) =", id(b))
print("Same object?", id(a) == id(b))

first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ").title()

current_year = 2026
age = current_year - birth_year

border = "=" * 36

print(border)
print("USER PROFILE CARD")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print("-" * 36)
print("Thank you for creating your profile!")
print(border)