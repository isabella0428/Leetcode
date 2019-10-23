class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def combination(n, k, count, tmp):
            if len(tmp) == k:
                ans.append(tmp)
                return
            for i in range(tmp[-1] + 1, n + 1):
                tmp.append(i)
                combination(n, k, count + 1, tmp[:])
                tmp = tmp[:-1]

        tmp = []
        ans = []
        for i in range(1, n + 1):
            tmp = [i]
            combination(n, k, 1, tmp[:])
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.combine(4, 2))