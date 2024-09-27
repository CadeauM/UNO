import random  # this is a function we using to randomise the deck of cards

colours = ['Green', 'Blue', 'Yellow', 'Red']
numbers = list(range(1, 10))  # this makes list from 1 to 9, theres only one zero so do code seperately
deck = []
for colour in colours:
    # because theres one zero in each colour lets start with that get it out of the way
    deck.append(f"{colour} 0")
    for number in numbers:
        deck.append(f"{colour} {number}")
        deck.append(f"{colour} {number}")  # there are 2 of each colour therfore the repeated command.

action_cards = ['skip', 'reverse', 'draw2+']
for colour in colours:
    for action_card in action_cards:
        deck.append(f"{colour} {action_card}")
        deck.append(f"{colour} {action_card}")  # there are also 2 of each colour so we repeat the command again.

wild_cards = ['wild card', 'wild draw4+']  # there are 4 each we should use range to count out 4.
for wild_card in wild_cards:
        deck.append(f"{wild_card}")
        deck.append(f"{wild_card}")
        deck.append(f"{wild_card}")
        deck.append(f"{wild_card}")

random.shuffle(deck)  # shuffles our deck

#print(deck)

# deal the cards between the player and the computer
# we could use list of to index number of cards given/handed out
playerhand = deck[:7]
computerhand = deck[7:14]
remaining_deck = deck[14:]

discard_pile = [remaining_deck.pop()]

print(f"Remaining cards in deck are now: {len(remaining_deck)}")
print(f"The top card: {discard_pile}\n")
print(f"Your cards are: {playerhand}")

# Function to check who the winner is...
def check_the_winner(playerhand, computerhand):
     if len(playerhand) == 0:  # if the players cards are done
          return "You"
     elif len(computerhand) == 0:  # if the computers cards finish first
          return "The Computer"
     else:
          return None

# Create function for the players turn when they play their card
# The players card has to match to match top card of discard pile by colour or number or action. ACTION CARDS WILL GO LAST TO CREATE
def playable_card(card, topcard):  # card is players and top card is on top of discard file
     if "wild" in card:
          return True
     
     card_colour, card_value = card.split(' ', 1)

     if "wild" in topcard:
        return True
     topcard_colour, topcard_value = topcard.split(' ', 1)
     return card_colour == topcard_colour or card_value == topcard_value

def replenish_deck(remaining_deck, discard_pile):
    if not remaining_deck:
        fresh_discardpile = discard_pile.pop()  # Keep the top card
        remaining_deck = discard_pile[:]  # Copy the discard pile
        random.shuffle(remaining_deck)  # Shuffle the deck
        discard_pile.clear()
        discard_pile.append(fresh_discardpile)  # Keep only the top card
    return remaining_deck, discard_pile

