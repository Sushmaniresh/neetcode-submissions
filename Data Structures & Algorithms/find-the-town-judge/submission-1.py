class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        total = defaultdict(int)
  
        for src,dest in trust:
            total[src]-=1
            total[dest]+=1
        for i in range(1,n+1):
            if total[i]==n-1:
                return i
        return -1
        