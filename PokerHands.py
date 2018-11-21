from enum import Enum


class Card:
    def __init__(self, rank, suit):
        self.suit = suit  # suit is an int from 1-13
        self.rank = rank  # rank is a string of ['hearts', 'diamonds', 'clubs', 'spades']


class Hand:
    def __init__(self, cards):
        self.cards = cards  # list of cards of type card

    def contains(self, value):
        """returns true if this hand contains a card with this number on it"""
        for card in self.cards:
            if card.rank == value:
                return True
        return False

    def handString(self):
        """returns a string of the hand for easy printing"""
        returnString = ''
        for card in self.cards:
            returnString += '\n'
            returnString += str(card.rank) + ' of ' + card.suit
        return returnString


class PokerHands(Enum):
    RoyalFlush = 10
    StraightFlush = 9
    FourOfAKind = 8
    FullHouse = 7
    Flush = 6
    Straight = 5
    ThreeOfAKind = 4
    TwoPair = 3
    Pair = 2
    HighCard = 1


def getTexasHoldEmHand(cardA, cardB, hand):
    """This will return the poker hand given by a texas hold em play of 2 given cards, and 'hand' on the table"""
    bestHand = Hand([cardA, cardB, hand.cards[0], hand.cards[1], hand.cards[2]])
    for i in range(0, len(hand.cards)):
        for j in range(0, len(hand.cards)):
            for k in range(0, len(hand.cards)):
                if i == j or i == k or j == k:
                    continue
                newHand = Hand([cardA, cardB, hand.cards[i], hand.cards[j], hand.cards[k]])
                if compareTwoHands(newHand, bestHand):
                    bestHand = newHand

    return bestHand


def compareTwoHands(handA, handB):
    """Returns true if handA wins and false if handB wins. returns None if the pot is split"""
    if pokerHand(handA).value > pokerHand(handB).value:
        return True
    if pokerHand(handB).value > pokerHand(handA).value:
        return False

    return tieBreak(handA, handB)


def tieBreak(handA, handB):
    """Breaks ties between hands if they are of the same type"""
    tiedPokerHand = pokerHand(handA)
    if tiedPokerHand == PokerHands.RoyalFlush:  # Royal Flushes are always ties
        return None
    elif tiedPokerHand == PokerHands.StraightFlush:
        return resolveStraight(handA, handB)
    elif tiedPokerHand == PokerHands.FourOfAKind:
        return resolveNOfAKind(handA, handB, 4)
    elif tiedPokerHand == PokerHands.FullHouse:
        return resolveFullHouse(handA, handB)
    elif tiedPokerHand == PokerHands.Flush:
        return resolveFlush(handA, handB)
    elif tiedPokerHand == PokerHands.Straight:
        return resolveStraight(handA, handB)
    elif tiedPokerHand == PokerHands.ThreeOfAKind:
        return resolveNOfAKind(handA, handB, 3)
    elif tiedPokerHand == PokerHands.TwoPair:
        return resolveTwoPair(handA, handB)
    elif tiedPokerHand == PokerHands.Pair:
        return resolveNOfAKind(handA, handB, 2)
    elif tiedPokerHand == PokerHands.HighCard:
        return resolveHighCard(handA, handB)


def resolveTwoPair(handA, handB):
    """Resolves the comparison of 2 hands if they are both two pair"""
    cardDictA = getAlikeCards(handA)
    cardDictB = getAlikeCards(handB)
    aTwosValue = getNumOfAKind(cardDictA, 2)
    bTwosValue = getNumOfAKind(cardDictB, 2)
    aTwosValue.sort(reverse=True)
    bTwosValue.sort(reverse=True)

    for i in range(0, len(aTwosValue)):
        if isLarger(aTwosValue[i], bTwosValue[i]) != None or i == len(aTwosValue):
            return isLarger(aTwosValue[i], bTwosValue[i])


def isLarger(a, b):
    """Given 2 ints, return true if a is larger than b if they are 2-13. ones are the highest. return none if the same"""
    if a > b:
        if b == 1:
            return False
        return True
    if b > a:
        if a == 1:
            return True
        return False
    return None


def resolveFullHouse(handA, handB):
    """Resolves the comparison of 2 hands if they are both full houses"""
    cardDictA = getAlikeCards(handA)
    cardDictB = getAlikeCards(handB)

    aThreesValue = getNumOfAKind(cardDictA, 3)
    bThreesValue = getNumOfAKind(cardDictB, 3)
    aTwosValue = getNumOfAKind(cardDictA, 2)
    bTwosValue = getNumOfAKind(cardDictB, 2)

    if isLarger(aThreesValue, bThreesValue) != None:
        return isLarger(aThreesValue, bThreesValue)
    return isLarger(aTwosValue, bTwosValue)