def players_turn(playerhand, discard_pile, remaining_deck):
     
     # player should choose their card from their hand im going to make it an integer but its basically the index.
     players_choice = input(f"Choose a card to play from 1 to {len(playerhand)} or do you want to draw?  ")
     
     # since function to check conditions we use parameters in players_turn as arguments so it can be checked as well
    
     if players_choice.isdigit() and 1 <= int(players_choice) <= len(playerhand):
        players_choice = (int(players_choice)-1)
        if playable_card(playerhand[players_choice], discard_pile[-1]):
            played_card = playerhand.pop(players_choice)
            discard_pile.append(played_card)  # removes card from players hand and adds it to the dicard pile
            print(f"You played {discard_pile[-1]}\n")
            # action cards sayings...
            if "wild" in played_card:
                 # the player gets to choose a colour
                 new_color = input("You played a Wild Card! Choose a color(red, green, blue, yellow): ")
                 discard_pile[-1] = f"{new_color} wild card"
                 print(f"New color is {new_color}, continue your turn...")
                 return "skip"
            elif "wild draw4+" in played_card:
                 new_color = input("You played a wild Draw 4! Choose a color(red, green, blue, yellow): ")
                 discard_pile[-1] = f"{new_color} wild draw4+"
                 for _ in range(4):
                      if remaining_deck:
                           computerhand.append(remaining_deck.pop())
                 print(f"Computer draws 4 cards and skips its turn.")
                 return "wild4"

            if "skip" in played_card:
                 print("Computer was skipped, play again...")
                 print(f"Top card is: {discard_pile[-1]}")
                 print(f"Your cards are {playerhand}\n")
                 return "skip"
            elif "reverse" in played_card:
                 print("Reverse card played, play again")  # its a two way stream so it acts as a skip
                 print(f"Top card is: {discard_pile[-1]}")
                 print(f"Your cards are {playerhand}\n")
                 return "skip"
            elif "draw2+" in played_card:
                 print("The computer draws 2 cards and loses its turn, play again...")
                 print(f"Top card is: {discard_pile[-1]}")
                 print(f"Your cards are {playerhand}\n")
                 return "draw2"              
          
     elif players_choice == 'draw':
          if remaining_deck:  # if there is still a draw pile
               draw_card = remaining_deck.pop()  # takes last card in pile
               playerhand.append(draw_card)
               print(f"Your draw card is: {draw_card}")

               if playable_card(draw_card, discard_pile[-1]):
                    played_card = playerhand.pop()
                    discard_pile.append(played_card)
                    print(f"The current top card in discard pile is: {discard_pile[-1]}")
                    if "wild" in played_card:
                         # the player gets to choose a colour
                         new_color = input("You played a Wild Card! Choose a color(red, green, blue, yellow): ")
                         discard_pile[-1] = f"{new_color} wild card"
                         print(f"New color is {new_color}, continue your turn...")
                         return "skip"
                    elif "wild draw4+" in played_card:
                         new_color = input("You played a wild Draw 4! Choose a color(red, green, blue, yellow): ")
                         discard_pile[-1] = f"{new_color} wild draw4+"
                         for _ in range(4):
                              if remaining_deck:
                                   computerhand.append(remaining_deck.pop())
                         print(f"Computer draws 4 cards and skips its turn.")
                         return "wild4"
                    
                    if "skip" in played_card:
                        print("Computer was skipped, play again...")
                        print(f"Top card is: {discard_pile[-1]}")
                        print(f"Your cards are {playerhand}\n")
                        return "skip"
                    elif "reverse" in played_card:
                         print("Reverse card played, play again")  # its a two way stream so it acts as a skip
                         print(f"Top card is: {discard_pile[-1]}")
                         print(f"Your cards are {playerhand}\n")
                         return "skip"
                    elif "draw2+" in played_card:
                         print("The computer draws 2 cards and loses its turn, play again...")
                         print(f"Top card is: {discard_pile[-1]}")
                         print(f"Your cards are {playerhand}\n")
                         return "draw2"   
               else:
                    print("Your draw card does is not playable, your turn ends")
          else:
            # if remaining deck is done we take the discard file and reshuffle it so its a fresh draw pile
            fresh_discardpile = discard_pile.pop()
            new_pile = discard_pile[:]  # taking all discard pile except thke top
            random.shuffle(new_pile)
            discard_pile = [fresh_discardpile]
            
            draw_card = new_pile.pop()  # takes last card in pile

            playerhand.append(draw_card)
            print(f"Your draw card is: {draw_card}")

            if playable_card(draw_card, discard_pile[-1]):
                discard_pile.append(playerhand.pop())
                print(f"The current top card in discard pile is: {discard_pile[-1]}")   
            else:
                print("Your draw card does is not playable, your turn ends")
               
     else:
          print("Invalid choice. Please try again.")
          return players_turn(playerhand, discard_pile, remaining_deck)

# Creating a function for the computers turn...

