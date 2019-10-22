'''
You will continue creating an interactive chat-bot type program. Eliza is a therapist program that interacts with the user. Your program will need to evaluate what the user asks and turn the user's input into a question that sounds like the therapist really cares.

Use lists or dictionaries to loop through user's input and implement the following:

Replacements:

replace i with you
replace me with you
replace my with your
replace am with are
We will continue to build on top of this application throughout the week. 

Here's how the replacement works:

The user enters something at the prompt: "my teacher hates me"

The program will loop through that string and replace "my" with "your" and "me" with "you" and then prepend the qualifier to the replacement string. So, my teacher hates me becomes "Why do you say that your teacher hates you?" The replacement method returns the same words as the user entered only the replacement words have been swapped.

Spend some time thinking how you would search through a string and replacing specific words. Hint: try using the .split() function

Example output:
Good day. What is your problem? Enter your response here or Q to quit: my teacher hates me
your teacher hates you
Enter your response here or Q to quit: i dont know what's wrong
you dont know what's wrong
Enter your response here or Q to quit: i am feeling great
you are feeling great
'''

repeatPrompt = True

def rewordingInput(x):
    x = x.lower()
    splitInput = x.split(' ')
    outputString = ''
    z=0    
    while z<len(splitInput):
        if splitInput[z]=='i':
            splitInput[z]='you'
        elif splitInput[z]=='me':
            splitInput[z]='you'
        elif splitInput[z]=='my':
            splitInput[z]='your'
        elif splitInput[z]=='am':
            splitInput[z]='are'
        z+=1
    
    for n in splitInput:
        outputString = outputString + n + ' '
        
    return outputString

userInput = input('Good day. What is your problem? Enter your response here or Q to quit: ')
print(rewordingInput(userInput))
if (userInput.lower()=='q') or (userInput.lower()=='i am feeling great'):
    repeatPrompt=False
else:
    while repeatPrompt==True:
        userInput = input('Enter your response here or Q to quit: ')
        print(rewordingInput(userInput))
        if (userInput.lower()=='q') or (userInput.lower()=='i am feeling great'):
            repeatPrompt=False