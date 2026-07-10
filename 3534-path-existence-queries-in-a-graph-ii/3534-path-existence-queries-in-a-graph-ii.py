class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted((v, i) for i, v in enumerate(nums))

        vals = [v for v, _ in order]
        ids = [i for _, i in order]

        pos = [0] * n
        for i, node in enumerate(ids):
            pos[node] = i

        comp = [0] * n
        cid = 0
        for i in range(n):
            if i and vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        LOG = n.bit_length()

        nxt = [0] * n
        for i in range(n):
            j = bisect_right(vals, vals[i] + maxDiff) - 1
            nxt[i] = j

        up = [nxt]
        for _ in range(LOG - 1):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if pu > pv:
                pu, pv = pv, pu

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            cur = pu
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < pv:
                    cur = up[k][cur]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans