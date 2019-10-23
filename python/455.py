class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        content = 0
        child_start = 0
        size_start = 0
        while child_start < len(g) and size_start < len(s):
            if s[size_start] >= g[child_start]:
                content += 1
                child_start += 1
            size_start += 1
        return content


if __name__ == "__main__":
    a = Solution()
    print(a.findContentChildren([10,9,8,7],
[5,6,7,8]))