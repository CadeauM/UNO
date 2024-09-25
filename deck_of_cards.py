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

action_cards = ['skip', 'reverse', 'draw 2+']
for colour in colours:
    for action_card in action_cards:
        deck.append(f"{colour} {action_card}")
        deck.append(f"{colour} {action_card}")  # there are also 2 of each colour so we repeat the command again.

wild_cards = ['wild card', 'wild draw 4+']  # there are 4 each we should use range to count out 4.
for wild_card in wild_cards:
        deck.append(f"{wild_card}")
        deck.append(f"{wild_card}")
        deck.append(f"{wild_card}")
        deck.append(f"{wild_card}")

random.shuffle(deck)  # shuffles our deck

print(deck)

# deal the cards between the player and the computer
# we could use list of to index number of cards given/handed out
playerhand = deck[:7]
computerhand = deck[7:14]
rest_of_deck = deck[14:]

print(f"Your cards are: {playerhand}")
print(f"The remaining cards in deck are: {len(rest_of_deck)}")

"""
print(deck)
print(len(deck))
print(computerhand)

"""

# Creating a discard pile and card on top should start.

discard_pile = deck[14]
remaining_deck = deck[15:]
print(f"The starting card is {discard_pile}")
print(f"The remaining cards in deck are now: {len(remaining_deck)}")

# Create function for the players turn when they play their card
# The players card has to match to match top card of discard pile by colour or number or action. ACTION CARDS WILL GO LAST TO CREATE

def playable_card(card, topcard):  # card is players and top card is on top of discard file
     card_properties = card.split(' ', 1)  # it splits the card into two properties colour and number/action, 1 makes sure it splits once
     card_colour = card_properties[0]  # the card colour
     card_value = card_properties[1]  # the card value/action
     
     topcard_properties = topcard.split(' ', 1)  # splits the top card into its properties
     topcard_colour = topcard_properties[0]
     topcard_value = topcard_properties[1]

     if card_colour == topcard_colour or card_value == topcard_value:  # if one of the properties match returns true.
          return True
     else:
          return False
     
#print(playable_card('Red 5', 'Blue 5'))

def players_turn(playerhand, discard_pile):
     # displaying what we have currently
     print(f"These are your current cards: {playerhand}")
     print(f"The discard pile is currently: {discard_pile[-1]}")  # This is to get the last card that was appended to the list basically the top card
     
     # player should choose their card from their hand im going to make it an integer but its basically the index.
     players_choice = int(input(f"Enter the index of the card you choose, choose from 0 to {len(playerhand)}"))
     
     # since function to check conditions we use parameters in players_turn as arguments so it can be checked as well
     if playable_card(playerhand[players_choice], discard_pile[-1]):
          discard_pile.append(playerhand.pop(players_choice))  # removes card from players hand and adds it to the dicard pile
          print(f"Player played {discard_pile[-1]}")
          print(playerhand)
     else:
          print("Invalid choice nothing matches, draw a card from the pile...")
          
          if remaining_deck:  # if there is still a draw pile
               draw_card = remaining_deck.pop()  # takes last card in pile
               playerhand.append(draw_card)
               print(f"Your draw card is: {draw_card}")

               if playable_card(draw_card, discard_pile[-1]):
                    discard_pile.append(playerhand.pop())
                    print(f"The current top card in discard pile is: {discard_pile}")   
               else:
                    print("Your draw card does is not playable, your turn ends")
          else:
               # if remaining deck is done we take the discard file and reshuffle it so its a fresh draw pile
               fresh_discardpile = discard_pile.pop()
               new_pile = discard_pile[:]  # taking all discard pile except the top
               random.shuffle(new_pile)
               discard_pile = [fresh_discardpile]
               
               draw_card = new_pile.pop()  # takes last card in pile

               playerhand.append(draw_card)
               print(f"Your draw card is: {draw_card}")

               if playable_card(draw_card, discard_pile[-1]):
                    discard_pile.append(playerhand.pop())
                    print(f"The current top card in discard pile is: {discard_pile}")   
               else:
                    print("Your draw card does is not playable, your turn ends")

# Creating a function for the computers turn...

def computers_turn(computerhand, discard_pile):
     print("Its the computers turn...")
     #print(f"computers hand {computerhand}")
     print(f"This is the top card of your dicard pile {discard_pile[-1]}")

     playable_cards = []  # empty list so that any playable card is stored in the list
     for card in computerhand:
          if playable_card(card, discard_pile[-1]):
               playable_cards.append(card)  # any playable card that matches with top card is added.

     if playable_cards:  # basically means if theres anything in it if the list exits then...
          discard_pile.append(playable_cards[0])  # The first playable card is given priority to be played.
          computerhand.remove(playable_cards[0])
          print(f"Computer played : {playable_cards[0]}")
     else:

        if remaining_deck:  # if there is still a draw pile
               draw_card = remaining_deck.pop()  # takes last card in pile
               computerhand.append(draw_card)
               print(f"Computer drew: {draw_card}")

               if playable_card(draw_card, discard_pile[-1]):
                    discard_pile.append(computerhand.pop())
                    print(f"The current top card in discard pile is: {discard_pile}")   
               else:
                    print("Computer's draw card does is not playable, Your turn...")

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
                    print(f"The current top card in discard pile is: {discard_pile}")   
               else:
                    print("Computer's draw card does is not playable, your turn...")
