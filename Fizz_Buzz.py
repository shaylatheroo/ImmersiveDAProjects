'''
Write a program that prints the numbers from 1 to 100.

For multiples of 3 print “Fizz” instead of the number.

For the multiples of five print “Buzz”.

For numbers which are multiples of both 3 and 5 print “FizzBuzz”.
'''

for x in range(1,101):
    printOutput = x
    if (x%3==0) and (x%5==0):
        printOutput = 'FizzBuzz'
    elif x%5==0:
        printOutput = 'Buzz'
    elif x%3==0:
        printOutput = 'Fizz'

    print(printOutput)