class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [-value for value in Counter(tasks).values()]
        heapq.heapify(tasks)
        q = deque()
        cycles = 0

        while tasks or q:
            cycles += 1

            if q and q[0][0] == cycles:
                heapq.heappush(tasks, q.popleft()[1])

            if tasks:
                value = heapq.heappop(tasks)
                if value + 1 < 0:
                    q.append((cycles + n + 1, value + 1))
                
        return cycles
