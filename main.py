from random import randint
#from tkinter import *
import tkinter as tk

deck = ['2', '3','4', '5', '6','7', '8', '9','10', 'J', 'Q','K', 'A']
PLAYERS_CARDS = []
PLAYERS_TOTAL = -1
DEALERS_TOTAL = -1
DEALERS_VISIBLE = -1
has_pair = None
TOTAL_PLAYED = 0
TOTAL_CORRECT = 0

def drawCard():
    rand = randint(0, 12)
    return deck[rand]

def getValue(card):
    if card == '1':
        return 1
    elif card == '2':
        return 2
    elif card == '3':
        return 3
    elif card == '4':
        return 4
    elif card == '5':
        return 5
    elif card == '6':
        return 6
    elif card == '7':
        return 7
    elif card == '8':
        return 8
    elif card == '9':
        return 9
    elif card == '10':
        return 10
    elif card == 'J':
        return 10
    elif card == 'Q':
        return 10
    elif card == 'K':
        return 10
    elif card == 'A':
        return 11

def checkSoftTotals():
    if PLAYERS_TOTAL == 20:
        return 'stand'
    elif PLAYERS_TOTAL == 19:
        if DEALERS_VISIBLE == 6:
            return 'double'
        else:
            return 'stand'
    elif PLAYERS_TOTAL == 18:
        if DEALERS_VISIBLE >= 9:
            return 'hit'
        elif DEALERS_VISIBLE <= 6:
            return 'double'
        else:
            return 'stand'
    elif PLAYERS_TOTAL == 17:
        if bool(DEALERS_VISIBLE == 13) | bool(DEALERS_VISIBLE == 14) | bool(DEALERS_VISIBLE == 15) | bool(DEALERS_VISIBLE == 16):
            return 'double'
        else:
            return 'hit'
    elif PLAYERS_TOTAL == 16:
        if bool(DEALERS_VISIBLE == 14) | bool(DEALERS_VISIBLE == 15) | bool(DEALERS_VISIBLE == 16):
            return 'double'
        else:
            return 'hit'
    elif PLAYERS_TOTAL == 15:
        if bool(DEALERS_VISIBLE == 14) | bool(DEALERS_VISIBLE == 15) | bool(DEALERS_VISIBLE == 16):
            return 'double'
        else:
            return 'hit'
    elif PLAYERS_TOTAL == 14:
        if bool(DEALERS_VISIBLE == 15) | bool(DEALERS_VISIBLE == 16):
            return 'double'
        else:
            return 'hit'
    elif PLAYERS_TOTAL == 13:
        if bool(DEALERS_VISIBLE == 15) | bool(DEALERS_VISIBLE == 16):
            return 'double'
        else:
            return 'hit'

def checkHardTotals():
    if PLAYERS_TOTAL >= 17:
        return 'stand'
    elif bool(PLAYERS_TOTAL == 16) | bool(PLAYERS_TOTAL == 15) | bool(PLAYERS_TOTAL == 14) | bool(PLAYERS_TOTAL == 13):
        if DEALERS_VISIBLE <= 6:
            return 'stand'
        else:
            return 'hit'
    elif PLAYERS_TOTAL == 12:
        if bool(DEALERS_VISIBLE == 4) | bool(DEALERS_VISIBLE == 5) | bool(DEALERS_VISIBLE == 6):
            return 'stand'
        else:
            return 'hit'
    elif PLAYERS_TOTAL == 11:
        return 'double'
    elif PLAYERS_TOTAL == 10:
        if DEALERS_VISIBLE <= 9:
            return 'double'
        else:
            return 'hit'
    elif PLAYERS_TOTAL == 9:
        if bool(DEALERS_VISIBLE == 3) | bool(DEALERS_VISIBLE == 4) | bool(DEALERS_VISIBLE == 5) | bool(DEALERS_VISIBLE == 6):
            return 'double'
        else:
            return 'hit'
    elif PLAYERS_TOTAL <= 8:
        return 'hit'

def checkSplit(c):
    if c == 'A':
        return True
    elif c == '10':
        return False
    elif c == '9':
        if bool(DEALERS_VISIBLE == 11) | bool(DEALERS_VISIBLE == 10) | bool(DEALERS_VISIBLE == 7):
            return False
        else:
            return True
    elif c == '8':
        return True
    elif c == '7':
        if DEALERS_VISIBLE <= 7:
            return True
        else:
            return False
    elif c == '6':
        if DEALERS_VISIBLE <= 6:
            return True
        else:
            return False
    elif c == '5':
        return False
    elif c == '4':
        if bool(DEALERS_VISIBLE == 5) | bool(DEALERS_VISIBLE == 6):
            return True
        else:
            return False
    elif c == '3':
        if DEALERS_VISIBLE <= 7:
            return True
        else:
            return False
    elif c == '2':
        if DEALERS_VISIBLE <= 7:
            return True
        else:
            return False

def hasPair(cards):
    if cards[0] == cards[1]:
        return True
    else:
        return False

def hasAce(cards):
    for card in cards:
        if card == 'A':
            return True
    return False

