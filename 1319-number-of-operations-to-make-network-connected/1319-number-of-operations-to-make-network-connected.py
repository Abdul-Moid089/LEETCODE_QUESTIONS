class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        graph = [[] for _ in range(n)]

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        components = 0

        def dfs(node):
            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                components += 1
                dfs(i)

        return components - 1