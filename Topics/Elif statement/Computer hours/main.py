# Make sure your output matches the assignment *exactly*

# Write a program that asks a user how long, on average,
# they spend on a computer per day. If it's less than 2 hours,
# the program should output "That's rare nowadays!".
# If it is 2 hours or more, but less than 4 hours per day it
# should output"This seems reasonable". In any other case,
# output "Don't forget to take breaks!"

screen_time = int(input())

if screen_time < 2:
    print("That's rare nowadays!")
elif 2 <= screen_time < 4:
    print("This seems reasonable")
else:
    print("Don't forget to take breaks!")
