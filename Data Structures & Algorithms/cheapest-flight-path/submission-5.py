class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)

        for s, d, w in flights: 
            g[s].append((d, w))

        h = [(0, src, k + 1)]

        # CHANGE 1: weights is now 2D: [node][remaining_flights]
        weights = [[float('inf')] * (k + 2) for _ in range(n)]
        weights[src][k + 1] = 0

        while h:
            w, u, rem = heapq.heappop(h)   # CHANGE 2: rename k -> rem

            # CHANGE 3: early return when we reach dst
            if u == dst:
                return w

            for v, nw in g[u]:
                new_weight = nw + w 
                # CHANGE 4: check weights[v][rem - 1]
                if new_weight < weights[v][rem - 1] and (rem - 1 > 0 or v == dst):
                    weights[v][rem - 1] = new_weight 
                    heapq.heappush(h, (new_weight, v, rem - 1))
        
        return -1
