class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ret = float('inf')
        sum = 0
        left = 0
        # change the start!
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                ret = min(ret, i - left +  1)
                sum -= nums[left]
                left += 1
        return ret if ret != float('inf') else 0


if __name__ == "__main__":
    a = Solution()
    print(a.minSubArrayLen(213,
[12,28,83,4,25,26,25,2,25,25,25,12]))