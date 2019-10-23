class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def recursive(tmp, nums):
            if not nums:
                tmp.sort()
                if tmp not in subset:
                    subset.append(tmp)
                return
            recursive(tmp[:], nums[1:])
            tmp.append(nums[0])
            recursive(tmp[:], nums[1:])
            tmp.pop()

        recursive([], nums)
        subset.sort()
        return subset


if __name__ == "__main__":
    a = Solution()
    print(a.subsetsWithDup([1, 2, 2]))