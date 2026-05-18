class Solution:
    def numIslands2(self, m, n, positions):
        par = list(range(m * n))
        rank = [1] * (m * n)
        land = set()
        count = 0
        result = []

        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            nonlocal count
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] > rank[py]:
                par[py] = px
                rank[px] += rank[py]
            else:
                par[px] = py
                rank[py] += rank[px]
            count -= 1  # two islands merged into one

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for r, c in positions:
            idx = r * n + c
            if idx in land:       # duplicate position
                result.append(count)
                continue
            land.add(idx)
            count += 1            # new island

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                nidx = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and nidx in land:
                    union(idx, nidx)

            result.append(count)

        return result