def resolveFlush(handA, handB):
    """Resolves the comparison of 2 hands if they are both flushes"""
    aRanks = getCardRankList(handA)
    bRanks = getCardRankList(handB)

    return resolveKickerCards(aRanks, bRanks)


def resolveStraight(handA, handB):
    """Resolves the comparison of 2 hands if they are both straights"""
    aHighCard = getHighCard(handA).rank
    bHighCard = getHighCard(handB).rank

    if aHighCard == 1 and handA.contains(2):  # This signifies a straight with a low of an ace
        aHighCard = 5
    if bHighCard == 1 and handB.contains(2):
        bHighCard = 5

    return isLarger(aHighCard, bHighCard)


def resolveNOfAKind(handA, handB, n):
    """Resolves which hand is better for n of a kind type hands"""
    cardDictA = getAlikeCards(handA)
    cardDictB = getAlikeCards(handB)

    aPairValue = getNumOfAKind(cardDictA, n)
    bPairValue = getNumOfAKind(cardDictB, n)

    if isLarger(aPairValue, bPairValue) != None:
        return isLarger(aPairValue, bPairValue)

    aRanks = getCardRankList(handA)
    bRanks = getCardRankList(handB)
    aRanks.remove(aPairValue)
    bRanks.remove(bPairValue)
    return resolveKickerCards(aRanks, bRanks)


def resolveKickerCards(aCards, bCards):
    """Takes the remnants of a hand after removing pairs and compares them. aCards and bCards must be lists with the same len"""
    aCards.sort(reverse=True)
    bCards.sort(reverse=True)

    for i in range(0, len(aCards)):
        if isLarger(aCards[i], bCards[i]) != None:
            return isLarger(aCards[i], bCards[i])

    return None


def resolveHighCard(handA, handB):
    """Resolves the comparison of 2 hands if they are both high cards"""
    aRanks = getCardRankList(handA)
    bRanks = getCardRankList(handB)

    return resolveKickerCards(aRanks, bRanks)


def pokerHand(hand):
    """Gives best poker hand from a Hand object"""
    if len(hand.cards) != 5:
        print('Hands need to be made up of 5 cards')
        return

    for card in hand.cards:
        if card.suit not in ['hearts', 'diamonds', 'clubs', 'spades']:
            print('Using a suit that does not exist')
            return
        if card.rank < 1 or card.rank > 13:
            print('Using an illegal card value')
            return

    if isRoyalFlush(hand):
        return PokerHands.RoyalFlush
    elif containsStraight(hand) and containsFlush(hand):
        return PokerHands.StraightFlush
    elif getBestAlikeCardHand(hand) != None and getBestAlikeCardHand(hand) == PokerHands.FourOfAKind:
        return PokerHands.FourOfAKind
    elif getBestAlikeCardHand(hand) != None and getBestAlikeCardHand(hand) == PokerHands.FullHouse:
        return PokerHands.FullHouse
    elif containsFlush(hand):
        return PokerHands.Flush
    elif containsStraight(hand):
        return PokerHands.Straight
    elif getBestAlikeCardHand(hand) != None:  # Handle 3 pair, 2 pair and 1 pair cases
        return getBestAlikeCardHand(hand)
    else:
        return PokerHands.HighCard


def isRoyalFlush(hand):
    """returns true if the hand is a royal flush"""
    if not containsFlush(hand) or not containsStraight(hand) or not getHighCard(hand).rank == 1:
        return False
    royalFlush = [10, 11, 12, 13, 1]
    for card in hand.cards:
        if card.rank not in royalFlush:
            return False
    return True


def containsFlush(hand):
    """returns true if the hand contains a flush"""
    suit = hand.cards[0].suit
    for card in hand.cards:
        if card.suit != suit:
            return False

    return True


def containsStraight(hand):
    """returns true if the hand contains a straight"""
    cardRanks = getCardRankList(hand)
    cardRanks.sort()
    if cardRanks[0] == 1 and cardRanks[1] != 2:
        cardRanks = cardRanks[1:] + cardRanks[
                                    0:1]  # if we have an ace, but not a 2, try the ace at the top of the list for 10-ace straights

    prevRank = cardRanks[0]
    for rank in cardRanks[1:]:
        if rank == prevRank + 1:
            prevRank = rank
        elif rank == 1 and prevRank == 13:  # handle the ace high case
            prevRank = rank
        else:
            return False
    return True


