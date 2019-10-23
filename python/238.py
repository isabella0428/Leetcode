class Solution1:
    # Time Limit exceeded!
    def productExceptSelf(self, nums):
        List = []
        n = len(nums)
        for i in range(n):
            product = 1
            for j in range(i + 1, i + n):
                product *= nums[j]
            nums.append(nums[i])
            List.append(product)
        return List


class Solution2:
    def productExceptSelf(self, nums):
        zero, product = [], 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(i)
        if not zero:
            for item in nums:
                product *= item
            for i in range(len(nums)):
                nums[i] = int(product / nums[i])
        else:
            if len(zero) == 1:
                for i in range(len(nums)):
                    if i == zero[0]:
                        continue
                    else:
                        product *= nums[i]
                nums[zero[0]] = product
            for i in range(len(nums)):
                if i != zero[0]:
                    nums[i] = 0
        return nums


class Solution3:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


if __name__ == "__main__":
    a = Solution3()
    print(a.productExceptSelf([1, 2,3,4]))