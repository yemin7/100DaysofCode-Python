from random import choice
import art

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

jqka = {
       'A': 11, 'J': 10, 'Q': 10, 'K': 10
       }

def deal_card():
    card = choice(cards)
    return card

def sum_card(card):
    for i in card:
        if i in jqka.keys():
            to_delete = card.index(i)
            card[to_delete] = jqka[i]
    return sum(card)

def condition_21(dealer, player):
    if player == 21 and dealer != 21:
        return ('\33[93m'+ 'BLACKJACK' + '\33[0m' +'\nYou Win!')
    elif (dealer > player and dealer < 21) or player > 21 or dealer == 21:
        return "Dealer Win"
    elif dealer == player:
        return "Push"
    else:
        return "You Win."

def not_21(card):
    if card == 21 or card > 21:
        return False
    else:
        return True

def blackjack():
    print(art.logo)
    not_finished = True
    dealer_cards = [deal_card() for _ in range(2)]
    player_cards = [deal_card() for _ in range(2)]
    dealer_cards_copy = dealer_cards.copy()
    hide_dealer_card = dealer_cards.copy()
    hide_dealer_card[1] = '❔'
    player_cards_copy = player_cards.copy()
    
    sum_dealer_cards = sum_card(dealer_cards_copy)
    sum_player_cards = sum_card(player_cards_copy)

    print(f"Dealer cards {hide_dealer_card}")
    print(f"Player cards {player_cards}, current score: {sum_player_cards}")
    
    while not_finished:

        if sum_player_cards == 21: not_finished = False

        draw_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()

        if draw_card == 'y':
            card = deal_card()
            player_cards.append(card)
            if card == 'A': card = 1
            player_cards_copy.append(card)
            sum_player_cards = sum_card(player_cards_copy)
            not_finished = not_21(sum_player_cards)
            print(f"Dealer cards {hide_dealer_card}")
            print(f"Player cards {player_cards}, current score: {sum_player_cards}")

        elif draw_card == 'n':
            while sum_dealer_cards < sum_player_cards and sum_dealer_cards < 17:
                card = deal_card()
                dealer_cards.append(card)
                if card == 'A': card = 1
                dealer_cards_copy.append(card)
                sum_dealer_cards = sum_card(dealer_cards_copy)
            not_finished = False
    print(f"\nDealer cards {dealer_cards}, final score: {sum_dealer_cards}")
    print(f"Player cards {player_cards}, final score: {sum_player_cards}")
    print(condition_21(sum_dealer_cards, sum_player_cards))

    result = input("\nDo you want to play again? (y/n)").lower()
    if result == 'y':
        art.clear()
        blackjack()
    else:
        return

blackjack()