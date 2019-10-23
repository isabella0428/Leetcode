class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        for i, val in enumerate(nums):
            n = n ^ i ^ val
        return n


if __name__ == "__main__":
    a = Solution()
    print(a.missingNumber([9,6,4,2,3,5,7,0,1]))