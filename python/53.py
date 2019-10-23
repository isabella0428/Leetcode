class Solution1:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nsum = 0
        nmax = float("-inf")

        for n in nums:
            nsum += n
            if nsum > nmax:
                nmax = nsum
            if nsum < 0:
                nsum = 0
                continue

        return nmax


class Solution2:
    def maxSubArray(self, nums):
        ret, total = max(nums), nums[0]
        for item in nums[1:]:
            if total < 0:
                total = 0
            total += item
            ret = max(total, ret)
        return ret


if __name__ == "__main__":
    a = Solution2()
    print(a.maxSubArray([-1, -3]))