class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix), len(matrix[0])
        l, r = 0, x * y - 1

        while l <= r:
            mid = l + (r - l + 1) // 2
            row = mid // y
            col = mid % y
            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
        
        return False