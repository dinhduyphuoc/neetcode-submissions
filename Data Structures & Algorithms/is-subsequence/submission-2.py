class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if not s:
            return True
        if s and not t:
            return False
        for c in t:
            if i >= len(s):
                return True
            if c == s[i]:
                i += 1
        
        return i >= len(s)
