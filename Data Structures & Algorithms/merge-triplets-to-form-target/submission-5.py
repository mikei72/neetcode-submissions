class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        obtained = [False, False, False]

        for t in triplets:
            if not obtained[0] and t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]:
                obtained[0] = True
            if not obtained[1] and t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2]:
                obtained[1] = True
            if not obtained[2] and t[2] == target[2] and t[1] <= target[1] and t[0] <= target[0]:
                obtained[2] = True

        return True if (obtained[0] and obtained[1] and obtained[2]) else False