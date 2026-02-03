class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        edge cases k > n??
        curr solution O(kn)
        """
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()

        max_heap = []

        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            w -= heapq.heappop(max_heap)
        return w
