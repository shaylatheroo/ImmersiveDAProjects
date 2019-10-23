'''
Create a program that mimics the Magic 8 Ball. If you don't know what a Magic 8 Ball is ... it's a toy ball containing a clear 'window'. You shake the ball and ask it a question. A random response rises to the window. You can read about the Magic 8 Ball on Wikipedia (Links to an external site).

Your program will prompt the user for a question and select a random answer from the list below. See the required output below the responses.

It is certain
It is decidedly so
Without a doubt
Yes definitely
You may rely on it
As I see it, yes
Most likely
Outlook good
Yes
Signs point to yes
Reply hazy try again
Ask again later
Better not tell you now
Cannot predict now
Concentrate and ask again
Don't count on it
My reply is no
My sources say no
Outlook not so good
Very doubtful

Implement a loop to continue asking the user for more questions until they enter "No" to stop.

Write a method to handle the generating of the random response.

Display the question and the answer to the user.

SAMPLE OUTPUT:
YOU ASKED: Will I win the lottery tomorrow?
 
MAGIC 8-BALL SAYS: Reply hazy, try again
 
Do you have another question for the Magic 8-Ball? (y/n)
n

Thank you for playing!
'''

import random

ball_responses = ['It is certain','It is decidedly so','Without a doubt','Yes definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again',"Don't count on it",'My reply is no','My sources say no','Outlook not so good','Very doubtful']
ball_result = 'Something has gone wrong'
#This initialized result will only show if things don't evaluate properly

play_Again = True

user_question = input("You have come to seek the wisdom of the Magic 8 Ball, what would you ask of me?")
print("You have asked... " + user_question)
ball_result = random.choice(ball_responses)
print("The mists have parted to tell me... " + ball_result)

while play_Again == True:
    play_reply = input("Would you ask me to consult the beyond once more? (y/n)")
    if play_reply=='y' or play_reply=='Y':
        user_question = input("Present your question, mortal.")
        print("You have asked... " + user_question)
        ball_result = random.choice(ball_responses)
        print("The mists have parted to tell me... " + ball_result)
    else:
        print("I shall return when you next require another look into the unknown...")
        play_Again = False