class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(x, y, i):
            if i == len(word):
                return True
            
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != word[i] or board[x][y] == '#':
                return False
            
            i += 1

            board[x][y] = '#'
            res = dfs(x - 1, y, i) or dfs(x + 1, y, i) or dfs(x, y - 1, i) or dfs(x, y + 1, i)
            board[x][y] = word[i - 1]

            return res
        
        for r in range(m):
            for s in range(n):
                if dfs(r, s, 0):
                    return True
        
        return False
            
            