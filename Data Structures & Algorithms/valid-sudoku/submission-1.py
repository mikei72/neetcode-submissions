class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for n in range(3):
                existed = set()
                for j in range(9):
                    if n == 0:
                        num = board[i][j]
                    elif n == 1:
                        num = board[j][i]
                    else:
                        num = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]

                    if num != "." and num in existed:
                        return False
                    else:
                        existed.add(num)
        
        return True

                

                
