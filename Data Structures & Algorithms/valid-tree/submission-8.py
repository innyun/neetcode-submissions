class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set()
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for nnode in graph[node]:
                if nnode == prev:
                    continue
                if not dfs(nnode, node):
                    return False
            
            return True

        return dfs(0, None) and len(visited) == n