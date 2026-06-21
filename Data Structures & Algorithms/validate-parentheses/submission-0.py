class Solution:
    def isValid(self, s: str) -> bool:
        opens = "([{"
        closes = ")]}"

        stack = []

        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if opens.index(top) != closes.index(c):
                    return False
        
        return True if not stack else False