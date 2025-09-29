students = list(range(1, 31))

for _ in range(28):
    number = int(input())
    if number in students:
        students.remove(number)

students.sort()
print(students[0])
print(students[1])
    
    