class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        tasks = [-v for v in Counter(tasks).values()]
        heapq.heapify(tasks)
        q = deque()

        while q or tasks: 
            time += 1
            if q and q[0][0] <= time:
                heapq.heappush(tasks, q.popleft()[1])
            if tasks: 
                v = heapq.heappop(tasks)
                
                if v + 1 < 0:
                    q.append((time + n + 1, v + 1))

        return time