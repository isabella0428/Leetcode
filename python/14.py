class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[: -1]
                if not prefix:
                    return ""
        return prefix


class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        def findPrefix(pre, t, n, strs):
            nonlocal prefix
            if t == n:
                prefix = pre if len(pre) > len(prefix) else prefix
                return
            cur, Flag = strs[0][t], True
            for char in strs:
                if cur != char[t]:
                    prefix = pre if len(pre) > len(prefix) else prefix
                    return
            if Flag:
                tmp = strs[0][t]
                findPrefix(pre + tmp, t + 1, n, strs)

        prefix, n = "", float('inf')
        for item in strs:
            if len(item) < n:
                n = len(item)
        findPrefix("", 0, n, strs)
        return prefix


if __name__ == "__main__":
    a = Solution1()
    print(a.longestCommonPrefix(["c", 'acc']))
