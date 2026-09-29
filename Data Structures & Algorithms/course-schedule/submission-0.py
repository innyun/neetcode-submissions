class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            graph[prereq[1]].append(prereq[0])
        
        q = deque()

        for i, deg in enumerate(indegree):
            if deg == 0:
                q.append(i)
    
        while q:
            node = q.popleft()
            next_nodes = graph[node]
            for next_node in next_nodes:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
            del graph[node]

        return not graph