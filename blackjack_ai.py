import random

# Define the card values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Create a deck of cards
def create_deck():
    deck = list(CARD_VALUES.keys()) * 4
    random.shuffle(deck)
    return deck

# Calculate the score of a hand
def calculate_score(hand):
    score = sum(CARD_VALUES[card] for card in hand)
    aces = hand.count('A')
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

# AI's decision-making process
def ai_decision(hand, dealer_card):
    score = calculate_score(hand)
    if score <= 11:
        return 'hit'
    elif score >= 17:
        return 'stand'
    elif dealer_card in ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        if score <= 16:
            return 'hit'
    return 'stand'

# Main game function
def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print(f"Your hand: {player_hand}, Score: {calculate_score(player_hand)}")
    print(f"Dealer's visible card: {dealer_hand[0]}")

    # AI plays its turn
    while True:
        decision = ai_decision(player_hand, dealer_hand[0])
        if decision == 'hit':
            player_hand.append(deck.pop())
            print(f"AI hits: {player_hand}, Score: {calculate_score(player_hand)}")
            if calculate_score(player_hand) > 21:
                print("AI busts! Dealer wins.")
                return
        else:
            print(f"AI stands with: {player_hand}, Score: {calculate_score(player_hand)}")
            break

    # Dealer plays
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print(f"Dealer's hand: {dealer_hand}, Score: {calculate_score(dealer_hand)}")

    # Determine winner
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21 or player_score > dealer_score:
        print("AI wins!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_blackjack()
