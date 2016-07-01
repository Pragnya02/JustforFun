'''
Card game
Every card selections will be based on a key (number) assigned to each card
Level 1:
Select three cards
If 3 cards are of the same family - pass level 1
else ask user to guess a riddle to go to the next level.
If user gueses right level passed. Else 1 life gone - start all over again. Game ends if you loose 3 lives.

Level 2:
User gets 10 chances to select pairs per chance out of the deck of cards.
For every game/chance the two cards selected will not be shown, point will increase if they are pairs,
else points remain the same. After every game the pairs chosen will be removed from the deck of cards.
She/He shoudl have won atleast 1 game more than the threshold score calculated to go to the next game.
Else go back to previous level

Threshold score calculation: The first card that you score for is noted, and its face value is the score
you have got to compete!


Level 3:
From the remaining cards from level 2 (30 cards) take 1 card but you wont know what that card is.
You will have 7 chances to inbetween which you can opt to see the pivot card,
but once you do this you won't be able to play further.
At the end of 7 games you for every card you selected if the face value of the card is > the face value of pivot card,
you wont that game, else you lost.
Total number of games won is this round should be at least two greater than your
counterpart computer score!
'''

'''
Required functions/methods
card class:
shuffle()
play game class:
level1() level2() level3()
computer_plays
score_for_Level2()

General:
players_total_score
lifecount
set of riddles with answer

'''

'''
GOAL : Use concepts of Inheritance , Class, function , multi threading
'''
from random import shuffle
from random import randint
import random
import sys
deck={}
card={}

