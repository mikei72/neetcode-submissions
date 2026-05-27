class Solution:
    def getKth(self, a: List[int], m: int, b: List[int], 
                n: int, k: int, a_start: int, b_start: int):
            if m > n:
                return self.getKth(b, n, a, m, k, b_start, a_start)
            
            if m == 0:
                return b[b_start + k - 1]
            
            if k == 1:
                return min(a[a_start], b[b_start])
            
            i = min(m, k // 2)
            j = min(n, k // 2)

            if a[a_start + i - 1] <= b[b_start + j - 1]:
                return self.getKth(a, m - i, b, n, k - i, a_start + i, b_start)
            else:
                return self.getKth(a, m, b, n - j, k - j, a_start, b_start + j)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA, lenB = len(nums1), len(nums2)
        lenTotal = lenA + lenB

        x = self.getKth(nums1, lenA, nums2, lenB, (lenTotal + 1) // 2, 0, 0)
        y = self.getKth(nums1, lenA, nums2, lenB, (lenTotal + 2) // 2, 0, 0)
        return (x + y) / 2
            