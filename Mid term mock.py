temp = float(input("Enter temperature: "))
scale = input("Enter scale (C/F): ").lower()

if scale == "c":
    f = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {f:.1f}°F")

elif scale == "f":
    c = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {c:.1f}°C")

else:
    print("Invalid scale.")





text = input("Enter a sentence: ")

upper = 0
lower = 0
digits = 0
spaces = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Total characters:", len(text))
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Spaces:", spaces)
print("Reversed:", text[::-1])


numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]

print("Original:", numbers)

print("First:", numbers[0], "Last:", numbers[-1])

print("Middle 4:", numbers[3:7])

numbers.append(99)
print("After append:", numbers)

numbers.insert(0, 0)
print("After insert:", numbers)

numbers.remove(42)
print("After remove:", numbers)

removed = numbers.pop()
print("Popped:", removed)

print(23 in numbers)

print("Index of 16:", numbers.index(16))

print("Final:", numbers)
print("Length:", len(numbers))






gpa = float(input("Enter GPA: "))
credits = int(input("Enter credits: "))
prereq = input("Prerequisite completed? (yes/no): ").lower()

if gpa >= 3.5 and credits >= 60 and prereq == "yes":
    status = "Approved: You meet all requirements."

elif gpa >= 3.5 and credits >= 60:
    status = "Conditionally approved: Complete the prerequisite first."

elif gpa >= 3.0 and credits >= 45:
    status = "Waitlisted: You may be admitted if space is available."

elif gpa >= 2.0:
    status = "Not eligible yet: Raise your GPA or earn more credits."

else:
    status = "Denied: GPA is below minimum threshold."

print(status)

print("--- Registration Summary ---")
print(f"GPA: {gpa:.2f}")
print("Credits:", credits)
print("Prerequisite:", prereq.capitalize())
print("Status:", status)
print("----------------------------")







names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]

# Task 1
print("=== CLASS ROSTER ===")
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {scores[i]}")
print("====================")

# Task 2 (find max/min manually)
max_score = scores[0]
min_score = scores[0]
max_name = names[0]
min_name = names[0]

for i in range(len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]
        max_name = names[i]
    if scores[i] < min_score:
        min_score = scores[i]
        min_name = names[i]

print("Highest:", max_name, "-", max_score)
print("Lowest:", min_name, "-", min_score)

# Task 3 (average)
total = 0
for s in scores:
    total += s
avg = total / len(scores)
print("Average:", round(avg, 2))

# Task 4 (grades)
print("--- Grade Report ---")
for i in range(len(scores)):
    s = scores[i]
    if s >= 90:
        g = "A"
    elif s >= 80:
        g = "B"
    elif s >= 70:
        g = "C"
    elif s >= 60:
        g = "D"
    else:
        g = "F"
    print(names[i] + ":", s, "->", g)

# Task 5
names.append("Frank")
scores.append(77)

index = names.index("Diana")
names.pop(index)
scores.pop(index)

print("New length:", len(names))

