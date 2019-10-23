class MySolution:
    def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
        def findParent(pre, i):
            if pre[i] == i:
                return i
            return findParent(pre, pre[i])

        def check(pre):
            root = set()
            for i in range(1, len(pre)):
                root.add(findParent(pre, i))
            if len(root) == 1:
                return True
            return False

        rebundant, vertex = [], []
        for item in edges:
            for ver in item:
                if ver not in vertex:
                    vertex.append(ver)
        ver_num = max(vertex)
        # [a, b] b is the parent of a
        for i in range(len(edges)):
            pre = [j for j in range(ver_num + 1)]
            for edge in edges:
                if edge == edges[i]:
                    continue
                parent = findParent(pre, edge[0])
                if pre[edge[1]] == parent:
                    continue
                pre[parent] = findParent(pre, edge[1])
            if check(pre):
                rebundant.append(edges[i])
        return rebundant[-1]

# ---------------------------------------------
# Solution with Union-By-Rank

class DSU:
    def __init__(self):
        self.par = list(range(1001))
        self.rnk = [1 for i in range(1001)]

    def find(self, i):
        if self.par[i] == i:
            return i
        return self.find(self.par[i])

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge



if __name__ == "__main__":
    a = Solution()
    print(a.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))