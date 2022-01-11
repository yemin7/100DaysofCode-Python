import random, os

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

## cards sum function
def cards_sum(card):
    sum = 0
    for i in card:
        if i == 'J' or i == 'Q' or i == 'K':
            sum += 10
        elif i == 'A':
            sum += 11
            if sum > 21:
                sum -= 10
        else:
            sum += i
    return sum

## Blackjack result function
def blackjack():
    finished, draw_card, above_21 = False, True, False
    while not finished: 
        dealer_cards = random.sample(cards, 2)      #2 random cards to dealer
        player_cards = random.sample(cards, 2)      #2 random cards to player
        player_cards_copy = player_cards.copy()     #store initial cards of player
        dealer_cards_copy = dealer_cards.copy()     #store initial cards of dealer
        hide_dealer_cards = dealer_cards.copy()     #copy dealer cards to hide 2nd card
        hide_dealer_cards[1] = '❔'                 #hid delear 2nd card
        
        dealer_sum = cards_sum(dealer_cards)        #sum of dealer cards
        player_sum = cards_sum(player_cards)        #sum of player cards
    

        if player_sum == 21 and dealer_sum != 21:   #Player Blackjack and another game
            print (f">\tYour cards: {player_cards}, current score: {player_sum}")
            print (f">\tDealer's cards: {dealer_cards}, dealer's score: {dealer_sum}")
            print('\33[93m'+ 'BLACKJACK' + '\33[0m' +'\nYou Win!')

        else:
            print (f">\tYour cards: {player_cards}, current score: {player_sum}")
            print (f">\tDealer's cards: {hide_dealer_cards}")

            while draw_card:
                hit = input("\nType 'y' to get another card, type 'n' to pass: ").lower()

                if hit == 'y':
                    another_card = random.sample(cards,1)                           #player draw another card
                    player_cards_copy += another_card                               #store the card to player initial cards store
    
                    return_card = cards_sum(another_card)                           #sum of player cards
                    if return_card == 11 and (player_sum + return_card) > 21:       #change ace 'A' value to '1' of next draw
                        return_card = 1
                    player_sum += return_card

                    if player_sum == 21:                                            #Player Blackjack
                        draw_card = False
        
                    elif player_sum > 21:                                           #Player bust
                        above_21 = True
                        draw_card = False
                    print (f">\tYour cards: {player_cards_copy}, current score: {player_sum}")      #output player cards result

                elif hit == 'n':
                    while (dealer_sum < player_sum) and dealer_sum < 16:                            #dealer draw another card if the player stand
                        dealer_another_card = random.sample(cards,1)
                        dealer_cards_copy += dealer_another_card
                        
                        return_card = cards_sum(dealer_another_card)
                        if return_card == 11 and (dealer_sum + return_card) > 21:               
                            return_card = 1
                        dealer_sum +=return_card
                        print(f">\tDealer draw a card: {dealer_another_card}")
                    draw_card = False
    
                    print (f">\tDealer's cards: {dealer_cards_copy}, dealer's score: {dealer_sum}") #output dealer cards result
    
            if dealer_sum == 21:
                print("Dealer Win.")
            elif above_21:
                print (f">\tDealer's cards: {dealer_cards}, dealer's score: {dealer_sum}")
                print("Dealer Win.")
                above_21 = False
            elif player_sum == 21:
                print('\33[93m'+ 'BLACKJACK' + '\33[0m' +'\nYou Win!')
            elif  dealer_sum > player_sum and dealer_sum < 21:                  #if delear cards result is not blackjack and greater than player's result, dealer win
                print("Dealer Win.")
            elif dealer_sum == player_sum:
                print("Push!")
            else:
                print("You Win.")
    
        result = input("\nDo you want to play again? (y/n)").lower()
        if result == 'y':
            finished = True
            os.system("clear")
            blackjack()
        if result == 'n':
            finished = True
        os.system("clear")

blackjack()