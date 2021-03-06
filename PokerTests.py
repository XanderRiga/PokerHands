import unittest
from enum import Enum
import PokerHands
from PokerHands import Card
from PokerHands import Hand
from PokerHands import PokerHands as hands


class PokerTests(unittest.TestCase):

    def getPairHand(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA

    def getHighCardHand(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(9, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA

    def getTwoPairHand(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(5, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA


    def getThreeOfAKindHand(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(3, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA


    def getStraightHand(self):
        cardA = Card(2, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(4, 'clubs')
        cardE = Card(6, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA

    def getFlushHand(self):
        cardA = Card(3, 'hearts')
        cardB = Card(6, 'hearts')
        cardC = Card(5, 'hearts')
        cardD = Card(2, 'hearts')
        cardE = Card(7, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA

    def getFullHouseHand(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(3, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA


    def getFourOfAKindHand(self):
        cardA = Card(3, 'diamonds')
        cardB = Card(3, 'hearts')
        cardC = Card(3, 'hearts')
        cardD = Card(2, 'clubs')
        cardE = Card(3, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA

    def getStraightFlush(self):
        cardA = Card(4, 'hearts')
        cardB = Card(3, 'hearts')
        cardC = Card(2, 'hearts')
        cardD = Card(5, 'hearts')
        cardE = Card(6, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA

    def getRoyalFlush(self):
        cardA = Card(10, 'hearts')
        cardB = Card(11, 'hearts')
        cardC = Card(12, 'hearts')
        cardD = Card(13, 'hearts')
        cardE = Card(1, 'hearts')

        handA = Hand([cardA, cardB, cardC, cardD, cardE])
        return handA

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

    def testRoyalFlushBeatsAllOthers(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertTrue(PokerHands.compareTwoHands(royalFlush, straightFlush))
        self.assertTrue(PokerHands.compareTwoHands(royalFlush, fourOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(royalFlush, fullHouse))
        self.assertTrue(PokerHands.compareTwoHands(royalFlush, flush))
        self.assertTrue(PokerHands.compareTwoHands(royalFlush, straight))
        self.assertTrue(PokerHands.compareTwoHands(royalFlush, threeOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(royalFlush, twoPair))
        self.assertTrue(PokerHands.compareTwoHands(royalFlush, pair))
        self.assertTrue(PokerHands.compareTwoHands(royalFlush, highCard))


    def testStraightFlushComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(straightFlush, royalFlush))
        self.assertTrue(PokerHands.compareTwoHands(straightFlush, fourOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(straightFlush, fullHouse))
        self.assertTrue(PokerHands.compareTwoHands(straightFlush, flush))
        self.assertTrue(PokerHands.compareTwoHands(straightFlush, straight))
        self.assertTrue(PokerHands.compareTwoHands(straightFlush, threeOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(straightFlush, twoPair))
        self.assertTrue(PokerHands.compareTwoHands(straightFlush, pair))
        self.assertTrue(PokerHands.compareTwoHands(straightFlush, highCard))


    def testFourOfAKindComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(fourOfAKind, royalFlush))
        self.assertFalse(PokerHands.compareTwoHands(fourOfAKind, straightFlush))
        self.assertTrue(PokerHands.compareTwoHands(fourOfAKind, fullHouse))
        self.assertTrue(PokerHands.compareTwoHands(fourOfAKind, flush))
        self.assertTrue(PokerHands.compareTwoHands(fourOfAKind, straight))
        self.assertTrue(PokerHands.compareTwoHands(fourOfAKind, threeOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(fourOfAKind, twoPair))
        self.assertTrue(PokerHands.compareTwoHands(fourOfAKind, pair))
        self.assertTrue(PokerHands.compareTwoHands(fourOfAKind, highCard))


    def testFullHouseComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(fullHouse, royalFlush))
        self.assertFalse(PokerHands.compareTwoHands(fullHouse, straightFlush))
        self.assertFalse(PokerHands.compareTwoHands(fullHouse, fourOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(fullHouse, flush))
        self.assertTrue(PokerHands.compareTwoHands(fullHouse, straight))
        self.assertTrue(PokerHands.compareTwoHands(fullHouse, threeOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(fullHouse, twoPair))
        self.assertTrue(PokerHands.compareTwoHands(fullHouse, pair))
        self.assertTrue(PokerHands.compareTwoHands(fullHouse, highCard))


    def testFlushComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(flush, royalFlush))
        self.assertFalse(PokerHands.compareTwoHands(flush, straightFlush))
        self.assertFalse(PokerHands.compareTwoHands(flush, fourOfAKind))
        self.assertFalse(PokerHands.compareTwoHands(flush, fullHouse))
        self.assertTrue(PokerHands.compareTwoHands(flush, straight))
        self.assertTrue(PokerHands.compareTwoHands(flush, threeOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(flush, twoPair))
        self.assertTrue(PokerHands.compareTwoHands(flush, pair))
        self.assertTrue(PokerHands.compareTwoHands(flush, highCard))


    def testStraightComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(straight, royalFlush))
        self.assertFalse(PokerHands.compareTwoHands(straight, straightFlush))
        self.assertFalse(PokerHands.compareTwoHands(straight, fourOfAKind))
        self.assertFalse(PokerHands.compareTwoHands(straight, fullHouse))
        self.assertFalse(PokerHands.compareTwoHands(straight, flush))
        self.assertTrue(PokerHands.compareTwoHands(straight, threeOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(straight, twoPair))
        self.assertTrue(PokerHands.compareTwoHands(straight, pair))
        self.assertTrue(PokerHands.compareTwoHands(straight, highCard))


    def testThreeOfAKindComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(threeOfAKind, royalFlush))
        self.assertFalse(PokerHands.compareTwoHands(threeOfAKind, straightFlush))
        self.assertFalse(PokerHands.compareTwoHands(threeOfAKind, fourOfAKind))
        self.assertFalse(PokerHands.compareTwoHands(threeOfAKind, fullHouse))
        self.assertFalse(PokerHands.compareTwoHands(threeOfAKind, flush))
        self.assertFalse(PokerHands.compareTwoHands(threeOfAKind, straight))
        self.assertTrue(PokerHands.compareTwoHands(threeOfAKind, twoPair))
        self.assertTrue(PokerHands.compareTwoHands(threeOfAKind, pair))
        self.assertTrue(PokerHands.compareTwoHands(threeOfAKind, highCard))


    def testTwoPairComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(twoPair, royalFlush))
        self.assertFalse(PokerHands.compareTwoHands(twoPair, straightFlush))
        self.assertFalse(PokerHands.compareTwoHands(twoPair, fourOfAKind))
        self.assertFalse(PokerHands.compareTwoHands(twoPair, fullHouse))
        self.assertFalse(PokerHands.compareTwoHands(twoPair, flush))
        self.assertFalse(PokerHands.compareTwoHands(twoPair, straight))
        self.assertFalse(PokerHands.compareTwoHands(twoPair, threeOfAKind))
        self.assertTrue(PokerHands.compareTwoHands(twoPair, pair))
        self.assertTrue(PokerHands.compareTwoHands(twoPair, highCard))


    def testPairComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(pair, royalFlush))
        self.assertFalse(PokerHands.compareTwoHands(pair, straightFlush))
        self.assertFalse(PokerHands.compareTwoHands(pair, fourOfAKind))
        self.assertFalse(PokerHands.compareTwoHands(pair, fullHouse))
        self.assertFalse(PokerHands.compareTwoHands(pair, flush))
        self.assertFalse(PokerHands.compareTwoHands(pair, straight))
        self.assertFalse(PokerHands.compareTwoHands(pair, threeOfAKind))
        self.assertFalse(PokerHands.compareTwoHands(pair, twoPair))
        self.assertTrue(PokerHands.compareTwoHands(pair, highCard))


    def testHighCardComparisons(self):
        royalFlush = self.getRoyalFlush()
        straightFlush = self.getStraightFlush()
        fourOfAKind = self.getFourOfAKindHand()
        fullHouse = self.getFullHouseHand()
        flush = self.getFlushHand()
        straight = self.getStraightHand()
        threeOfAKind = self.getThreeOfAKindHand()
        twoPair = self.getTwoPairHand()
        pair = self.getPairHand()
        highCard = self.getHighCardHand()

        self.assertFalse(PokerHands.compareTwoHands(highCard, royalFlush))
        self.assertFalse(PokerHands.compareTwoHands(highCard, straightFlush))
        self.assertFalse(PokerHands.compareTwoHands(highCard, fourOfAKind))
        self.assertFalse(PokerHands.compareTwoHands(highCard, fullHouse))
        self.assertFalse(PokerHands.compareTwoHands(highCard, flush))
        self.assertFalse(PokerHands.compareTwoHands(highCard, straight))
        self.assertFalse(PokerHands.compareTwoHands(highCard, threeOfAKind))
        self.assertFalse(PokerHands.compareTwoHands(highCard, twoPair))
        self.assertFalse(PokerHands.compareTwoHands(highCard, pair))