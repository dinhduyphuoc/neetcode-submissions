class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0] * 26

        for c in s:
            check[ord(c) - ord('a')] += 1
        
        for c in t:
            idx = ord(c) - ord('a')
            if check[idx] == 0:
                return False
            check[idx] -= 1
        
        return sum(check) == 0