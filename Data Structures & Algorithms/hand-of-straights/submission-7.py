class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        groupNum = int(len(hand) / groupSize)

        hand.sort()

        for i in range(groupNum):
            start = hand[0]
            hand.remove(start)
            for j in range(groupSize - 1):
                if start + j + 1 in hand:
                    hand.remove(start + j + 1)
                else:
                    return False

        return True