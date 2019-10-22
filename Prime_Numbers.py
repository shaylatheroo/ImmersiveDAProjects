'''
Project Prompt:
A prime number is a number that has only itself and 1 as a factor. 

This means that for each of the numbers from 2 to that number, the number cannot be divided without a remainder. 

For example, 9 is not a prime number because it can be divided by 3 without a remainder. But 7 is a prime number because it cannot be divided by 2, 3, 4, 5, or 6 without a remainder. 

Write an appliation that will that show a list of numbers and indicate whether or not they are prime.

The user will have to input the last number in the range, and you will print all of the numbers from 1 to that number. 

For example you would have the numbers from 1 to 10 as follow: 

1 is not a prime number 

2 is a prime number 

3 is a prime number 

4 is not a prime number

5 is a prime number 

6 is not a prime number 

7 is a prime number 

8 is not a prime number 

9 is not a prime number 

10 is not a prime number 

The challenge is to do this without the use of importing a library
'''

num = input("Please enter the last number in your sequence: ")
num = int(num)

def is_prime(x):
    isPrime=True;
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                isPrime=False;
                break;
            else:
                isPrime=True;
    else:
        isPrime=True;
    return isPrime;
        
for a in range(1,(num+1)):
    primeResult = is_prime(a)
    if primeResult==True:
        print(str(a) + " is a prime number.")
    else:
        print(str(a) + " is not a prime number.")