class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [1] * (size + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False
        
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1

        return True
