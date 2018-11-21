import unittest
from enum import Enum
import PokerHands
from PokerHands import Card
from PokerHands import Hand
from PokerHands import PokerHands as hands


class PokerTests(unittest.TestCase):

    # ======= Test Creations =======

    def testPair(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.Pair)

    def testHighCard(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(9, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.HighCard)

    def testTwoPair(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(5, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.TwoPair)

    def testThreeOfAKind(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(3, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.ThreeOfAKind)

    def testStraight(self):
        cardA = Card(2, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(4, 'clubs')
        cardE = Card(6, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.Straight)

    def testFlush(self):
        cardA = Card(3, 'hearts')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.Flush)

    def testFullHouse(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(3, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.FullHouse)

    def testFourOfAKind(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(3, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(3, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.FourOfAKind)

    def testStraightFlush(self):
        cardA = Card(4, 'hearts')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(5, 'hearts')
        cardE = Card(6, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.StraightFlush)

    def testRoyalFlush(self):
        cardA = Card(10, 'hearts')
        cardB = Card(11, 'hearts')
        cardC = Card(12, 'hearts')
        cardD = Card(13, 'hearts')
        cardE = Card(1, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handType = PokerHands.pokerHand(handA)
        self.assertEqual(handType, hands.RoyalFlush)

    # ======= Test Comparisons to own type =======

    def testTiedHandsComparison(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(7, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(6, 'clubs')
        cardE = Card(8, 'hearts')

        cardF = Card(3, 'diamonds')
        cardG = Card(7, 'hearts')
        cardH = Card(2, 'hearts')
        cardI = Card(6, 'clubs')
        cardJ = Card(8, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertIsNone(PokerHands.compareTwoHands(handA, handB))

    def testHighCardComparison(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(7, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(6, 'clubs')
        cardE = Card(8, 'hearts')

        cardF = Card(4, 'diamonds')
        cardG = Card(3, 'hearts')
        cardH = Card(2, 'hearts')
        cardI = Card(6, 'clubs')
        cardJ = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertTrue(PokerHands.compareTwoHands(handA, handB))

    def testTiedHighCardComparison(self):
        """Tests when pairs have the same value if it knows who won based on kicker cards"""
        cardA = Card(10, 'diamonds')
        cardB = Card(8, 'hearts')
        cardC = Card(6, 'hearts')
        cardD = Card(5, 'clubs')
        cardE = Card(4, 'hearts')

        cardF = Card(10, 'diamonds')
        cardG = Card(7, 'hearts')
        cardH = Card(2, 'hearts')
        cardI = Card(6, 'clubs')
        cardJ = Card(4, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertTrue(PokerHands.compareTwoHands(handA, handB))

    def testPairComparison(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(6, 'clubs')
        cardE = Card(7, 'hearts')

        cardF = Card(4, 'diamonds')
        cardG = Card(4, 'hearts')
        cardH = Card(2, 'hearts')
        cardI = Card(6, 'clubs')
        cardJ = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testTiedPairComparison(self):
        """Tests when pairs have the same value if it knows who won based on kicker cards"""
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(6, 'clubs')
        cardE = Card(7, 'hearts')

        cardF = Card(3, 'diamonds')
        cardG = Card(3, 'hearts')
        cardH = Card(2, 'hearts')
        cardI = Card(6, 'clubs')
        cardJ = Card(9, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testTwoPairComparison(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(7, 'hearts')

        cardF = Card(4, 'diamonds')
        cardG = Card(4, 'hearts')
        cardH = Card(2, 'hearts')
        cardI = Card(2, 'clubs')
        cardJ = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testTiedTwoPairComparison(self):
        """Tests when first pair haa the same value if it knows who won based on the 2nd pair"""
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(7, 'hearts')

        cardF = Card(3, 'diamonds')
        cardG = Card(3, 'hearts')
        cardH = Card(5, 'hearts')
        cardI = Card(5, 'clubs')
        cardJ = Card(9, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testTiedTwoPairKickerComparison(self):
        """Tests when pairs have the same value if it knows who won based on kicker cards"""
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(7, 'hearts')

        cardF = Card(3, 'diamonds')
        cardG = Card(3, 'hearts')
        cardH = Card(2, 'hearts')
        cardI = Card(2, 'clubs')
        cardJ = Card(9, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testThreeOfAKindComparison(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(3, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(7, 'hearts')

        cardF = Card(4, 'diamonds')
        cardG = Card(4, 'hearts')
        cardH = Card(4, 'hearts')
        cardI = Card(2, 'clubs')
        cardJ = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testTiedThreeOfAKindComparison(self):
        """Tests when the 3 have the same value if it knows who won based on the kicker cards"""
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(3, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(7, 'hearts')

        cardF = Card(3, 'diamonds')
        cardG = Card(3, 'hearts')
        cardH = Card(3, 'hearts')
        cardI = Card(5, 'clubs')
        cardJ = Card(9, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testStraightComparison(self):
        cardA = Card(2, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(4, 'clubs')
        cardE = Card(6, 'hearts')

        cardF = Card(3, 'diamonds')
        cardG = Card(6, 'hearts')
        cardH = Card(7, 'hearts')
        cardI = Card(5, 'clubs')
        cardJ = Card(4, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testTiedStraightComparison(self):
        """Tests when first pair haa the same value if it knows who won based on the 2nd pair"""
        cardA = Card(2, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(6, 'clubs')
        cardE = Card(4, 'hearts')

        cardF = Card(3, 'diamonds')
        cardG = Card(6, 'hearts')
        cardH = Card(5, 'hearts')
        cardI = Card(4, 'clubs')
        cardJ = Card(2, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertIsNone(PokerHands.compareTwoHands(handA, handB))

    def testTiedFlushComparison(self):
        cardA = Card(8, 'hearts')
        cardB = Card(4, 'hearts')
        cardC = Card(3, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        cardF = Card(8, 'spades')
        cardG = Card(4, 'spades')
        cardH = Card(3, 'spades')
        cardI = Card(2, 'spades')
        cardJ = Card(7, 'spades')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertIsNone(PokerHands.compareTwoHands(handA, handB))

    def testFlushComparison(self):
        cardA = Card(8, 'hearts')
        cardB = Card(3, 'hearts')
        cardC = Card(12, 'hearts')
        cardD = Card(9, 'hearts')
        cardE = Card(7, 'hearts')

        cardF = Card(2, 'hearts')
        cardG = Card(3, 'hearts')
        cardH = Card(7, 'hearts')
        cardI = Card(5, 'hearts')
        cardJ = Card(9, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertTrue(PokerHands.compareTwoHands(handA, handB))

    def testFullHouseComparison(self):
        cardA = Card(2, 'diamonds')
        cardB = Card(2, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(3, 'clubs')
        cardE = Card(3, 'hearts')

        cardF = Card(3, 'diamonds')
        cardG = Card(3, 'hearts')
        cardH = Card(3, 'hearts')
        cardI = Card(2, 'clubs')
        cardJ = Card(2, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testTiedFullHouseComparison(self):
        """Tests when first pair haa the same value if it knows who won based on the 2nd pair"""
        cardA = Card(5, 'diamonds')
        cardB = Card(5, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(3, 'clubs')
        cardE = Card(3, 'hearts')

        cardF = Card(5, 'diamonds')
        cardG = Card(5, 'hearts')
        cardH = Card(5, 'hearts')
        cardI = Card(4, 'clubs')
        cardJ = Card(4, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testFourOfAKindComparison(self):
        cardA = Card(5, 'diamonds')
        cardB = Card(5, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(5, 'clubs')
        cardE = Card(3, 'hearts')

        cardF = Card(6, 'diamonds')
        cardG = Card(6, 'hearts')
        cardH = Card(6, 'hearts')
        cardI = Card(6, 'clubs')
        cardJ = Card(3, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testTiedFourOfAKindComparison(self):
        """Tests when first pair haa the same value if it knows who won based on the 2nd pair"""
        cardA = Card(5, 'diamonds')
        cardB = Card(5, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(5, 'clubs')
        cardE = Card(3, 'hearts')

        cardF = Card(5, 'diamonds')
        cardG = Card(5, 'hearts')
        cardH = Card(5, 'hearts')
        cardI = Card(5, 'clubs')
        cardJ = Card(4, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertFalse(PokerHands.compareTwoHands(handA, handB))

    def testStraightFlushComparison(self):
        cardA = Card(10, 'hearts')
        cardB = Card(7, 'hearts')
        cardC = Card(8, 'hearts')
        cardD = Card(9, 'hearts')
        cardE = Card(11, 'hearts')

        cardF = Card(7, 'hearts')
        cardG = Card(6, 'hearts')
        cardH = Card(5, 'hearts')
        cardI = Card(3, 'hearts')
        cardJ = Card(4, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertTrue(PokerHands.compareTwoHands(handA, handB))

    def testTiedStraightFlushComparison(self):
        """Tests when first pair haa the same value if it knows who won based on the 2nd pair"""
        cardA = Card(10, 'hearts')
        cardB = Card(9, 'hearts')
        cardC = Card(7, 'hearts')
        cardD = Card(8, 'hearts')
        cardE = Card(6, 'hearts')

        cardF = Card(6, 'hearts')
        cardG = Card(8, 'hearts')
        cardH = Card(7, 'hearts')
        cardI = Card(9, 'hearts')
        cardJ = Card(10, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertIsNone(PokerHands.compareTwoHands(handA, handB))

    def testRoyalFlushComparison(self):
        cardA = Card(10, 'hearts')
        cardB = Card(12, 'hearts')
        cardC = Card(13, 'hearts')
        cardD = Card(1, 'hearts')
        cardE = Card(11, 'hearts')

        cardF = Card(12, 'diamonds')
        cardG = Card(11, 'diamonds')
        cardH = Card(13, 'diamonds')
        cardI = Card(10, 'diamonds')
        cardJ = Card(1, 'diamonds')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        handB = Hand([cardF, cardG, cardH, cardJ, cardI])

        self.assertIsNone(PokerHands.compareTwoHands(handA, handB))

    # ===== Test against other hand types =====
