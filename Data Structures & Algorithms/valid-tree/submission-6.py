class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and not edges:
            return True
        visited = set()
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        valid = True

        def dfs(node, cur_visited, prev):
            nonlocal valid

            print(node, cur_visited, valid)

            if node not in graph.keys() or node in visited or not valid:
                visited.add(node)
                return
            if node in cur_visited:
                valid = False
                visited.add(node)
                return
            for nnode in graph[node]:
                if nnode == prev:
                    continue
                cur_visited.add(node)
                dfs(nnode, cur_visited, node)
            visited.add(node)

        print(graph)
        
        for node in graph.keys():
            dfs(node, set(), None)
            visited.add(node)
            break

        print(visited)

        return valid and len(visited) == n
            
