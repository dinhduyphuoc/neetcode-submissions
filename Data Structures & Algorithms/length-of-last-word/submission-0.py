class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        isAlnum = True
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if not s[i].isalnum():
                return count
            count += 1   
        return count