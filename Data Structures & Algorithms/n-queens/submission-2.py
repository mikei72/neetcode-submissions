class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        row = [False] * n
        posDiag, negDiag = [False] * n * 2, [False] * n * 2

        def dfs(count):
            if count == n:
                res.append(["".join(row) for row in board])
                return
            
            for x in range(n):
                if row[x] or posDiag[count + x] or negDiag[count - x + n]:
                    continue

                row[x] = True
                posDiag[count + x] = True
                negDiag[count - x + n] = True
                board[x][count] = "Q"

                dfs(count + 1)
                
                row[x] = False
                posDiag[count + x] = False
                negDiag[count - x + n] = False
                board[x][count] = "."
                    
        dfs(0)
        
        return res