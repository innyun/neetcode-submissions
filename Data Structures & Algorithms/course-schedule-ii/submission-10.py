class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = []
        processed = 0

        indegree = [0] * numCourses
        graph = defaultdict(list)

        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            graph[prereq[1]].append(prereq[0])
        
        q = deque()

        for i, deg in enumerate(indegree):
            if deg == 0:
                q.append(i)

        while q:
            node = q.popleft()
            out.append(node)
            adjacent_nodes = graph[node]
            for adj_n in adjacent_nodes:
                indegree[adj_n] -= 1
                if indegree[adj_n] == 0:
                    q.append(adj_n)
            processed += 1

        return out if processed == numCourses else []