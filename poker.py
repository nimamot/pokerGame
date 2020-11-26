#Simulated basic poker game written with python by Nima Motieifard.
import random
import time
from time import sleep
import sys

def drawcards():
    """Draw the cards"""
    num1 = random.randint(2, 14)
    num2 = random.randint(2, 14)
    if num1 >= num2:
        card1 = num1
        card2 = num2
    else:
        card1 = num2
        card2 = num1
    return [card1, card2]


def card2str(card):
    """Converts the cards to String type"""
    if 10 >= card >= 2:
        card = str(card)
    elif card == 11:
        card = "J"
    elif card == 12:
        card = "Q"
    elif card == 13:
        card = "K"
    elif card == 14:
        card = "A"
    return card


def printhand(card1, card2, player):
    """printing out the cards"""
    print(f"[{card1}] [{card2}] {player}")


def printoutcome(cC, cC2, uC, uC2):
    """responsible for most of the logic of the project"""
    if cC > cC2:
        highestComputerCard = cC
        secondHeighestCumputer = cC2
    elif cC2 > cC:
        highestComputerCard = cC2
        secondHeighestCumputer = cC
    else:
        # we have a Tie
        highestComputerCard = cC2
        secondHeighestCumputer = cC2

    if uC > uC2:
        highestUserCard = uC
        secondHighestUserCard = uC2
    elif uC2 > uC:
        highestUserCard = uC2
        secondHighestUserCard = uC
    else:
        # We have a tie
        highestUserCard = uC2
        secondHighestUserCard = uC2
    # pairs
    if cC == cC2 and uC == uC2:
        if cC > uC:
            winner = cC
        elif uC > cC:
            winner = uC
        else:
            winner = "Tie"
    elif cC == cC2 or uC == uC2:
        if cC == cC2:
            winner = cC
        else:
            winner = uC

    # No pairs
    else:
        if highestComputerCard > highestUserCard:
            winner = cC
        elif highestUserCard > highestComputerCard:
            winner = uC
        else:
            if secondHeighestCumputer > secondHighestUserCard:
                winner = cC
            elif secondHighestUserCard > secondHeighestCumputer:
                winner = uC
            else:
                winner = "Tie"

    if winner == cC:
        losePrint = "YOU LOSE, better luck next time..."
        for i in range(len(losePrint)):
            print(losePrint[i], sep = " ", end = " ", flush=True); sleep(0.15)
        print("\n")
    elif winner == uC:
        winPrint = "YOU WIN"
        for i in range(len(winPrint)):
            print(winPrint[i], sep = " ", end = " ", flush=True); sleep(0.15)
        print("\n")
    else:
        print("Tie")

def main():
    loading = "<< GENERATING CARDS... >>"
    for i in range(len(loading)):
        print(loading[i], sep = " ", end = " ", flush=True); sleep(0.15)
    print("\n")
    computerCard = drawcards()
    userCard = drawcards()
    cC = card2str(computerCard[0])
    cC2 = card2str(computerCard[1])
    uC = card2str(userCard[0])
    uC2 = card2str(userCard[1])
    printhand(cC, cC2, "COMPUTER'S CARD")
    sleep(0.75)
    printhand(uC, uC2, "YOUR CARD")
    sleep(0.73)
    print("\n")
    printoutcome(computerCard[0], computerCard[1], userCard[0], userCard[1])

    playAgain = input("play again?(y/n): ")
    while playAgain.upper() == "Y":
        main()
        break
print("-----")
print("-----------")
print("            Welcome to the Amazing Poker Game")
print("-----------")
print("-----")

main()
