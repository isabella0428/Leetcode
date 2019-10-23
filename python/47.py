class Solution:
    def __init__(self):
        self.perm = {}
        self.count = {}

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def Permutation(nums, tmp, n):
            if len(tmp) == n:
                self.perm[tuple(tmp)] = 1
                return
            for i in range(len(nums)):
                tmp_count = [k for k in range(len(tmp)) if tmp[k] == nums[i]]
                tmp_count = len(tmp_count)
                if tmp_count < self.count[nums[i]]:
                    tmp.append(nums[i])
                    Permutation(nums, tmp[:], n)
                    tmp = tmp[:-1]

        for i in range(len(nums)):
            self.count[nums[i]] = self.count.get(nums[i], 0) + 1
        length = len(nums)
        new_nums= list(self.count.keys())       #remove same values
        for i in range(len(new_nums)):
            tmp = [new_nums[i]]
            Permutation(new_nums, tmp, length)
        ret = list(self.perm.keys())
        for i in range(len(ret)):
            ret[i] = list(ret[i])
        return ret


if __name__ == "__main__":
    a = Solution()
    print(a.permuteUnique([1, 1, 2]))