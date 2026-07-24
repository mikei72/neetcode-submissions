class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = []
        for t in triplets:
            if t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]:
                res = t
                triplets.remove(t)
        if not res:
            return False

        for t in triplets:
            if t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2]:
                res = [
                    res[0],
                    t[1],
                    max(res[2], t[2])
                ]
                triplets.remove(t)
        if res[1] != target[1]:
            return False
        elif res[2] == target[2]:
            return True
        
        for t in triplets:
            if t[2] == target[2] and t[0] <= target[0] and t[1] <= target[1]:
                return True

        return False