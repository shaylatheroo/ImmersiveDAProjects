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

def room1():
	roomName = 'foyer'
	contents = ['dead scorpion']
	exits = {
	'n' : 2
	}

def room2():
	roomName = 'front room'
	contents = ['piano']
	exits = {
	's' : 1,
	'w' : 3,
	'e' : 4
	}

def room3():
	roomName = 'library'
	contents = ['spiders']
	exits = {
	'e' : 2,
	'n' : 5
	}

def room4():
	roomName = 'kitchen/"food library"'
	contents = ['bats']
	exits = {
	'w' : 2,
	'n' : 7
	}

def room5():
	roomName = 'dining room'
	contents = ['dust','empty box']
	exits = {
	's' : 3
	}

def room6():
	roomName = 'vault'
	contents = ['3 walking skeletons']
	exits = {
	'e' : 7,
	'e' : 8
	}
	#don't forget that this room needs special conditions regarding which exits they can find

def room7():
	roomName = 'parlor'
	contents = ['treasure chest']
	exits = {
	'w' : 6,
	's' : 4
	}

def room8():
	roomName = 'secret room'
	contents = ['piles of gold']
	exits = {
	'w' : 6
	}