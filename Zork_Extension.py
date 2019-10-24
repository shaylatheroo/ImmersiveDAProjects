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

    
#Initializing a bool for whether the user has found the secret room; it is currently false, once it is found, we'll toggle to true.
#Because Room 6 has two rooms accessible via going East, while this is False the game will need to only display the option to go East once.
#Once the secret room is found, it should display two options, East to Parlor or East to Secret Room.
secretRoom = False
currentRoom = 1
userChoice = ''
nextRoom = 0
isValid = True
userGold = 0
JeffsRoom = random.randint(1, 8)
roomsSeen=0

roomTracking = {
    1 : [False, random.randint(0, 1000)],
    2 : [False, random.randint(0, 1000)],
    3 : [False, random.randint(0, 1000)],
    4 : [False, random.randint(0, 1000)],
    5 : [False, random.randint(0, 1000)],
    6 : [False, random.randint(0, 1000)],
    7 : [False, random.randint(0, 1000)],
    8 : [False, random.randint(0, 1000)]
}
#userChoice is going to be holding our quit condition, such as a request to leave the house or simply quit

'''
so now that we've gotten the tracking initialized, and Jeff is getting set to a room, we just need to add the
logic for the Jeff encounter where there's a 50/50 chance of losing your gold, as well as logic that lets the
user take the gold from each room, track/print that running value, and then upon entering the room setting the
bool to true
'''

while userChoice != 'end':
    if currentRoom == 6:
        result = random.choices([True, False], weights=[1,4], k=1)
        secretRoom = result[0]
    #thinking I should just always pass a "current room" and the "secret room" value, regardless, to maximize reuse
    roomName, contents, exits = roomData(currentRoom, secretRoom)
    print("\nYou find yourself in the " + roomName + " of an old castle.")
    print("The room contains " + describeRoom(contents) + ".")
    if len(exits) == 1:
        print("You see a door to the " + describeRoomExits(exits) + ".")
    else:
        print("You see " + str(len(exits)) + " doors to the " + describeRoomExits(exits) + ".")
    if currentRoom == 6 and secretRoom == True:
        print("The two doors to the east lead to the parlor and... the secret room!")
    userChoice = input("Where would you like to go? ")
    userChoice, nextRoom, isValid = roomMovement(userChoice, currentRoom, exits)
    while isValid != True:
        userChoice = input("Your choice is not possible and the home groans. Which direction would you like to go? ")
        userChoice, nextRoom, isValid = roomMovement(userChoice, currentRoom, exits)
    currentRoom = nextRoom
    
print("\nYou have chosen to leave these musty, cursed halls...")
'''
We'll need to toss in something to print out the number of unique rooms visited, total gold,
and a list of the items in the rooms

This should utilize roomData, as it will give us the contents if we pass the room number, and
since the room number is stored in our dictionary it's an easy pass. We'll have superfluous data
returned, but that isn't the end of the world. Run roomData, then pass the contents off to
describeRoom for a result that's more print-friendly
'''

for x in roomTracking.values():
    if x[0]==True:
        roomsSeen+=1

roomContentsSeen = ''
        
print("You've seen " + str(roomsSeen) + " rooms of this desolate place... of a possible 8.")
print("In those rooms, you saw many things: \n" + roomContentsSeen + "\n... Maybe some of it is best forgotten")

if userGold > 0:
    print("On the bright side, you leave $" + userGold + " richer. Hopefully the gold isn't cursed...")
else:
    print("Sadly, you leave none the richer, either by force or by choice.")

result = random.choices([True, False], weights=[1,4], k=1)
if result[0]==True:
    print("You have a strange sense, as you leave the castle behind, that a spectral presense follows you home...")