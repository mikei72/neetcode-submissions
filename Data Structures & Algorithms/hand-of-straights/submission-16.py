class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        map = Counter(hand)
        
        for i in sorted(map.keys()):
            if map[i]:
                value = map[i]
                for j in range(groupSize):
                    if map[i + j] and map[i + j] >= value:
                        map[i + j] -= value
                    else:
                        return False
        
        return True