def press(button):
    correct = None
    if hasPair(PLAYERS_CARDS):
        if checkSplit(PLAYERS_CARDS[0]):
            correct = 'split'
        else:
            if hasAce(PLAYERS_CARDS):
                correct = checkSoftTotals()
            else:
                correct = checkHardTotals()
    else:
        if hasAce(PLAYERS_CARDS):
            correct = checkSoftTotals()
        else:
            correct = checkHardTotals()

    if bool(correct == 'split') & bool(button == 'P'):
        response('correct', correct)
    elif bool(correct == 'hit') & bool(button == 'H'):
        response('correct', correct)
    elif bool(correct == 'stand') & bool(button == 'S'):
        response('correct', correct)
    elif bool(correct == 'double') & bool(button == 'D'):
        response('correct', correct)
    else:
        response('incorrect', correct)

    print("pressed")

def response(res, answer):
    global TOTAL_PLAYED
    global TOTAL_CORRECT
    TOTAL_PLAYED += 1
    if res == 'correct':
        TOTAL_CORRECT += 1
        correctText = tk.Label(text=f"Correct", foreground='green')
        correctText.grid(row=2, column=0)
        answerText = tk.Label(text=f"{answer}", foreground='green')
        answerText.grid(row=2, column=1)
    else:
        incorrectText = tk.Label(text=f"Inorrect", foreground='red')
        incorrectText.grid(row=2, column=0)
        answerText = tk.Label(text=f"{answer}", foreground='green')
        answerText.grid(row=2, column=1)
    countText = tk.Label(text=f"{TOTAL_CORRECT}/{TOTAL_PLAYED}")
    countText.grid(row=2, column=2)
    playGame()

def playGame():

    #Deal Players Cards & Calculate Total
    global PLAYERS_CARDS
    card = drawCard()
    PLAYERS_CARDS = [drawCard(), drawCard()]
    playersValue = [getValue(PLAYERS_CARDS[0]), getValue(PLAYERS_CARDS[1])]
    global PLAYERS_TOTAL
    PLAYERS_TOTAL = sum(playersValue)
    if bool(PLAYERS_TOTAL > 21) & hasAce(PLAYERS_CARDS):
        PLAYERS_TOTAL -= 10

    #Deal Dealers Cards & Calculate Total
    dealersCards = [drawCard(), drawCard()]
    dealersValue = [getValue(dealersCards[0]), getValue(dealersCards[1])]
    global DEALERS_TOTAL
    DEALERS_TOTAL = sum(dealersValue)
    global DEALERS_VISIBLE
    DEALERS_VISIBLE = dealersValue[0]

    #Display Dealers Cards & Total
    dealerText = tk.Label(text=f"Dealer's\nCards")
    dealerText.grid(row=0, column=0)
    dealerCard1 = tk.Label(text=dealersCards[0])
    dealerCard1.grid(row=0, column=1)
    dealerCard2 = tk.Label(text="?")
    dealerCard2.grid(row=0, column=2)
    dealerTot = tk.Label(text=str(DEALERS_VISIBLE))
    dealerTot.grid(row=0, column=3)

    #Display Players Cards & Total
    playerText = tk.Label(text=f"Player's\nCards")
    playerText.grid(row=1, column=0)
    playerCard1 = tk.Label(text=PLAYERS_CARDS[0])
    playerCard1.grid(row=1, column=1)
    playerCard2 = tk.Label(text=PLAYERS_CARDS[1])
    playerCard2.grid(row=1, column=2)
    playerTot = tk.Label(text=str(PLAYERS_TOTAL))
    playerTot.grid(row=1, column=3)

    print("Player's Cards: " + PLAYERS_CARDS[0] + " " + PLAYERS_CARDS[1])
    print("Player's Total: " + str(PLAYERS_TOTAL))

    print("Dealer's Cards: " + '?' + " " + dealersCards[0])
    print("Dealer's Total: " + str(DEALERS_VISIBLE))

if __name__ == '__main__':
    gui = tk.Tk()
    gui.configure(background="green")
    gui.title("Blackjack")
    gui.geometry("300x300")

    for i in range(4):
        gui.columnconfigure(i, weight=1, minsize=50)
        gui.rowconfigure(i, weight=1, minsize=50)

        for j in range(0, 4):
            frame = tk.Frame(
                master=gui,
                relief=tk.RAISED,
                borderwidth=0
            )
            frame.grid(row=i, column=j)

            if i == 3:
                if j == 0:
                    hitButton = tk.Button(frame, text='Hit', command=lambda: press("H"), height=1, width=8)
                    hitButton.pack()
                elif j == 1:
                    standButton = tk.Button(frame, text='Stand', command=lambda: press("S"), height=1, width=8)
                    standButton.pack()
                elif j == 2:
                    doubleButton = tk.Button(frame, text='Double', command=lambda: press("D"), height=1, width=8)
                    doubleButton.pack()
                elif j == 3:
                    splitButton = tk.Button(frame, text='Split', command=lambda: press("P"), height=1, width=8)
                    splitButton.pack()

    playGame()


    gui.mainloop()
