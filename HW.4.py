age = int(input("Age: "))
m = input("Matinee? yes/no: ")

if age < 0:
    print("Invalid age")

elif age < 13:
    if m == "yes":
        price = 6
    else:
        price = 8
    print("Child")
    print(price)

elif age <= 17:
    if m == "yes":
        price = 7
    else:
        price = 10
    print("Teen")
    print(price)

elif age <= 64:
    if m == "yes":
        price = 8
    else:
        price = 13
    print("Adult")
    print(price)

else:
    if m == "yes":
        price = 6
    else:
        price = 7
    print("Senior")
    print(price)







errors = []

sid = input("ID: ")
name = input("Name: ")
age = input("Age: ")
major = input("Major: ")

if len(sid) != 8:
    errors.append("ID must be 8 chars")

if sid == "" or not sid[0].isalpha():
    errors.append("ID must start with letter")

if len(sid) == 8 and not sid[1:].isdigit():
    errors.append("Last 7 must be digits")

if name.strip() == "":
    errors.append("Name empty")

try:
    age = int(age)
    if age < 16 or age > 99:
        errors.append("Age 16-99 only")
except:
    errors.append("Age not number")

if major.upper() not in ["CS","IT","CE","DS"]:
    errors.append("Bad major")

if len(errors) == 0:
    print("Good profile")
else:
    for e in errors:
        print(e)








print("1 Coffee")
print("2 Sandwich")
print("3 Salad")
print("4 Combo")

c = input("Choice: ")
price = 0

if c == "1":
    price = 3.5
    s = input("size: ")
    if s == "medium":
        price = 4.5
    elif s == "large":
        price = 5.5

elif c == "2":
    price = 6
    ch = input("cheese yes/no: ")
    if ch == "yes":
        price += 0.75

elif c == "3":
    price = 5.5
    d = input("dressing: ")

elif c == "4":
    price = 8
    s = input("size: ")
    if s == "medium":
        price += 1
    elif s == "large":
        price += 2
    ch = input("cheese yes/no: ")
    if ch == "yes":
        price += 0.75

name = input("name: ")

q = int(input("qty: "))

total = price * q
tax = total * 0.07

print("Total:", total)
print("Final:", total + tax)