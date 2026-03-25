age = int(input("Enter age: "))
showtime = (input ("Enter showtime(matinee/evening): "))
member = input("Rewards member? (yes/no): ")

showtime_lower = showtime.lower()
member_lower = member.lower()

if age < 12:
    base_price = 6.00
if age >= 65:
    base_price = 7.00
if age => 12 and age <= 17:
    base_price = 9.00
else:
    base_price = 13.00

if showtime_lower != "matinee" and showtime_lower != "evening":
    print("Invalid showtime.")
else:
    price= base_price
    matinee_discount = 0
    rewards_discount = 0

if showtime_lower == "matinee":
    matinee_discount = 2.00
    price = price - matinee_discount

if member_lower == "yes":
    rewards_discount = price * 0.15
    price = price - rewards_discount

print("--- Movie Ticket ---")
print(f"Age: {age}")
print(f"Showtime: {showtime.capitalize()}") 
print(f"Rewards member: {member.capitalize()}")
print(f"Base price: ${base_price:2f}")

if matinee_discount > 0:
     print(f"Matinee discount: -${matinee_discount:.2f}")
if rewards_discount > 0:
    print(f"Rewards discount: -${rewards_discount:.2f}")
print(f"Final price: ${price:.2f}")
print("--------------------")