class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for s, t, w in times: 
            g[s].append((t, w))
        
        weights = [float('inf') for _ in range(n)]
        weights[k - 1] = 0
        h = [(k, 0)]

        while h:
            n, w = heapq.heappop(h)

            if w > weights[n - 1]:
                continue
            
            for nn, nw in g[n]:
                new_weight = nw + w
                if new_weight < weights[nn - 1]:
                    weights[nn - 1] = new_weight
                    heapq.heappush(h, (nn, new_weight))

        return max(weights) if max(weights) != float('inf') else -1