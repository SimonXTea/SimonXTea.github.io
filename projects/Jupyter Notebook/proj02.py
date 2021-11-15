## Made by Simon X Camilo
## PROJECT 2: ROCK, PAPER, SCISSORS
## Jaime Mahoney
## CSC 125 - Python Programming
## 11/8/2020

import random ## allows me to use the randomize command
import time ## Allows me to make it so the scoreboard doesn't close instantly

#Sets the rules of the game, decides who wins. Key are the choices, definition is the winner
RULES = {
  ('s', 'p'): 's',
  ('p', 'r'): 'p',
  ('r', 's'): 'r',
}

# "Legal Values" Sets the options the bot has for randomization. M is a common nickname to smart bots I make. It also decides what values are allowed
M = ["s", "p", "r"]

#Tells the user the controls of the game
print("Legend:")
print("Type s for scissors")
print("Type p for paper")
print("Type r for rock")
print()

replay = True # tells the program if the user wants to keep playing, used in a while loop
# scoreboard
s = 0
r = 0
p = 0
t = 0
player = 0
computer = 0

while replay:
    incorrect = True # Sees that the value entered by the user is correct
    hand1 = input("Your hand: ").lower() # Gets user's input
    while incorrect:
        if hand1 in M:
            incorrect = False # because the user entered one of the legal values, the user can continue
        else:
            hand1 = input("Your hand: ").lower() # the user is going to be asked to enter another value if it's not correct (doesn't appear in M)                          
    if eval(hand1) == r and hand1 != "r": # sees if the bot can make a smart decision, based on patterns from the player.
        # It does this by comparing the numerical value the player's choice has (based on how many times it has been picked) with the value on every choice
        # It also compares the player's entered variable with each option. If any of the two are equal, it can't make a smart decision
        bot = random.choice(M) # if it can't make a smart decision, it will choose a random value
    elif eval(hand1) == p and hand1 != "p":
        bot = random.choice(M)
    elif eval(hand1) == s and hand1 != "s":
        bot = random.choice(M)
    else: # if the bot notices a pattern and can make a smart decision, it will choose the best option
        botting = {"r":r,"p":p,"s":s} # updates the database for the bot
        bott = max(botting, key=botting.get) # gets the variable with the highest value/most used by player in the scoreboard
        if bott == "p": # tells the bot how to win against this value
            bot = "s"
        elif bott == "s":
            bot = "r"
        else:
            bot = "p"
    winner = RULES.get((hand1, bot), RULES.get((bot, hand1), 'tie')) # declares who won based on the dictionary
    
    # this gives more info to the program
    if winner is "s":
        loser = "paper" # if scissors won, paper loses
        act = "cut" # describes in detail what the winner does
        winner = "scissors" # translates the winner to a word, in order to print results
    elif winner is "p":
        loser = "rock"
        act = "covers"
        winner = "paper"
    elif winner is "r":
        loser = "scissors"
        act = "breaks"
        winner = "rock"
    else: # if it's not any of the above, then it must be a tie
        t += 1 # counts in the scoreboard as a tie
        
    if hand1 == "s":
        hand1 = "scissors" # translaters player's choice to a word, so it can be compared to the winner at the end of the code. This way, the program can declare which player won
        s += 1 # counts how many times the player has picked that option
    elif hand1 == "p":
        hand1 = "paper"
        p += 1 # counts how many times the player has picked that option
    else: # if it's not any of the above, then it could had only been rock
        hand1 = "rock"
        r += 1 # counts how many times the player has picked that option

    if winner is "tie": #declares a tie
        print("It's a tie")
    else:
      print(winner.capitalize(), act, loser.capitalize()) # Says what happened based on the choices.
      if hand1 == winner: # Announces that the human won. It knows this if the translated hand1 and winner are the same
          print("Player wins")
          player += 1 # Counts how many times the player has won
      else: # Announces that the machine won. If the above is wrong, then the machine won
          print("Computer wins")
          computer += 1 # Counts how many times the computer has won

    again = input("Press Q to Quit, Enter to keep playing ").lower() #Asks the player if they want to continue
    if again == "q": #if the player decides to quit
        replay = False # the program is told to not start another game
        # It publiahes the scoreboard
        print("Player:", player)
        print("Bot:", computer)
        print("Ties:", t)
        print("Your Rocks:", r)
        print("Your Papers:", p)
        print("Your Scissors:", s)
        print("=====")
        print("Thanks for playing! This program will close in 30 seconds")
        time.sleep(30) # allows player to see the scoreboard
        print("Byebye")
    else:
        print()
    # The program starts another game