class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp1 = set()
        dp1.add(0)

        for i in range(len(nums)):
            dp2 = set()
            for t in dp1:
                if t + nums[i] == target:
                    return True
                dp2.add(t + nums[i])
                dp2.add(t)
            dp1 = dp2
        
        return False