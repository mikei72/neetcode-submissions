class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appear = set()
        for num in nums:
            if num in appear:
                appear.remove(num)
            else:
                appear.add(num)
        return appear.pop()