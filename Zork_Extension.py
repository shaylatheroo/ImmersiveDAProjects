'''
Zork is a famous text-only adventure game for the computer. Users would type commands and navigate the rooms of a castle.

Write an application that asks the user what direction they wish to travel in. Once they tell you the direction, move them to the next room and tell them what is in it and what direction the other exits are.

When you develop your program it is helpful to include each room in its own function. The role of the functions are to get input from the user and direct the user to the appropriate room.

Your program shall allow the user to move from one room back and forth to any other connected room.

You program should allow the user to find the secret room only 25% of the time. However, once they find the secret room they can always find it.

When the user exits the house or quits there is a 25% chance they will be followed by a ghost. Let them know when they are being followed.

Also let the user know how many rooms they visited after they exit or quit.

room			contains				doors to (direction & room #)
#1	foyer		dead scorpion			room n2
#2	front room	piano					rooms s1,w3, e4
#3	library		spiders					rooms e2 & n5
#4	kitchen		bats					rooms w2 & n7
#5	dining room	dust empty box			room s3
#6	vault		3 walking skeletons		room e7 : room e8 (only 25% chance of finding)
#7	parlor		treasure chest			rooms w6, s4
#8	secret room	piles of gold			room w6
'''

'''
Why am I confounded by the lack of treasure in the vault and the lack of need to find a combination to enter the vault.
One of the rooms should contain the vault key or combination, so you have to visit that room to be able to access the vault.
'''

'''
Take the Zork program you completed in the previous assignment and extend it allow for 
each room to have a random amount of money between $0 and $1000.00, that you can take, 
adding it to your personal total. If the money is taken it is not in the room anymore.

Update the program so that every time it tells you about a room it also tells you how much money you have.

Once you implement all that add a character which you shall name to the room. 
The character will be randomly assigned to one room when the game begins. 
For example the character will appear in the kitchen. Then when the player appears 
in the kitchen then the character will try to take their money. The character will 
take all the money the player has gathered so far.

When you exit the program it will print out the number of rooms you have visited, 
the items you have seen (like skeletons, pianos, and dusty boxes), and the amount of money you have.
'''

'''
I find the term "try" to be very important regarding the random encounter. So, I made it
possible that you encounter "Jeff" and he be unsuccessful in taking your gold.
'''
import random

def room1():
    roomName = 'foyer'
    contents = ['a dead scorpion']
    exits = {
    'n' : 2
    }
    return roomName, contents, exits

def room2():
    roomName = 'front room'
    contents = ['a piano']
    exits = {
    's' : 1,
    'w' : 3,
    'e' : 4
    }
    return roomName, contents, exits

def room3():
    roomName = 'library'
    contents = ['spiders']
    exits = {
    'e' : 2,
    'n' : 5
    }
    return roomName, contents, exits

def room4():
    roomName = 'kitchen/"food library"'
    contents = ['bats']
    exits = {
    'w' : 2,
    'n' : 7
    }
    return roomName, contents, exits

def room5():
    roomName = 'dining room'
    contents = ['dust','an empty box']
    exits = {
    's' : 3
    }
    return roomName, contents, exits

def room6(secretRoom): 
    roomName = 'vault'
    contents = ['3 walking skeletons']
    exitsTrue = {
    'e1' : 7,
    'e2' : 8
    }
    exitsFalse = {
    'e' : 7
    }
    if secretRoom ==True:
        exits = exitsTrue
    else:
        exits = exitsFalse
    return roomName, contents, exits

def room7():
    roomName = 'parlor'
    contents = ['a treasure chest']
    exits = {
    'w' : 6,
    's' : 4
    }
    return roomName, contents, exits

def room8():
    roomName = 'secret room'
    contents = ['piles of gold']
    exits = {
    'w' : 6
    }
    return roomName, contents, exits

def roomData(currentRoom, secretRoom):
    if currentRoom ==1:
        return room1()
    elif currentRoom == 2:
        return room2()
    elif currentRoom == 3:
        return room3()
    elif currentRoom == 4:
        return room4()
    elif currentRoom == 5:
        return room5()
    elif currentRoom == 6:
        return room6(secretRoom)
    elif currentRoom == 7:
        return room7()
    elif currentRoom == 8:
        return room8()
    
