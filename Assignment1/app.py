
# this program will display the respricol  and the square of any number

# this variable message will hold message about what the programming is going to do
Welcome_message = """
Welcome To the program :
This program will give you the reciprocal and the square of any number you enter
"""
main_message = """
!!!!! You Have 5 Times to Attempt !!!!!
---------------------------------------
Please Enter any Number You Want to get The Reciprocal and square of that number
"""


# this username holds name of the user and print the name of the user with message that
# describes if it connected or not
username = input("Please input your username : ")

print(f'Hello, {username} Now You Are Connected.....')
# this statement will make new line
print(end='\n')
# to seperate upper part of the output and lower part
for i in range(35):
    print("- ", end=''),
# this is function prints out the recprical and square of the number that user entered


def reciprocal_square_fun():

    number = eval(input())
    # reciprical is 1/the number of user entered
    reciprocal = 1.0/number
    # square of the number is num*num
    square = number*number

    print(f"the recprical of {number} is 1/{number} = {reciprocal} ")
    print(f"The Square of {number} is {square}")


# this block will run one time
print(Welcome_message)
print(main_message)
print("Attempt 1")
reciprocal_square_fun()
# This for Loop gives 5 times to attempt without cancelling the program
for Attempt in range(1, 5):
    print(end="\n")
    print("Attempt", Attempt+1)
    reciprocal_square_fun()
    print("You Attempted ", Attempt+1, "times")

# This will show up when the user have attempt chance
print("\n!!!!!!!!!!!!!!!!!You Have 0 Attempt Chance Thank you !!!!!!!!!!!!!!!!")
