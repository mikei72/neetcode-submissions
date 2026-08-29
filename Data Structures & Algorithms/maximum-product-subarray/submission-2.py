class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        subs = []
        cur = []
        res = max(nums)

        for num in nums:
            if num == 0:
                if cur:
                    subs.append(cur)
                    cur = []
            else:
                cur.append(num)

        if cur:
            subs.append(cur)

        for sub in subs:
            negs = sum(1 for n in sub if n < 0)
            prod = 1
            needs = negs if negs % 2 == 0 else negs - 1
            negs = 0
            j = 0

            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    negs += 1
                    while negs > needs:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j += 1
                if j <= i:
                    res = max(res, prod)
            
        return res
        