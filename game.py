import random


class Card:
    def __init__(self, colour, figure):
        self.__figure = figure
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def getFigure(self):
        return self.__figure


class Game:
    deck = []
    gameDeck = []
    playerCards = []
    computerCards = []
    colours = ['♣', '♦', '♥', '♠']
    figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    playerMoney = 0
    bet = 0
    response = ''

    def __init__(self):
        self.createDeck()
        self.playerMoney = 1000

    def createDeck(self):
        for colour in self.colours:
            for figure in self.figures:
                self.deck.append(Card(colour, figure))

    def getGameDeck(self):
        self.gameDeck = list.copy(self.deck)
        random.shuffle(self.gameDeck)
        self.playerCards = []
        self.computerCards = []

    def setBet(self):
        betSet = True
        print('Players money: ' + str(self.playerMoney) + '$')
        while betSet:
            playerBet = int(input("How much do you want to play? "))
            if ((self.playerMoney - playerBet) >= 0):
                self.bet += playerBet
                betSet = False
                print('Deal!')
            else:
                print("You don't have that much money. Bet for less or go away")

    def sumScore(self, cards):
        sum = 0
        ace = 0
        for card in cards:
            if card.getFigure() in ['J', 'Q', 'K']:
                sum += 10
            elif card.getFigure() is 'A':
                ace += 1
            else:
                sum += int(card.getFigure())
        if ace != 0:
            if ace - 1 + 11 + sum < 22:
                return ace - 1 + 11 + sum
            else:
                return ace + sum
        return sum

    def printCards(self, cards, flag):
        for card in cards[flag:]:
            print(card.getFigure() + ' ' + card.getColour(), end=' | ')

    def mainGame(self):
        gameOn = 'y'
        while gameOn is not 'q':  # Loop for new gameplay
            self.getGameDeck()
            self.setBet()
            for i in range(2):
                self.playerCards.append(self.gameDeck.pop())
                self.computerCards.append(self.gameDeck.pop())
            end = False
            while not end:  # Loop for ongoing gameplay
                print('Player Cards')
                self.printCards(self.playerCards, 0)
                playerScore = self.sumScore(self.playerCards)
                print('Sum of player cards: ' + str(playerScore))
                print('Computer cards:')
                print('X | ', end=' ')
                self.printCards(self.computerCards, 1)
                print()
                if playerScore >= 21:
                    end = True
                else:
                    hit = input('Hit? y - yes || s - stop  ')
                    if hit == 'y':
                        self.playerCards.append(self.gameDeck.pop())
                    else:
                        end = True

            while playerScore < 22 and self.sumScore(self.computerCards) < 17:
                self.computerCards.append(self.gameDeck.pop())

            print('Computer Cards')
            self.printCards(self.computerCards, 0)
            computerScore = self.sumScore(self.computerCards)
            print('Sum of computer cards: ' + str(computerScore))

            if (22 > playerScore > computerScore) or (playerScore < 22 <= computerScore):
                print("You win!")
                self.playerMoney += self.bet
            elif (22 > computerScore > playerScore) or (computerScore < 22 <= playerScore):
                print("You lose!")
                self.playerMoney -= self.bet
            else:
                print("Draw!")

            print('You have ' + str(self.playerMoney) + '$')
            self.bet = 0
            if self.playerMoney == 0:
                print("Game over looser")
                gameOn = 'q'
            else:
                gameOn = input('Again? y - yes || q - quit  ')


gameActive = Game()
gameActive.mainGame()
