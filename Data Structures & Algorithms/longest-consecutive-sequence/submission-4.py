class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find_consec(num, nums_set, length):
            if num + 1 in nums_set:
                return find_consec(num + 1, nums_set, length + 1)
            else:
                return length

        nums_set = set(nums)

        start_list = []
        for num in nums_set:
            if num - 1 not in nums_set:
                start_list.append(num)
        
        length = 0
        for start in start_list:
            length = max(length, find_consec(start, nums_set, 1))
        
        return length
