from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            vertices = 1
            degree = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    v, d = dfs(nei)
                    vertices += v
                    degree += d

            return vertices, degree

        for i in range(n):
            if not visited[i]:
                vertices, degree = dfs(i)
                edge_count = degree // 2

                if edge_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans