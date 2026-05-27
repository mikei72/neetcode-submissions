class Solution:
    def getKth(self, a: List[int], m: int, b: List[int], n: int, k: int):
            if m > n:
                return self.getKth(b, n, a, m, k)
            
            if m == 0:
                return b[k - 1]
            
            if k == 1:
                return min(a[0], b[0])
            
            i = min(m, k // 2)
            j = min(n, k // 2)

            if a[i - 1] <= b[j - 1]:
                return self.getKth(a[i:], m - i, b, n, k - i)
            else:
                return self.getKth(a, m, b[j:], n - j, k - j)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA, lenB = len(nums1), len(nums2)
        lenTotal = lenA + lenB

        if (lenA + lenB) % 2 == 1:
            return self.getKth(nums1, lenA, nums2, lenB, (lenTotal + 1) // 2)
        else:
            x = self.getKth(nums1, lenA, nums2, lenB, lenTotal // 2)
            y = self.getKth(nums1, lenA, nums2, lenB, lenTotal // 2 + 1)
            return (x + y) / 2
            