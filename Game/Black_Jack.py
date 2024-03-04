# JP0030

import random
import tkinter
from tkinter.font import BOLD

def getCardImages(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    faceCards = ['jack', 'queen', 'king']

    ext= 'png'
    for suit in suits:
        for card in range(1, 11):
            name = 'C:/Users/DELL/Downloads/cards/{}_{}.{}'.format(str(card), suit, ext)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, ))

        for card in faceCards:
            name = 'C:/Users/DELL/Downloads/cards/{}_{}.{}'.format(str(card), suit, ext)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image, ))


def getCard(frame):
    next_card = deck.pop(0) 
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card

def calcScore(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score

def staying():
    dealer_score = calcScore(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(getCard(dealer_cardFrame))
        dealer_score = calcScore(dealer_hand)
        dealerScore.set(dealer_score)

    player_score = calcScore(player_hand)
    if player_score > 21 or dealer_score > player_score:
        winner.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        winner.set("Player wins!")
    else:
        winner.set("Draw!")