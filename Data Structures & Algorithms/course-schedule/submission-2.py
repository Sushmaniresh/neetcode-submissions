class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list )
        indegree = {i:0 for i in range(numCourses)}
        visited = 0
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1

        que = deque(p for p in range(numCourses) if indegree[p]==0)
   
        while que:
            curr = que.popleft()
            visited+=1
           
            for n in graph[curr]:
                indegree[n]-=1
                if indegree[n]==0:
                    que.append(n)
        if visited == numCourses:
            return True
        else:
            return False
        

            

        
            

        