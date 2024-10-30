# data structures

# 2a) Write a python program that asks the user to enter ten integers, and displays a list containing their squares.
def exercise_2a():
    list = []
    for i in range(10):
        list.append(int(input("enter a number: ")))

    for i in range(10):
        list[i] = list[i] ** 2
    
    print(list)

#exercise_2a()

#5a) Find the average of marks in 3 subjects for a 1000 students. The students' id range from 0 to 999. 
# The marks can be generated randomly. Implement this using both lists and dictionaries. 
# Compare the size (of the data structures) in memory as well as performance (ie, running time), and comment on your findings.

def exercise_5a():
    student_id = []
    for i in range(1000):
        student_id.append(i)
    print(student_id)

exercise_5a()
    