def describeRoom(contents):
    returnValue = ''
    iterator = 0
    if len(contents) > 1:
        return contents[0]
    else:
        for x in contents:
            returnValue += x
            while iterator < (len(contents)-1):
                returnValue += ' and '
                iterator+=1
        return returnValue
    
def describeRoomExits(exits):
    returnValue = ''
    numberOfExits = len(exits)

    if 'n' in exits:
        returnValue += 'north'
        if numberOfExits > 1:
            returnValue += ' and '
            numberOfExits -= 1
    if 's' in exits:
        returnValue += 'south'
        if numberOfExits > 1:
            returnValue += ' and '
            numberOfExits -= 1
    if 'e' in exits:
        returnValue += 'east'
        if numberOfExits > 1:
            returnValue += ' and '
            numberOfExits -= 1
    if 'w' in exits:
        returnValue += 'west'
        if numberOfExits > 1:
            returnValue += ' and '
            numberOfExits -= 1
    if 'e1' in exits: #this means we are running under the condition that the secret room is found, where there are technically two doors to the east
        returnValue += 'east'
        
    return returnValue

def roomMovement(userChoice, currentRoom, exits):
    userChoice = userChoice.lower()
    nextRoom = 0
    splitUserChoice = userChoice.split()
    isValid = True
    if 'quit' in splitUserChoice:
        userChoice = 'end'
        return userChoice, nextRoom, isValid
    elif 'end' in splitUserChoice:
        userChoice = 'end'
        return userChoice, nextRoom, isValid
    elif 'leave' in splitUserChoice:
        userChoice = 'end'
        return userChoice, nextRoom, isValid
    elif 'stop' in splitUserChoice:
        userChoice = 'end'
        return userChoice, nextRoom, isValid
    elif 'north' in splitUserChoice:
        userChoice = 'n'
    elif 'n' in splitUserChoice:
        userChoice = 'n'
    elif 'south' in splitUserChoice:
        userChoice = 's'
    elif 's' in splitUserChoice:
        userChoice = 's'
    elif 'secret' in splitUserChoice:
        userChoice = 'e2'
    elif 'parlor' in splitUserChoice:
        userChoice = 'e1'
    elif 'east' in splitUserChoice:
        userChoice = 'e'
    elif 'e' in splitUserChoice:
        userChoice = 'e'
    elif 'w' in splitUserChoice:
        userChoice = 'w'
    elif 'west' in splitUserChoice:
        userChoice = 'w'
    
    isValid, nextRoom = validateChoice(userChoice, exits)
    
    return userChoice, nextRoom, isValid

def validateChoice(userChoice, exits):
    isValid = False
    nextRoom = 0
    
    if userChoice in exits:
        isValid = True
        nextRoom = int(exits.get(userChoice))
    
    return isValid, nextRoom


secretRoom = False
currentRoom = 1
userChoice = ''
nextRoom = 0
isValid = True
userGold = 0
JeffsRoom = random.randint(1, 8)
roomsSeen=0

roomTracking = {
    1 : [False, random.randint(0, 1000), ''],
    2 : [False, random.randint(0, 1000), ''],
    3 : [False, random.randint(0, 1000), ''],
    4 : [False, random.randint(0, 1000), ''],
    5 : [False, random.randint(0, 1000), ''],
    6 : [False, random.randint(0, 1000), ''],
    7 : [False, random.randint(0, 1000), ''],
    8 : [False, random.randint(0, 1000), '']
}

print("On your walk along a wooded trail, you come upon an old, abandoned castle.")
print("Perhaps against your better judgement, you've decided to have a look around.")
print("After a little work undoing a jammed front door...")

