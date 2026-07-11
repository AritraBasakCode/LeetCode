class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        res = 0

        def dfs(node):
            visited[node] = True
            vertices.append(node)

            for b in graph[node]:
                if not visited[b]:
                    dfs(b)

        for i in range(n):
            if not visited[i]:
                vertices = []
                dfs(i)

                m = len(vertices)

                # Sum of degrees - m*(m-1)/2 m is the number of nodes
                degree_sum = 0
                for v in vertices:
                    degree_sum += len(graph[v])

                edge_count = degree_sum // 2

                if edge_count == m * (m - 1) // 2:
                    res += 1

        return res