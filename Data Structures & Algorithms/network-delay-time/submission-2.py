class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)

        for s, t, w in times: 
            d[s].append((t, w))
        
        h = [(0, k)]
        weights = {i: float('inf') for i in range(1, n + 1)}
        weights[k] = 0

        nodes = n

        while h:
            w, n = heapq.heappop(h)

            if w > weights[n]:
                continue
            
            nodes -= 1

            for nn, nw in d[n]:
                new_weight = w + nw 
                if new_weight < weights[nn]:
                    weights[nn] = new_weight
                    heapq.heappush(h, (new_weight, nn))
        
        return max(weights.values()) if nodes == 0 else -1




