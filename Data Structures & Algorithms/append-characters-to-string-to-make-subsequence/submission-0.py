class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = q = 0
        while p < len(s):
            if q >= len(t):
                return len(t[q:])
            if s[p] != t[q]:
                p += 1
            else:
                p += 1
                q += 1
        return len(t[q:])