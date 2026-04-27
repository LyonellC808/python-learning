#RGB color tuple
rgb_color = (255, 128, 0)

print(f"Red: {rgb_color[0]}")
print(f"Green: {rgb_color[1]}")
print(f"Blue: {rgb_color[2]}")

palette = []
palette.append(rgb_color)

print(f"Palette: {palette}")




# Create student tuples (name, grade, age)
s1 = ("Lyonell", 95, 19)
s2 = ("Alice", 88, 18)
s3 = ("Bob", 72, 20)

classroom = [s1, s2, s3]

print(f"Second student name: {classroom[1][0]}")

name, grade, age = classroom[0]

print(f"Student {name} is {age} years old and has a grade of {grade}.")






# Create original student tuple (name, [exams], final_grade)
student = ("Lyonell", [85, 90, 88], 0)

# Add fourth exam score to the list inside the tuple
student[1].append(92)

# Calculate new average
avg = sum(student[1]) / len(student[1])

# Create new tuple with updated final grade (since tuples are immutable)
updated_student = (student[0], student[1], avg)

# Print both tuples
print(f"Original (with modified list): {student}")
print(f"Updated Student Record: {updated_student}")







def boost_grades(grades, bonus):
    for i in range(len(grades)):
        grades[i] += bonus

hw_grades = [85, 70, 90]
today_date = (4, 27, 2026)

boost_grades(hw_grades, 5)
print(f"Boosted Grades: {hw_grades}")

# Comment: 
# Using a LIST for grades because they are dynamic and need to be modified.
# Using a TUPLE for the date because a date is a fixed point in time and shouldnt be
# accidentally changed







def find_range(*args):
    return (min(args), max(args))

# Test with 3 and 7 numbers
print(f"Range 1: {find_range(10, 5, 20)}")
print(f"Range 2: {find_range(1, 5, 100, 2, 50, -5, 10)}")

# Unpack list using * operator
test_scores = [78, 92, 85, 88, 91]
print(f"Test Scores Range: {find_range(*test_scores)}")








def calculate_statistics(*args):
    count = len(args)
    total = sum(args)
    avg = total / count if count > 0 else 0
    return (count, total, avg)

def update_student_records(records, bonus):
    # Returns a NEW list with new tuples
    return [(name, grade + bonus) for name, grade in records]

# Demonstration
classroom = [("Lyonell", 90), ("Alice", 85)]
updated = update_student_records(classroom, 5)
all_grades = [s[1] for s in updated]

stats = calculate_statistics(*all_grades)
print(f"Updated Records: {updated}")
print(f"Stats (Count, Sum, Avg): {stats}")






# Create nested list
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print center number
print(f"Center number: {grid[1][1]}")

# Print each row on a separate line
print("Grid Display:")
for row in grid:
    print(row)









scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

# Passing grades (60+)
passing_grades = [s for s in scores if s >= 60]

# Convert to letter grades
letter_grades = [
    'A' if s >= 90 else 'B' if s >= 80 else 'C' if s >= 70 else 'D' 
    for s in passing_grades
]

print(f"Passing: {passing_grades}")
print(f"Letters: {letter_grades}")










# 1. 4x4 multiplication table
table = [[i * j for j in range(1, 5)] for i in range(1, 5)]
print("Multiplication Table:")
for row in table:
    print(row)

# 2. Sum diagonal function
def sum_diagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

print(f"Diagonal Sum: {sum_diagonal(table)}")

# 3. Generator for even numbers
evens_gen = (num for row in table for num in row if num % 2 == 0)

print("First 5 even numbers from table:")
for _ in range(5):
    print(next(evens_gen), end=" ")









