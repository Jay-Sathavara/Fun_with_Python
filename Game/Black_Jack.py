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

def hitting():
    player_hand.append(getCard(player_card_frame))
    player_score = calcScore(player_hand)

    playerScore.set(player_score)
    if player_score > 21:
        winner.set("Dealer Wins!")


def initial_deal():
    hitting()
    dealer_hand.append(getCard(dealer_cardFrame))
    dealerScore.set(calcScore(dealer_hand))
    hitting()


def new_game():
    global dealer_cardFrame
    global player_card_frame
    global dealer_hand
    global player_hand
    dealer_cardFrame.destroy()
    dealer_cardFrame = tkinter.Frame(gameWindow, bg="black")
    dealer_cardFrame.place(x=100,y=80)
    
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(gameWindow, bg="black")
    player_card_frame.place(x=100,y=200)

    winner.set("")

    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    random.shuffle(deck)

gameWindow = tkinter.Tk()

gameWindow.title("DataFlair Black Jack")
gameWindow.geometry("640x480")

tkinter.Label(gameWindow, text='DataFlair Black Jack',
      fg='black', font=('Courier', 20,BOLD)).place(x=150, y=10)

winner=tkinter.StringVar()
result = tkinter.Label(gameWindow, textvariable=winner,fg='black',font=('Courier', 15))
result.place(x=250,y=50)

dealerScore = tkinter.IntVar()
tkinter.Label(gameWindow, text="Dealer Score:", fg="black",bg="white").place(x=10,y=80)
tkinter.Label(gameWindow, textvariable=dealerScore, fg="black",bg="white").place(x=10,y=100)
dealer_cardFrame = tkinter.Frame(gameWindow, bg="black")
dealer_cardFrame.place(x=100,y=80)

playerScore = tkinter.IntVar()

tkinter.Label(gameWindow, text="Player Score:", fg="black",bg="white").place(x=10,y=200)
tkinter.Label(gameWindow, textvariable=playerScore,fg="black",bg="white").place(x=10,y=220)
player_card_frame = tkinter.Frame(gameWindow, bg="black")
player_card_frame.place(x=100,y=200)

