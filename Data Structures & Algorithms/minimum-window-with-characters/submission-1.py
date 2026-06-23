class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = Counter(t)
        window = defaultdict(int)
        minWin = [0, float('inf')]

        required = len(need)
        formed = 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in need and window[c] == need[c]:
                formed += 1
            
            while l <= r and formed == required:
                if (r - l) < minWin[1] - minWin[0]:
                    minWin[0] = l
                    minWin[1] = r
                cLeft = s[l]
                window[cLeft] -= 1

                if cLeft in need and window[cLeft] < need[cLeft]:
                    formed -= 1
                
                l += 1
        
        return s[minWin[0]: minWin[1] + 1] if minWin[1] != float('inf') else ""
