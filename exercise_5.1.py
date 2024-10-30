# data structures

# 2a) Write a python program that asks the user to enter ten integers, and displays a list containing their squares.
def exercise_2a():
    list = []
    for i in range(10):
        list.append(int(input("enter a number: ")))

    for i in range(10):
        list[i] = list[i] ** 2
    
    print(list)

exercise_2a()

    