#This class would contain shuffle, card deck generation
class Card(object):
    def deck_Of_Cards(self):
        family=['Heart','Spades','Clubs','Diamond'] #Family of Cards
        number=['Ace','King','Queen','Jack',"Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
        deck=[[a,b] for a in family for b in number]
        #Call the generateNumberforCard to have a unique number for each card
        card  =  self.generate_Number_for_Card(deck)
        return card

    def shuffle_card(self,card):
        values=card.values()
        shuffle(values)
        shuffledCard=dict(zip(card.keys(),values))
        return shuffledCard

    #Generate a unique number for each card
    def generate_Number_for_Card(self,deck):
        for i in range(0,len(deck)):
            card[i]=deck[i]
        return card

#playGame class inherits Card class
class playGame(Card):
    selectedCard=[]
    life=3
    scoreComp=0
    def start_Game(self,card):
        card = cardDeck.deck_Of_Cards()
        card = cardDeck.shuffle_card(card)
        #print card
        print "\n You have started your game! Buckle up and let us test your memory!\n"
        print " This is a Card Game. You wont be seeing a card, but each number corresponds to a card!\n"
        print "Beware your cards are shuffled! Lets start now!! \n"

        enter = raw_input("Press Enter to continue\n")
        if not enter:
            self.level3(card)


        #compare User score and computer score



    def level1(self,card):
        #For level 1 n=3
        #print card
        chances=0
        score = 0
        choice="Y"
        print "This is level 1. Game Rules!"
        print "******************************"
        print self.game_rules(1)
        print "*********************************\n"

        print " Atleast 4 of your 5 cards shoudl be of the same family\n"
        while chances<10 and self.life!=0 and choice!="COMPLETE":
            choice = self.level1_Check(card)
            if choice=='R':
                answer=self.riddle()
                if answer==True:
                    print "YAY you passed this Riddle!!"
                    choice="COMPLETE"


                else:
                    print "Oops that was wrong again! You loose a life"
                    self.life=self.life-1
                    card = cardDeck.shuffle_card(card)

            else:
                card = cardDeck.shuffle_card(card)
                chances=chances+1
        print "CHOICE from LEVEL1 ",choice

        if choice=="COMPLETE":
            print "YAY you passed this level!!\n"
            enter = raw_input("Press enter to continue\n")
            if not enter:
                self.level2(cardDeck.shuffle_card(card))

        #return choice

    def level1_Check(self,card):
        lost=True
        option=self.userChoice(5)
        for i in option:
            self.selectedCard.append(card[int(i)])
        if len(set([k for k,v in self.selectedCard]))>4:
            lost=True
            choice=raw_input("OOPs bad luck! Do you want to Try again to answer a riddle to pass the level?!\n Type R for riddle! ")
        else:
            lost=False
            choice="COMPLETE"
        return choice

    def level2(self,card):
        #10 chances for user to sekect pair of cards
        score=0
        chance=10
        computerscore=0
        deletedCard=[]

        print "This is level 2. Game Rules!"
        print "******************************"
        print self.game_rules(2)
        print "*********************************\n"
        while chance>0:
            self.selectedCard=[]
            #Use Multithreading to make user and computer play together
            #This is users game
            option=self.userChoice(2)

            try:
                for i in option:
                    if i in deletedCard:
                        raise
            except:
                #sys.exit("I am sorry, you entered a number that has been removed off the deck! You need to have a better memory. Game Over!")
                print "I am sorry, you entered a number that has been removed off the deck! You need to have a better memory. \nGo back to level1!"
                score=0
                enter = raw_input("Press enter to continue\n")
                if not enter:
                    self.start_Game(card)
                break
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            for i in option:
                self.selectedCard.append(card[int(i)])

                #del card[int(i)]

                #use try catch to make sure the sae number isnt chosen again
            print [v for k,v in self.selectedCard]
            if len(set([v for k,v in self.selectedCard]))==1:
                lost=True
                score=score+1
                chance=chance+1
                if score==1:
                    computerscore= [int(v) for k,v in self.face_value(self.selectedCard).items()][0]

                    print computerscore
                for i in option:
                    deletedCard.append(i)
                    del card[int(i)]
            else:
                lost=False

            chance = chance-1



        if score > computerscore and score>0:
            print "\nYay! your score is",score
            print " And you've won the threshold score of", computerscore
            print "Congrats, you are goin to the next level!\n"
            enter = raw_input("Press enter to continue\n")
            if not enter:
                self.level3(card)
        elif score <= computerscore and score>0:
            print "OOPS your score is only",score
            print " You have to go back to level 1 because you haven't crossed the score of\n",computerscore
            card = cardDeck.deck_Of_Cards()
            enter = raw_input("Press enter to continue\n")
            if not enter:
                self.level1(cardDeck.shuffle_card(card))
        elif score==0:
            print "I am sorry you lost the game.\nYou've got to start from beginning.\n"
            enter = raw_input("Press enter to continue\n")
            if not enter:
                self.start_Game(card)


        #return score,computer score

    def checkCompScore(self,card):
        #Computer Selects two cards from 0-51 every game.
        a,b= random.sample(range(0,51),2)

        if card[int(a)]==card[int(b)]:
            self.scoreComp=self.scoreComp+1

        return self.scoreComp


    def level3(self,card):
        print "This is level 3. Game Rules!"
        print "******************************"
        print self.game_rules(3)
        print "*********************************\n"

        chance=0
        chosenCard=[]
        pivotCard=[]
        cardVal=[]
        print [k for k,v in card.items()]
        pivot = int(raw_input("Pick one card as a pivot "))
        print "Great! Your Pivot card has been chosen. Well you can't see it,\n but lets test your luck with the other 7 chances!"
        while chance<7:
            print "This is your",chance,"st/nd/rd choice! "
            val=int(raw_input("Select your card "))
            #Should check if the value chosen is from the list

            chosenCard.append(val)
            choice = raw_input("Do you want to see the Pivot and quit this game?(Y/N) ")
            if choice=='Y':
                print " You chose to end the game.\n"
                break
            chance=chance+1
        for i in chosenCard:

            cardVal.append(card[i])

        pivotCard.append(card[pivot])
        pivotVal = [v for k,v in self.face_value(pivotCard).items()][0]

        print "This is your Pivot card! : ",pivotCard," Its Face Value is",pivotVal," Lets see your luck now!\n"
        #print cardVal
        print self.face_value(cardVal)


    def riddle(self):
        print "This is a riddle!"
        riddle = {1:"What can travel around the world while staying in a corner?",
        2:"If you have me, you want to share me. If you share me, you havent got me. What am I?",
        3:"I run distances, often making many turns, yet I never move one foot. What am I?",
        4:"You answer me, although I never ask you questions. What am I?"
        }
        answers={1:"stamp",2:"secret",3:"watch",4:"phone"}
        number=randint(1,4)
        userAnswer= raw_input(riddle[number])
        if userAnswer.lower()==answers[number]:
            return True
        else:
            return False

    def game_rules(self,n):
        rules={1:"Level 1:\n\
        Select three cards\n\
        If 4 cards are of the same family - pass level 1\n\
        else ask user to guess a riddle to go to the next level.\n\
        If user gueses right level passed. Else 1 life gone - start all over again. Game ends if you loose 3 lives.",
        2: "User gets 10 chances to select pairs per chance out of the deck of cards.\n\
        For every game/chance the two cards selected will not be shown, point will increase if they are pairs,\n\
        else points remain the same. After every game the pairs chosen will be removed from the deck of cards\n\
        She/He shoudl have won atleast 1 game more than the threshold score calculated to go to the next game.\n\
        Else go back to previous level. Bonus chances to play for every score you get!\n\
        \n\
        Threshold score calculation: The first card that you score for is noted, and its face value is the \n\
        score you have got to compete!",
        3:"From the remaining cards from level 2 (30 cards) take 1 card but you wont know what that card is.\n\
        You will have 7 chances to inbetween which you can opt to see the pivot card,\n\
        but once you do this you won't be able to play further.\n\
        At the end of 7 games you for every card you selected if the face value of the card is > the face value of pivot card,\n\
        you wont that game, else you lost.\n\
        Total number of games won is this round should be at least two greater than your\n\
        counterpart computer score!"}

        return(rules[n])

    def user_Total_Score():
        pass

    def face_value(self,card):
        value={}
        number={'Ace':14,'King':13,'Queen':12,'Jack':11,"Ten":10,"Nine":9,"Eight":8,"Seven":7,"Six":6,"Five":5,"Four":4,"Three":3,"Two":2}
        for k,v in card:
            value[v]=number[v]
        return value

    def userChoice(self,n):
        choice=raw_input("Choose %s unique numbers (0-51) with space between each number: " %(n))
        option=choice.split(" ")
        while len(set(option))< n:
            print "Sorry you either chose the same card more than once or entered the wrong number of cards"
            choice=raw_input("Choose %s unique numbers (0-51) with space between each number: " %(n))
            option=choice.split(" ")
        return option

cardDeck = playGame()

cardDeck.start_Game(card)
'''
deck={}
card={}
def deckOfCards():
    family=['Heart','Spades','Clubs','Diamond'] #Family of Cards
    number=['Ace','King','Queen','Jack',"Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]

    deck=[[a,b] for a in family for b in number]
    return deck

def userChoice(n):
    choice=raw_input("Choose %d unique numbers (0-51) with space between each number: ",n)
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
    n=2
    option=userChoice(n)

    for i in option:
        selectedCard.append(shuffledCard[int(i)])

    print "The Cards you have chosen are: "

    #Print the cards you have chosen
    printSelectedCard(selectedCard)

    #Check if winner or not
    isWinner(selectedCard)
if __name__ == '__main__':
    main()
'''
