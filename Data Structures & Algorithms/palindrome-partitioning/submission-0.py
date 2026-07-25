class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def generate(start):
            if start == len(s):
                res.append(cur.copy())
                return
            for end in range(start, len(s)):
                if not isPalindrome(s[start:end+1]):
                    continue
                cur.append(s[start:end+1])
                generate(end+1)
                cur.pop()

        generate(0)
        return res