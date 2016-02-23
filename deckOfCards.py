'''
******DECK OF CARDS****
*Player randomly selects 4 Card, if it is of the same number- prints Winner
*@author: PRAGNYA SRINIVASAN
*pragnya.srini@gmail.com
'''
from random import shuffle

deck={}
card={}
def deckOfCards():
    family=['Heart','Spades','Clubs','Diamond'] #Family of Cards
    number=['Ace','King','Queen','Jack',"Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]

    deck=[[a,b] for a in family for b in number]
    return deck

def userChoice():
    choice=raw_input("Choose 4 unique numbers (0-51) with space between each number: ")
    option=choice.split(" ")
    return option

#Generate a unique number for each card
def generateNumberforCard(deck):
    for i in range(0,len(deck)):
        card[i]=deck[i]
    return card

def shuffle_card(card):
    values=card.values()
    shuffle(values)
    shuffledCard=dict(zip(card.keys(),values))
    return shuffledCard

def printSelectedCard(selectedCard):
    for i in selectedCard:
        print 3*" ",i[1],"of",i[0]
    print " "

def isWinner(selectedCard):
    number=[]
    for x in selectedCard:
        n=x
        number.append([y.split(',') for y in n][1])

    x=number[0]
    number.remove(x)
    if len(number)==0:
        print "YAY! YOU WON"
    else:
        print "OOPS! YOU LOST!"

def main():
    print " "
    selectedCard=[]
    #Stores Deck of Cards
    deck=deckOfCards()

    #Creates a number for Deck of Cards
    card=generateNumberforCard(deck)

    #Shuffle the cards
    shuffledCard = shuffle_card(card)

    #Takes in User Options (4 numbers)
    option=userChoice()

    for i in option:
        selectedCard.append(shuffledCard[int(i)])

    print "The Cards you have chosen are: "

    #Print the cards you have chosen
    printSelectedCard(selectedCard)

    #Check if winner or not
    isWinner(selectedCard)
if __name__ == '__main__':
    main()
