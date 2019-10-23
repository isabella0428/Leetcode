import math


class Solution1:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Time Limit Exceeded!
        dicts = {}
        for i, v in enumerate(nums):
            for j in range(max(0, i - k), i):
                tmp = nums[j]
                if abs(tmp - v) <= t:
                    return True
            dicts[v] = i
        return False


class Solution2:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Bucket-sort
        if t < 0:
            return False
        d = {}
        w = t + 1   # To keep an appropriate interval
        for i in range(len(nums)):
            m = math.floor(nums[i] / w)
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[math.floor(nums[i - k] / w)]
        return False


if __name__ == "__main__":
    a = Solution2()
    print(a.containsNearbyAlmostDuplicate([-3, 3], 2, 4))