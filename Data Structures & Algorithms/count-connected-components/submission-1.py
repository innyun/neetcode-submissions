class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)
        
        components = set()
        
        for node in uf.parent:
            components.add(uf.find(node))

        return len(components)
        

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

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
