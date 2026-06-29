class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()
            stack.append(i)
            if len(stack) == 1:
                res.append(0)
            else:
                res.append(stack[-2] - stack[-1])
        
        return res[::-1]