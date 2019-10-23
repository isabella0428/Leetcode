class Solution:
    def shortestPathLength(self, graph):
        # use bits to represent states
        N = len(graph)
        dp = [[float('inf') for i in range(N)] for j in range(1 << N)]

        q = []
        for i in range(N):
            dp[1 << i][i] = 0
            q.append([1 << i, i])

        while q:
            state, node = q.pop(0)
            step = dp[state][node]
            for k in graph[node]:
                new_state = state | (1 << k)
                if dp[new_state][k] == float('inf'):
                    dp[new_state][k] = step + 1
                    q.append([new_state, k])
        return min(dp[-1])


if __name__ == "__main__":
    a = Solution()
    print(a.shortestPathLength([[1, 2, 3],[0], [0], [0]]))