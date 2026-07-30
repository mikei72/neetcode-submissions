class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        par = []

        def dfs(left, right):
            if len(par) == 2 * n:
                res.append(''.join(par))
                return
            
            if left < n:
                par.append('(')
                dfs(left + 1, right)
                par.pop()

            if left > right:
                par.append(')')
                dfs(left, right + 1)
                par.pop()

        dfs(0, 0)
        return res