def computers_turn(computerhand, discard_pile, remaining_deck):
     print("Its the computers turn...\n")
     #print(f"computers hand {computerhand}")
     print(f"Top card of the discard pile is: {discard_pile[-1]}")

     playable_cards = []  # empty list so that any playable card is stored in the list
     for card in computerhand:
          if playable_card(card, discard_pile[-1]):
               playable_cards.append(card)  # any playable card that matches with top card is added.

     if playable_cards:  # basically means if theres anything in it if the list exits then...
          played_card = playable_cards[0]
          discard_pile.append(played_card)  # The first playable card is given priority to be played.
          computerhand.remove(played_card)
          print(f"Computer played : {played_card}\n")
          print(f"The top card of discard pile is: {discard_pile[-1]}")
          print(f"Your cards are {playerhand}\n")

          if "wild" in played_card:
               new_color = random.choice(['red', 'green', 'blue', 'yellow'])
               discard_pile[-1] = f"{new_color} wild card"
               print(f"Computer played a wild card! New color is {new_color}")
               return "skip"
          elif "wild draw4+" in played_card:
               new_color = random.choice(['red', 'green', 'blue', 'yellow'])
               discard_pile[-1] = f"{new_color} wild draw4+"
               for _ in range(4):
                    if remaining_deck:
                         playerhand.append(remaining_deck.pop())
               print(f"Computer played a wild draw 4! You draw 4 cards and the new color is {new_color}")
               return "wild4"

          if "skip" in played_card:
            print("Computer played a skip card, you were skipped...")
            print(f"Top card is: {discard_pile[-1]}")
            return "skip"
          elif "reverse" in played_card:
            print("Computer played a reverse card! You were skipped...")  # its a two way stream so it acts as a skip
            print(f"Top card is: {discard_pile[-1]}")
            return "skip"
          elif "draw2+" in played_card:
            print("Computer played draw 2+, pick two cards...")
            print(f"Top card is: {discard_pile[-1]}")
            return "draw2"
          
     else:

        if remaining_deck:  # if there is still a draw pile
               draw_card = remaining_deck.pop()  # takes last card in pile
               computerhand.append(draw_card)
               print(f"Computer drew: {draw_card}")

               if playable_card(draw_card, discard_pile[-1]):
                    discard_pile.append(draw_card)
                    computerhand.remove(draw_card)
                    print(f"Computer played : {draw_card}\n")
                    print(f"The current top card in discard pile is: {discard_pile[-1]}")
                    print(f"Your cards are {playerhand}\n")

                    if "wild" in draw_card:
                         new_color = random.choice(['red', 'green', 'blue', 'yellow'])
                         discard_pile[-1] = f"{new_color} wild card"
                         print(f"Computer played a wild card! New color is {new_color}")
                         return "skip"
                    elif "wild draw4+" in draw_card:
                         new_color = random.choice(['red', 'green', 'blue', 'yellow'])
                         discard_pile[-1] = f"{new_color} wild draw4+"
                         for _ in range(4):
                              if remaining_deck:
                                   playerhand.append(remaining_deck.pop())
                         print(f"Computer played a wild draw 4! You draw 4 cards and the new color is {new_color}")
                         return "wild4"

                    if "skip" in draw_card:
                        print("Computer played a skip card, you were skipped...")
                        print(f"Top card is: {discard_pile[-1]}")
                        return "skip"
                    elif "reverse" in draw_card:
                        print("Computer played a reverse card! You were skipped...")  # its a two way stream so it acts as a skip
                        print(f"Top card is: {discard_pile[-1]}")
                        return "skip"
                    elif "draw2+" in draw_card:
                         print("Computer played draw 2+, pick two cards...")
                         return "draw2"
               else:
                    print("Computer's draw card is not playable, Your turn...\n")
                    print(f"The top card in discard pile is: {discard_pile[-1]}")
                    print(f"Your cards are {playerhand}\n")

        else:
               # if remaining deck is done we take the discard file and reshuffle it so its a fresh draw pile
               fresh_discardpile = discard_pile.pop()
               new_pile = discard_pile[:]  # taking all discard pile except the top
               random.shuffle(new_pile)
               discard_pile = [fresh_discardpile]
               draw_card = new_pile.pop()  # takes last card in pile
               computerhand.append(draw_card)
               if playable_card(draw_card, discard_pile[-1]):
                    discard_pile.append(computerhand.pop())
                    print(f"The current top card in discard pile is: {discard_pile[-1]}")   
               else:
                    print("Computer's draw card does is not playable, your turn...")


# Alternating loop between player and computer up until one of them all their cards end.
def game_loop(playerhand, computerhand, discard_pile, remaining_deck):  # for the playerturn and computerturn functions we take their hands and the discard pile as arguments therefore we'll take all three here
     take_turn = 0  # this is the players turn
     while True:
          if take_turn == 0:
               action = players_turn(playerhand, discard_pile, remaining_deck)  # as long as the take turn is 0 the player turn function should take place with its conditions
               The_winner = check_the_winner(playerhand, computerhand)
               if The_winner:
                    print(f"{The_winner} win!")
                    break              
               if action == "skip":
                    take_turn = 0
               elif action == "draw2":
                    for _ in range(2):
                         if remaining_deck:
                              computerhand.append(remaining_deck.pop())
                         else:
                              break
                    take_turn = 0  # The player gets to go again
               elif action == "wild04":
                    for _ in range(4):
                         if remaining_deck:
                              computerhand.append(remaining_deck.pop())
                         else:
                              break
                    take_turn = 0 #player goes again
               else:
                    take_turn = 1

          elif take_turn == 1: 
               action = computers_turn(computerhand, discard_pile, remaining_deck)  # same thing and everytime we change the take turn 
               The_winner = check_the_winner(playerhand, computerhand)
               if The_winner:
                    print(f"{The_winner} wins!")
                    break
               if action == "skip":
                    take_turn = 1
               elif action == "draw2":
                    for _ in range(2):
                         if remaining_deck:
                              playerhand.append(remaining_deck.pop())  # player draws 2 +
                         else:
                              break
                    take_turn = 1  # computer goes again...
               elif action == "wild04":
                    for _ in range(4):
                         if remaining_deck:
                              playerhand.append(remaining_deck.pop())
                         else:
                              break
                    take_turn = 1  # Computer goes again.
               else:
                    take_turn = 0
          else:
               break
game_loop(playerhand, computerhand, discard_pile, remaining_deck)