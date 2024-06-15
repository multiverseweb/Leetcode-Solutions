class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        n = len(profits)
        projects = list(zip(profits, capital))
        projects.sort(key=lambda x: x[1])
        current_capital = w
        max_heap = []
        for _ in range(k):
            while projects and projects[0][1] <= current_capital:
                profit = projects.pop(0)[0]
                heapq.heappush(max_heap, -profit)
            if not max_heap:
                break
            current_capital += -heapq.heappop(max_heap)
        return current_capital
