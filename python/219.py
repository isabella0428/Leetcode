class Solution1:
    def containsNearbyDuplicate(self, nums, k: int):
        # brute force: Time Limit Exceeded!
        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False


class Solution2:
    def containsNearbyDuplicate(self, nums, k):
        # optimized brute force: hash table -> Time Limit Exceeded!
        for i in range(len(nums)):
            item = nums[i: min(i + k + 1, len(nums))]
            if len(set(item)) < len(item):
                return True
        return False


class Solution3:
    def containsNearbyDuplicate(self, nums, k):
        # one pass
        dicts = {}
        for i, v in enumerate(nums):
            if v in dicts and i - dicts[v] <= k:
                return True
            dicts[v] = i
        return False


if __name__ == "__main__":
    a = Solution3()
    print(a.containsNearbyDuplicate([1, 2, 3, 1], 3))






