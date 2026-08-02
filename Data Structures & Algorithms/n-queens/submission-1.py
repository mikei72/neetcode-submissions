class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        row = set()
        posDiag, negDiag = set(), set()

        def dfs(count):
            if count == n:
                res.append(["".join(row) for row in board])
                return
            
            for x in range(n):
                if x in row or (count + x) in posDiag or (count - x) in negDiag:
                    continue

                row.add(x)
                posDiag.add(count + x)
                negDiag.add(count - x)
                board[x][count] = "Q"

                dfs(count + 1)
                
                row.remove(x)
                posDiag.remove(count + x)
                negDiag.remove(count - x)
                board[x][count] = "."
                    
        dfs(0)
        
        return res