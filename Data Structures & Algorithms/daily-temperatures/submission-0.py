class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                stack_i = stack.pop()
                res[stack_i]=i-stack_i
            stack.append(i)
        return res