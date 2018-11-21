class Card:
	def __init__(self, rank, suit):
		self.suit = suit  # suit is an int from 1-13
		self.rank = rank  # rank is a string of ['hearts', 'diamonds', 'clubs', 'spades']


class Hand:
	def __init__(self, cards):
		self.cards = cards  # list of cards of type card


def pokerHand(hand):  # hand is assumed to be of type Hand above
	print('Contains Flush: ' + str(containsFlush(hand)) + '\n')
	print('Contains Straight: ' + str(containsStraight(hand)))

def containsFlush(hand):
	suit = hand.cards[0].suit
	for card in hand.cards:
		if card.suit != suit:
			return False

	return True


def containsStraight(hand):
	cardRanks = []
	for card in hand.cards:
		cardRanks.append(card.rank)
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



def getRank(card):
	return card.rank


def main():
	cardD = Card(2, 'hearts')
	cardA = Card(1, 'hearts')
	cardB = Card(3, 'hearts')
	cardE = Card(6, 'hearts')
	cardC = Card(4, 'hearts')

	hand = Hand([cardA, cardB, cardC, cardD, cardE])
	pokerHand(hand)

main()
