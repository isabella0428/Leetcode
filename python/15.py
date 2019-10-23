class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        counts = {}
        for s in range(len(nums)):
            counts[nums[s]] = counts.get(nums[s], 0) + 1

        ans = {}

        edge = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                edge = i
                break

        for i in range(edge):
            n1 = nums[i]
            for j in range(edge, len(nums)):
                n2 = nums[j]
                c = - (nums[i] + nums[j])
                if counts.get(c, 0):
                        if (c == n1 and counts.get(n1) == 1) or (c == n2 and counts.get(n2) == 1):
                            continue
                        else:
                            tmp = [n1, n2, c]
                            tmp.sort()
                            ans[tuple(tmp)] = 1

        if counts.get(0) and counts.get(0) >= 3:
            ans[(0, 0, 0)] = 1
        ans = list(ans.keys())
        ans.sort()
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.threeSum([-1, 0, 1, 2, -1, -4]))