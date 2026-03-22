a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(a < b < c)
print(not (a > b or b > c))
print(a <= b and b <= c)

if (not (a > b or b > c)) == (a <= b and b <= c):
    print("Expressions match")
else:
    print("Expressions do not match")




temp = int(input("Temp: "))
rain = input("Raining? (yes/no): ")
if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temp > 85:
    if rain == "yes":
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif temp >= 60:
    if rain == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif temp >= 32:
    print("It's cold — bundle up!")

else:
    print("FREEZE WARNING: Roads may be icy!")






    name = input("Name: ")
e1 = float(input("Exam 1: "))
e2 = float(input("Exam 2: "))
e3 = float(input("Exam 3: "))

avg = (e1 + e2 + e3) / 3

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

if avg >= 90:
    status = "Dean's List"
elif avg >= 70:
    status = "Good Standing"
elif avg >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

print(name)
print("Average:", round(avg, 2))
print("Grade:", grade)
print("Status:", status)
