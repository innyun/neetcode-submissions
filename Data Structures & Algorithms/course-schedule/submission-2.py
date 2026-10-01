class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        g = defaultdict(list)

        for t, s in prerequisites:
            indegrees[t] += 1
            g[s].append(t)

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for nn in g[node]:
                indegrees[nn] -= 1
                if indegrees[nn] == 0:
                    q.append(nn)
        
        return all(x == 0 for x in indegrees)

