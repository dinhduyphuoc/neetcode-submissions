class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []
        kb = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        cur = []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(cur))
                return
            for c in kb[digits[i]]:
                cur.append(c)
                backtrack(i + 1)
                cur.pop()

        backtrack(0)
        print(res)
        return res

