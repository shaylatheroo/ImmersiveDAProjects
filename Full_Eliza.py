'''
You will be creating an interactive chat-bot type program. Eliza is a therapist program that interacts with the user. Your 
program will need to evaluate what the user asks and turn the user's input into a question that sounds like the therapist really cares.

Sample hedges:
Please tell me more
Many of my patients tell me the same thing
It is getting late, maybe we had better quit

Sample qualifiers:
Why do you say that
You seem to think that
So, you are concerned that
Replacements:

replace i with you
replace me with you
replace my with your
replace am with are
 

When the user enters a statement the program responds in one of two ways:

1. With a randomly chosen hedge, such as "Please tell me more"

2. By changing some keywords  in the user's input string and appending this string to a randomly chosen qualifier. 
To get a random item from a dictionary, set the dictionary keys to be an index for each qualifier, 
then select a random number in order to pull the value from the dictionary to get the string qualifier phrase.

 

Here's how the replacement works:

The user enters something at the prompt: "my teacher hates me"

The program will loop through that string and replace "my" with "your" and "me" with "you" and then 
prepend the qualifier to the replacement string. So, my teacher hates me becomes "Why do you say that 
your teacher hates you?" The replacement method returns the same words as the user entered only the 
replacement words have been swapped. Then the qualifier is prepended to the user's words.

Spend some time thinking how you would search through a string and replacing specific words. Hint: try using the .split() function

Example session with Eliza

Good day. What is your problem? Enter your response here or Q to quit: my teacher hates me
Why do you say that your teacher hates you
Enter your response here or Q to quit: she always calls on the girls in the class
Please tell me more
Enter your response here or Q to quit: i would like to get called on too
You seem to think that you would like to get called on too
Enter your response here or Q to quit: q
'''

'''
This is the code I used in the Intermediate_Eliza program

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
'''

'''
So, on top of the base code I have here, I'll need to work up a dictionary of the hedges and qualifiers,
then randomly use a hedge statement, or reword the patient's input with a qualifier tacked onto the back

We are no longer returning the reworked statement before quitting should they be choosing to do that - so we can
reorder the former code to stop doing that.

First, when there is non-quit input, we can run a random module to decide if we're sending a hedge or adding a qualifier.
If a hedge, we don't need to process the input - simply return the hedge and re-prompt for a reply or Q to quit.

So, to process...
- We do the initial prompt
- If not quitting, we proceed to randomly decide if we're doing a hedge or qualifier
	-If hedge, randomly choose a hedge, print it, proceed to re-prompt the user for input
	-If qualifier, proceed to process the user's input, and print with teh qualifer before the processed input; re-prompt
'''
# While all other assignments we've tried to avoid importing anything,
# random is useful and important for this specific application
import random

# Initializing the boolean variable that allows the program to iterate
repeatPrompt = True

def rewordingInput(x):
    hedgeList = ['Please tell me more', 'Many of my patients tell me the same thing', 'It is getting late, maybe we had better quit']
    qualifierList = ['Why do you say that ', 'You seem to think that ', 'So, you are concerned that ']
    randomLists = [hedgeList, qualifierList]
    result = random.choice(random.choice(randomLists))
    outputString = result
    
    x = x.lower()
    splitInput = x.split(' ')
    
    # First, I'll be running random to choose whether we're using a hedge or qualifier
    if result in hedgeList:
        return outputString
    
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

if (userInput.lower()=='q') or (userInput.lower()=='i am feeling great'):
    repeatPrompt=False
else:
    while repeatPrompt==True:
        #We will now process the input, printing the reworded content
        #The defined fuction will also handle randomization
        print(rewordingInput(userInput))
        userInput = input('Enter your response here or Q to quit: ')
        if (userInput.lower()=='q') or (userInput.lower()=='i am feeling great'):
            repeatPrompt=False