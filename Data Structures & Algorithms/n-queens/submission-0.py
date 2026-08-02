class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(count):
            if count == n:
                res.append(["".join(row) for row in board])
                return
            
            for x in range(n):
                if self.isSafe(x, count, board):
                    board[x][count] = "Q"
                    dfs(count + 1)
                    board[x][count] = "."
                    
        dfs(0)
        
        return res

    def isSafe(self, row, col, board):
        c = col - 1
        while c >= 0:
            if board[row][c] == "Q":
                return False
            c -= 1
        
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        r, c = row + 1, col - 1
        while r < len(board) and c >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1
        
        return True
