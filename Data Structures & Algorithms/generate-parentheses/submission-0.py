class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(arr, opens, closes):
            if opens == closes == n:
                res.append("".join(arr))
                return
            if opens < n:
                arr.append("(")
                backtrack(arr, opens + 1, closes)
                arr.pop()
            if closes < opens:
                arr.append(")")
                backtrack(arr, opens, closes + 1)
                arr.pop()
        
        backtrack([], 0, 0)
        return res