class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        a, b, ret = 0, 0, 0
        for num in nums:
            ret ^= num
        mask = 1
        while mask & ret == 0:
            mask = mask << 1
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == "__main__":
    a = Solution()
    print(a.singleNumber([1, 2, 1, 3, 2, 5]))