'''
You are going to develop an application to produce numbers in a sequence. 

The user will be required to enter a number, and for that number, you will: 

* Divide the number by 2 if it is even

* Multiply the number by 3, and add 1 if it is odd. 

* Do this until you get to 1. 

Ask the user if he/she would like to input another number, and continue until he/she does not want to enter any more numbers. 

Show the results as you go. For example, the number 5 should produce the following output: 

5 16 8 4 2 1

The number 3 should produce the following output: 

3 10 5 16 8 4 2 1 
'''

def Collatz():
    inputNumber = int(input("Please enter the first number in your sequence:"))
    
    print(int(inputNumber))

    while inputNumber != 1:
        if inputNumber%2==0:
            inputNumber = inputNumber/2
            print(int(inputNumber))
        else:
            inputNumber = inputNumber * 3 + 1
            print(int(inputNumber))

    repeatRequest = input("Would you like to continue? yes/no:").lower()
    if repeatRequest=='yes':
        return True
    else:
        return False
    
runFunction = True

while runFunction == True:
    runFunction = Collatz()