def getAlikeCards(hand):
    """returns dict where keys are unique values in the hand, and values are number of times it appears.
    e.g. a full house of 2s and 3s would look like: {3:2, 2:3}"""
    cardRanks = getCardRankList(hand)
    uniqueCards = list(set(cardRanks))

    ofAKindDict = {}
    for cardRank in uniqueCards:
        numOfAKind = cardRanks.count(cardRank)
        ofAKindDict[cardRank] = numOfAKind

    return ofAKindDict


def getBestAlikeCardHand(hand):
    """Gives highest possible combination of pairs, returned as [pokerhand, list or singleton of values]"""
    cardDict = getAlikeCards(hand)
    if len(cardDict) == len(hand.cards):
        return None  # This means there are no pairs
    if len(cardDict) == 2:  # Full house or 4 of a kind
        fours = getNumOfAKind(cardDict, 4)
        if fours != None:
            return PokerHands.FourOfAKind
        else:
            return PokerHands.FullHouse
    if len(cardDict) == 3:  # Two pair or 3 of a kind
        threes = getNumOfAKind(cardDict, 3)
        if threes != None:
            return PokerHands.ThreeOfAKind
        else:
            return PokerHands.TwoPair
    if len(cardDict) == 4:  # One pair
        return PokerHands.Pair

    return None


def getNumOfAKind(cardDict, num):
    """Returns value of card of which we have "num" of. e.g. if we had 3 5s, and i pass 3 as num, it will return 5, returns list if multiples"""
    values = []
    for key, value in cardDict.items():
        if value == num:
            values.append(key)
    if len(values) > 1:
        return values
    elif values != []:
        return values[0]
    else:
        return None


def getCardRankList(hand):
    """Returns list of ranks of all cards in the hand"""
    cardRanks = []
    for card in hand.cards:
        cardRanks.append(card.rank)
    return cardRanks


def getHighCard(hand):
    """Returns highest card in hand(if there is a 1, it is returned)"""
    highestCard = hand.cards[0]
    for card in hand.cards:
        if card.rank == 1:
            return card
        if card.rank > highestCard.rank:
            highestCard = card

    return highestCard


def main():
    cardA = Card(3, 'diamonds')
    cardB = Card(3, 'hearts')
    cardC = Card(5, 'hearts')
    cardD = Card(2, 'hearts')
    cardE = Card(7, 'hearts')

    handA = Hand([cardA, cardB, cardC, cardD, cardE])

    cardF = Card(3, 'hearts')
    cardG = Card(3, 'hearts')
    cardH = Card(7, 'diamonds')
    cardI = Card(4, 'hearts')
    cardJ = Card(5, 'hearts')

    handB = Hand([cardF, cardG, cardH, cardI, cardJ])

    print('Hand A: ' + str(pokerHand(handA)))
    print('Hand B: ' + str(pokerHand(handB)))

    winner = compareTwoHands(handA, handB)
    if winner:
        print('Hand A wins!')
    elif winner != None:  # Need strict comparison because None means a split pot
        print('Hand B wins!')
    else:
        print('The pot is split')

    print('\n')

    cardA = Card(10, 'diamonds')
    cardB = Card(11, 'hearts')
    cardC = Card(12, 'spades')
    cardD = Card(2, 'clubs')
    cardE = Card(7, 'hearts')

    tableCards = Hand([cardA, cardB, cardC, cardD, cardE])

    # Player A cards
    cardF = Card(9, 'diamonds')
    cardG = Card(13, 'hearts')
    
    # Player B Cards
    cardH = Card(13, 'spades')
    cardI = Card(1, 'hearts')

    playerAHand = getTexasHoldEmHand(cardF, cardG, tableCards)
    playerBHand = getTexasHoldEmHand(cardH, cardI, tableCards)
    print('Player As best hand is: ' + playerAHand.handString())
    print('which is a: ' + str(pokerHand(playerAHand)))
    print('')
    print('Player Bs best hand is: ' + playerBHand.handString())
    print('which is a: ' + str(pokerHand(playerBHand)))

    texasHoldEmWinner = compareTwoHands(playerAHand, playerBHand)
    if texasHoldEmWinner:
        print('Hand A wins Texas Holdem!')
    elif texasHoldEmWinner != None:  # Need strict comparison because None means a split pot
        print('Hand B wins Texas Holdem!')
    else:
        print('The pot is split for Texas Holdem')


main()
