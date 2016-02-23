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
    family=['Heart','Spades','Clubs','Diamond']
    #color['heart','diamond']="red"
    #color['space','claver']="black"
    number=['Ace','King','Queen','Jack',"Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    deck={}
    card={}

    deck=[[a,b] for a in family for b in number]

        #print deck

    return deck

def userChoice():
    choice=raw_input("Choose 4 numbers (1-52) with space between each number: ")
    option=choice.split(" ")
    return option

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
    deck=deckOfCards()
    #print deck
    card=generateNumberforCard(deck)
    option=userChoice()
    #print option
    shuffledCard = shuffle_card(card)
    for i in option:
        selectedCard.append(shuffledCard[int(i)])

    print "Your Cards are: "
    printSelectedCard(selectedCard)
    isWinner(selectedCard)
if __name__ == '__main__':
    main()
