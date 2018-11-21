from enum import Enum

class Card:
	def __init__(self, rank, suit):
		self.suit = suit  # suit is an int from 1-13
		self.rank = rank  # rank is a string of ['hearts', 'diamonds', 'clubs', 'spades']


class Hand:
	def __init__(self, cards):
		self.cards = cards  # list of cards of type card


class PokerHands(Enum):
	RoyalFlush = 1
	StraightFlush = 2
	FourOfAKind = 3
	FullHouse = 4
	Flush = 5
	Straight = 6
	ThreeOfAKind = 7
	TwoPair = 8
	Pair = 9
	HighCard = 10


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

	if containsStraight(hand) and containsFlush(hand) and getHighCard(hand).rank == 1:
		return PokerHands.RoyalFlush
	elif containsStraight(hand) and containsFlush(hand):
		return PokerHands.StraightFlush
	elif getBestAlikeCardHand(hand) != None and getBestAlikeCardHand(hand)[0] == PokerHands.FourOfAKind:
		return PokerHands.FourOfAKind
	elif getBestAlikeCardHand(hand) != None and getBestAlikeCardHand(hand)[0] == PokerHands.FullHouse:
		return PokerHands.FullHouse
	elif containsFlush(hand):
		return PokerHands.Flush
	elif containsStraight(hand):
		return PokerHands.Straight
	elif getBestAlikeCardHand(hand) != None: # Handle 3 pair, 2 pair and 1 pair cases
		return getBestAlikeCardHand(hand)[0]
	else:
		return PokerHands.HighCard

def containsFlush(hand):
	suit = hand.cards[0].suit
	for card in hand.cards:
		if card.suit != suit:
			return False

	return True


def containsStraight(hand):
	cardRanks = getCardRankList(hand)
	cardRanks.sort()
	if cardRanks[0] == 1 and cardRanks[1] != 2:
		cardRanks = cardRanks[1:] + cardRanks[0:1] # if we have an ace, but not a 2, try the ace at the top of the list for 10-ace straights


	prevRank = cardRanks[0]
	for rank in cardRanks[1:]:
		if rank == prevRank+1:
			prevRank = rank
		elif rank == 1 and prevRank == 13: # handle the ace high case
			prevRank = rank
		else:
			return False
	return True


def getAlikeCards(hand):
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
		return None # This means there are no pairs
	if len(cardDict) == 2: # Full house or 4 of a kind
		fours = getNumOfAKind(cardDict, 4)
		if fours != None:
			return [PokerHands.FourOfAKind, fours]
		else:
			threes = getNumOfAKind(cardDict, 3)
			twos = getNumOfAKind(cardDict, 2)
			return [PokerHands.FullHouse, [threes, twos]]
	if len(cardDict) == 3: # Two pair or 3 of a kind
		threes = getNumOfAKind(cardDict, 3)
		if threes != None:
			return [PokerHands.ThreeOfAKind, threes]
		else:
			twos = getNumOfAKind(cardDict, 2)
			return [PokerHands.TwoPair, twos]
	if len(cardDict) == 4: # One pair
		pair = getNumOfAKind(cardDict, 2)
		return [PokerHands.Pair, pair]

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
	cardRanks = []
	for card in hand.cards:
		cardRanks.append(card.rank)
	return cardRanks


def getHighCard(hand):
	highestCard = hand.cards[0]
	for card in hand.cards:
		if card.rank == 1:
			return card
		if card.rank > highestCard.rank:
			highestCard = card

	return highestCard


def getRank(card):
	return card.rank


def main():
	cardD = Card(1, 'hearts')
	cardA = Card(1, 'hearts')
	cardB = Card(11, 'diamonds')
	cardE = Card(11, 'hearts')
	cardC = Card(11, 'hearts')

	hand = Hand([cardA, cardB, cardC, cardD, cardE])
	print('Contains Flush: ' + str(containsFlush(hand)))
	print('Contains Straight: ' + str(containsStraight(hand)))
	print('Best pairs: ' + str(getBestAlikeCardHand(hand)))
	print('High Card: ' + str(getHighCard(hand).rank) + ' of ' + getHighCard(hand).suit)

	print(pokerHand(hand))

main()
