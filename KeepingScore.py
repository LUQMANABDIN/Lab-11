t = True
playersScore = 0 # This variable will be useful later
scoreboard = {} # This list is empty so that the user can fill it
def x():
    scoreboard[player] = playersScore
def y():
    scoreboard[player] = scoreboard[player] + 1
def z():
    print ('We do not have any records of a player named ' + player + '.')
    print ('Would you like to add him/her as a new player?') # This function will be used to make sure that the user wants to add a new player to the list
print ('Hello')
print ('This is a digital scorekeeping program.')
print ('This program cwill keep a record of how many times your friends and yourself have won at a particular game')
print ('Lets start.')
# Explain what this program does
while t:
    print ('')
    print ('Type in a to view a players score.')
    print ('Type in b to add one point to a players score.')
    print ('Type in c to save these scores.')
    print ('Type in d to quit this program.')
    # Type out all the available options
    choice = input()
    if choice == 'a':
        print ('Whose score would you like to view?')
        player = input()
        if player in scoreboard:
            print (player + ' has a score of ' + str(scoreboard[player])) #Display the person's score
        else:
            z()
            choice2 = input()
            if choice2 == 'no':
                print ('Okay, ' + player + ' has not been added to our scoreboard.')
            elif choice2 == 'yes':
                x() # Use the playersScore variable inside the x() function to add the new player to the list and set their score to 0
                print ('Okay, ' + player + ' has now been added to our scoreboard.')
    elif choice == 'b':
        print ('Who do you want to give a point to?')
        player = input()
        if player in scoreboard:
            y()
            print (player + ' has now been given one additonal point.')
        else:
            z()
            choice3 = input()
            if choice3 == 'yes':
                x() # Set the new player's initial score to 0
                y() # Add 1 point onto that initial score
                print ('Okay, ' + player + ' has now been added to our scoreboard and given one point.')
            elif choice3 == 'no':
                print ('Okay,' + player + ' has not been added to our scoreboard.')
    elif choice == 'c':
        tallyKeeperFile = open('tallyKeeper.txt','w') # Create a text file
        for player in scoreboard:
            tallyKeeperFile.write(player + ' has a score of ' + str(scoreboard[player]) + '\n') # Display the a list of the players and their scores inside the text file
        tallyKeeperFile.close()
        print ('Okay, a record of the players and their scores have now been saved to a text file.') # Inform the user of what has happened
    elif choice == 'd':
        t = False # Terminate the program
print("I like keeping score!")