while userChoice != 'end':
    if currentRoom == 6:
        result = random.choices([True, False], weights=[1,4], k=1)
        secretRoom = result[0]
    #thinking I should just always pass a "current room" and the "secret room" value, regardless, to maximize reuse
    roomName, contents, exits = roomData(currentRoom, secretRoom)
    
    '''
    This portion will update the roomTracking dictionary's list for the currentRoom to state True,
    indicating the room has been seen for later use. It's simply set to True rather than double-checking
    if the room has ever been seen simply because that doesn't really matter. We won't cause any issues
    unless we wanted the output to look different if the room's been seen before.
    '''
    (roomTracking[currentRoom])[0] = True
    (roomTracking[currentRoom])[2] = describeRoom(contents)
    
    print("\nYou find yourself in the " + roomName + ".")
    print("The room contains " + describeRoom(contents) + ".")
    if (roomTracking[currentRoom])[1] > 0:
        print("There is $" + str((roomTracking[currentRoom])[1]) + " of gold available to take from the room.")
    print("You're currently carrying $" + str(userGold) + ".")

    if (roomTracking[currentRoom])[1] > 0:
        takeGold = input("Would you like to take the gold? ")
        if takeGold.lower() == 'yes' or takeGold.lower() == 'y':
            userGold += (roomTracking[currentRoom])[1]
            (roomTracking[currentRoom])[1] = 0
            print("You're now carrying $" + str(userGold) + ".")
            
    '''
    Tossing in the Jeff encounter right here. He'll attack from the shadows as you've mulled over your choice
    regarding the money from the room, but only if you're carrying any money to begin with (kind of silly otherwise).
    '''
    
    if currentRoom == JeffsRoom:
        print("\nYou feel someone watching you from the shadows of the room...")
        #This essentially makes it so the encounter waits to trigger when you actually have gold
        #Then, it triggers once. Regardless of robbery success, he leaves after.
        #We *could* reset this logic to assign a failed robbery to a new random room.
        if userGold > 0:
            print("'I'm Jeff, and that's my gold!' is shouted from behind you!")
            JeffSuccess = random.choice([True, False])
            if JeffSuccess == True:
                print("Jeff has robbed you! He took the $" + str(userGold) + " you had gathered!")
                userGold = 0
                print("The man has run back off into the shadows, cackling with glee. You think he's left the mansion.")
                JeffsRoom = 0
                print("You're back to $" + str(userGold) + " gold in your pocket, but at least you're alive!")
            else:
                print("Jeff has attempted to rob you, lunging your way! You were quick on your feet, though, and avoided his attack.")
                print("The strange man hisses at you before running away. You think you hear his footsteps carry him out of the mansion.")
                JeffsRoom = 0
                print("You still have the $" + str(userGold) + " gold in your pocket.")
    
    if len(exits) == 1:
        print("\nYou see a door to the " + describeRoomExits(exits) + ".")
    else:
        print("\nYou see " + str(len(exits)) + " doors to the " + describeRoomExits(exits) + ".")
    if currentRoom == 6 and secretRoom == True:
        print("The two doors to the east lead to the parlor and... the secret room!")
    
    userChoice = input("Where would you like to go? ")
    userChoice, nextRoom, isValid = roomMovement(userChoice, currentRoom, exits)
    while isValid != True:
        userChoice = input("Your choice is not possible and the very stones of the mansion groan. Which direction would you like to go? ")
        userChoice, nextRoom, isValid = roomMovement(userChoice, currentRoom, exits)
    currentRoom = nextRoom
    
print("\nYou have chosen to leave these musty, cursed halls...")

roomContentsSeen = ''

for x in roomTracking.values():
    if x[0]==True:
        roomsSeen+=1
        roomContentsSeen = roomContentsSeen + x[2] + "\n"
        
print("You've seen " + str(roomsSeen) + " rooms of this desolate place... of a possible 8.")
print("In those rooms, you saw many things: \n" + roomContentsSeen + "... Maybe some of it is best forgotten?")

if userGold > 0:
    print("\nOn the bright side, you leave $" + str(userGold) + " richer. Hopefully the gold isn't cursed...")
else:
    print("\nYou leave none the richer - financially, anyways - either by force or by choice.")

result = random.choices([True, False], weights=[1,4], k=1)
if result[0]==True:
    print("But... you have a strange sense, as you leave the castle behind, that a spectral presense follows you home...")
