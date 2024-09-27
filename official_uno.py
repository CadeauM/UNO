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
     
def reshuffle_deck(discard_pile, remaining_deck):
    top_card = discard_pile.pop()
    remaining_deck.extend(discard_pile)
    random.shuffle(remaining_deck)
    discard_pile.clear()
    discard_pile.append(top_card)
    print("Deck reshuffled.")


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

def process_special_cards(card, discard_pile, playerhand, computerhand, remaining_deck):
    """Handles action cards and returns the appropriate effect for the game loop"""
    if "wild" in card:
        new_color = input("Choose a color (red, green, blue, yellow): ")
        discard_pile[-1] = f"{new_color} {card.split()[-1]}"
        if "draw4" in card:
            for _ in range(4):
                if remaining_deck:
                    computerhand.append(remaining_deck.pop())
            print("Computer draws 4 cards.")
            return "wild4"
        return "skip"

    if "draw2" in card:
        for _ in range(2):
            if remaining_deck:
                computerhand.append(remaining_deck.pop())
        print("Computer draws 2 cards.")
        return "draw2"

    if "skip" in card:
        print("Computer is skipped.")
        return "skip"

    return None
     
def players_turn(playerhand, discard_pile, remaining_deck):
     
     # player should choose their card from their hand im going to make it an integer but its basically the index.
     print(f"Your cards: {playerhand}")
     top_card = discard_pile[-1]
     print(f"Top card is: {top_card}")
     print(players_choice = input(f"Choose a card to play (1-{len(playerhand)}) or type 'draw' to draw a card: "))
     while True:
        players_choice = input(f"Choose a card to play (1-{len(playerhand)}) or type 'draw' to draw a card: ")
        if players_choice.isdigit() and 1 <= int(players_choice) <= len(playerhand):
            choice_index = int(players_choice) - 1
            chosen_card = playerhand[choice_index]
            if playable_card(chosen_card, top_card):
                played_card = playerhand.pop(choice_index)
                discard_pile.append(played_card)
                print(f"You played {played_card}")
                return process_special_cards(played_card, discard_pile, playerhand, computerhand, remaining_deck)
            else:
                print("You can't play that card. Try again.")
        elif players_choice.lower() == 'draw':
            if remaining_deck:
                draw_card = remaining_deck.pop()
                playerhand.append(draw_card)
                print(f"You drew {draw_card}")
                if playable_card(draw_card, top_card):
                    playerhand.pop()
                    discard_pile.append(draw_card)
                    print(f"You played {draw_card}")
                    return process_special_cards(draw_card, discard_pile, playerhand, computerhand, remaining_deck)
            else:
                print("Deck is empty. Reshuffling discard pile...")
                reshuffle_deck(discard_pile, remaining_deck)

        else:
            print("Invalid choice, try again.")


# Creating a function for the computers turn...

def computers_turn(computerhand, discard_pile, remaining_deck):
     print("Computer's turn...")
     top_card = discard_pile[-1]
     
     playable_cards = [card for card in computerhand if playable_card(card, top_card)]
     if playable_cards:
        chosen_card = playable_cards[0]  # Play the first matching card
        computerhand.remove(chosen_card)
        discard_pile.append(chosen_card)
        print(f"Computer played {chosen_card}")
        return process_special_cards(chosen_card, discard_pile, playerhand, computerhand, remaining_deck)
     else:
        if remaining_deck:
            draw_card = remaining_deck.pop()
            computerhand.append(draw_card)
            print(f"Computer drew a card")
            if playable_card(draw_card, top_card):
                computerhand.remove(draw_card)
                discard_pile.append(draw_card)
                print(f"Computer played {draw_card}")
                return process_special_cards(draw_card, discard_pile, playerhand, computerhand, remaining_deck)
        else:
            print("Deck is empty. Reshuffling discard pile...")
            reshuffle_deck(discard_pile, remaining_deck)
        return None


# Alternating loop between player and computer up until one of them all their cards end.
def game_loop(playerhand, computerhand, discard_pile, remaining_deck):
    while True:
        # Player's turn
        result = players_turn(playerhand, discard_pile, remaining_deck)
        winner = check_the_winner(playerhand, computerhand)
        if winner:
            print(f"{winner} wins!")
            break

        # If the player's result doesn't skip the computer's turn
        if result not in ["skip", "wild4", "draw2"]:
            # Computer's turn
            result = computers_turn(computerhand, discard_pile, remaining_deck)
            winner = check_the_winner(playerhand, computerhand)
            if winner:
                print(f"{winner} wins!")
                break