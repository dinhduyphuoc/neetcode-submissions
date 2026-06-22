class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        check = [0] * 26
        curCheck = [0] * 26
        
        for c in s1:
            check[ord(c) - ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            idxL = ord(s2[l]) - ord('a')
            idxR = ord(s2[r]) - ord('a')
            if (r - l + 1) > len(s1):
                curCheck[idxL] -= 1
                l += 1
            curCheck[idxR] += 1
            if check == curCheck:
                return True
        return False