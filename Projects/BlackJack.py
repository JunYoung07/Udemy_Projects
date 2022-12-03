############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# index = random.randint(0, 10)
user = [cards[random.randint(0, len(cards)-1)], cards[random.randint(0, len(cards)-1)]]
comp = [cards[random.randint(0, len(cards)-1)]]

print('Your card: ', user)
print("Dealer's card: ", comp)

# Your Turn
while True:
    cont = input('Hit or Stay(H/S): ')
    if cont == 'H':
        user.append(cards[random.randint(0, len(cards)-1)])
        if sum(user) > 21:
            if 11 in user:
                user[user.index(11)] = 1
                print('Your card: ', user)
            else:
                print('Your card: ', user)
                print('You Lose')
                break
        else:
            print('Your card: ', user)
    elif cont == 'S':
        break
    else:
        cont = int('Hit or Stay')

# Dealer Turn
# Computer should have larger than 17
while True:
    comp.append(cards[random.randint(0, len(cards)-1)])
    if sum(comp) > 21:
        if 11 in comp:
            user[user.index(11)] = 1
            print('Dealer\'s card: ', comp)
        else:
            print('Dealer\'s card: ', comp)
            print('You win')
        break
    elif sum(comp) > sum(user):
        print('Dealer\'s card: ', comp)
        print('Dealer win')
        break
    elif sum(comp) == sum(user):
        print('Dealer\'s card: ', comp)
        print('Draw')
        break
    elif sum(comp) >= 21 and sum(comp) < sum(user):
        comp.append(cards[random.randint(0, len(cards)-1)])
        print('Dealer\'s card: ', comp)
    elif sum(user) > 21:
        print('Dealer\'s card: ', comp)
        break


