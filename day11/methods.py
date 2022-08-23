import art
import random

def system_loop():
    print(art.logo)
    done = False
    while(not done):
        print(play_game())
        done = input("Do you want to play another game? Press 'y' to continue. ").lower() != "y"


def play_game():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = [pick_card(deck)]
    dealer_hand = [pick_card(deck)]
    done = False
    player_hand = player_phase(player_hand, deck)
    player_score = score_hand(player_hand)
    if len(player_hand) == 2 and player_score == 21:
        return "Blackjack! You win!"
    if player_score >= 21:
        return "Busted! You lose!"
    dealer_hand = dealer_phase(dealer_hand, deck)
    dealer_score = score_hand(dealer_hand)
    if dealer_score > 21:
        return "Dealer busted! You win!"
    if player_score > dealer_score:
        return "You win!"
    if player_score < dealer_score:
        return "You lose!"
    return "It's a draw!"

def player_phase(hand, deck, dealer_hand):
    done = False
    while(not done):
        new_card = pick_card(deck)
        hand.append(new_card)
        score = score_hand(hand)
        print(f"You currently have the following cards: {display_hand(hand)}")
        print(f"The dealer has the following cards: {display_hand(hand)}, *")
        print(f"Your hand total is: {score}")
        if score >= 21:
            done = True
        else:
            input_value = 'c'
            while(input_value != 'h' and input_value != 'f'):
                input_value = input("Do you want to hit or fold? Press 'h' to hit or 'f' to fold. ").lower()
            done = input_value == 'f'
    return hand

def dealer_phase(hand, deck):
    done = False
    while(not done):
        new_card = pick_card(deck)
        hand.append(new_card)
        score = score_hand(hand)
        print(f"The dealer currently has the following cards: {display_hand(hand)}")
        print(f"Their hand total is: {score}")
        if score >= 17:
            done = True
    return hand

def pick_card(deck):
    return random.choice(deck)

def display_hand(hand):
    return ", ".join(map(str, hand))

def score_hand(hand):
    base_score = sum(hand)
    aces_count = len(tuple(filter(lambda x: x == 11, hand)))
    while base_score > 21 and aces_count > 0:
        base_score -= 10
        aces_count -= 1
    return base_score
