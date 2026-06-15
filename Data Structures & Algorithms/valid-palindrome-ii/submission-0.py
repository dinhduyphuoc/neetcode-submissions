class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            while l <= r:
                print("Inside", s[l], s[r])
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        l = 0
        r = len(s) - 1

        while l <= r:
            print(s[l], s[r])
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s[l+1:r+1]) is True or isPalindrome(s[l:r]) is True 
        
        return True