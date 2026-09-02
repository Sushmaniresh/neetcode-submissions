class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a) #b->a
        state = {}
        def dfs(course):
            if state.get(course)=='visiting':
                return False
            if state.get(course)=='done':
                return True
            state[course]='visiting'
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            state[course]='done'
            return True
        return all(dfs(c) for c in range(numCourses))
            

        