class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = []

        def solutions(n , r, l , current):
            if(l == n):
                solution.append(current)
                return

            if(r < n):
                solutions(n, r + 1, l , current + "(")
            if(r > l):
                solutions(n, r, l + 1 , current + ")")

        solutions(n , 0 , 0 , "")
        return solution