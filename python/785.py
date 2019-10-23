class Solution:
    def isBipartite(self, graph: 'List[List[int]]') -> 'bool':
        def fillColor(m, n, graph, colormap, index):
            nonlocal Flag
            for i in graph[index]:
                if colormap[i] != nocolor:
                    if colormap[i] == colormap[index]:
                        Flag = False
                else:
                    colormap[i] = 1 - colormap[index]
                    fillColor(m, n, graph, colormap, i)
            return

        Flag = True
        m, n = len(graph), len(graph[0])
        nocolor, red, blue = -1, 0, 1
        colormap = [nocolor for i in range(m)]
        colormap[0] = red
        fillColor(m, n, graph, colormap, 0)
        for i in range(1, m):
            if colormap[i] == nocolor:
                fillColor(m, n, graph, colormap, i)
        return Flag


if __name__ == "__main__":
    a = Solution()
    print(a.isBipartite([[1,3], [0,2], [1,3], [0,2]]))