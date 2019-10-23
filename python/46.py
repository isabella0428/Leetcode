class Solution1:
    def __init__(self):
        self.perm = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def Permutation(nums, tmp):
            if len(tmp) == len(nums):
                self.perm.append(tmp)

            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                Permutation(nums, tmp[:])
                tmp = tmp[:-1]

        for i in range(len(nums)):
            tmp = []
            tmp.append(nums[i])
            Permutation(nums, tmp)

        return self.perm


class Solution2:
    def __init__(self):
        self.perm = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def recursive(tmp, nums):
            if len(tmp) == len(nums):
                self.perm.append(tmp)
                return

            for item in nums:
                if item not in tmp:
                    tmp.append(item)
                    recursive(tmp[:], nums)
                    tmp.pop()

        recursive([], nums)
        return self.perm


class Solution3:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def _rec(i):
            if i == n - 1:
                ret.append(nums[:])
                return

            s = set()
            for j in range(i, len(nums)):
                if nums[j] not in s:
                    # avoid swapping same values to cause duplicates
                    s.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    _rec(i + 1)
                    nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        ret = []
        _rec(0)
        return ret


if __name__ == "__main__":
    a = Solution3()
    print(a.permute([1,1,2]))