class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n +1))
        min_edge = [float('inf')] * (n + 1)

        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j, weight):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                min_edge[root_j] = min(min_edge[root_j], min_edge[root_i], weight)
            else:
                min_edge[root_j] = min(min_edge[root_j], weight)

        for u, v, w in roads: union(u, v, w)
        return min_edge[find(1)]