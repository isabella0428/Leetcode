class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        prev, start = nums[0], nums[0]
        ret = []
        for item in nums[1:]:
            if item == prev + 1:
                prev = item
                continue
            else:
                if start == prev:
                    ret.append(str(start))
                else:
                    ret.append(str(start) + '->' + str(prev))
                start = item
                prev = item
        if start == prev:
            ret.append(str(start))
        else:
            ret.append(str(start) + '->' + str(prev))
        return ret


if __name__ == "__main__":
    a = Solution()
    print(a.summaryRanges([0,1,2,4,5,7]))