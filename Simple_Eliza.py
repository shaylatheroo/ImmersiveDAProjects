'''
You will be creating an interactive chat-bot type program.
Eliza is a therapist program that interacts with the user.
Your program will need to evaluate what the user asks and
turn the user's input into a question that sounds like the therapist really cares.

Your first task is to develop a program with a running loop.
If the user types in "I am feeling great" or enter "Q", the
program will stop running. Your program should print out the
last input (as an output) every time before accepting new input.
Make sure you are accommodating for NO case-sensitivity. (Q is the same as q)

Example output:
Good day. What is your problem? Enter your response here or Q to quit: my teacher hates me
my teacher hates me
Enter your response here or Q to quit: i dont know what's wrong
i dont know what's wrong
Enter your response here or Q to quit: i am feeling great
i am feeling great
>>> END

So in this simple iteration, the program should take input, and if the input is 'q' or 'i am feeling great'
(regardless of case), the program quits. Any input should be returned verbatim with the quit
conditions also returned before the program terminates
'''
repeatPrompt = True

userInput = input('Good day. What is your problem? Enter your response here or Q to quit: ')
print(userInput)
if (userInput.lower()=='q') or (userInput.lower()=='i am feeling great'):
    repeatPrompt=False
else:
    while repeatPrompt==True:
        userInput = input('Enter your response here or Q to quit: ')
        print(userInput)
        if (userInput.lower()=='q') or (userInput.lower()=='i am feeling great'):
            repeatPrompt=False