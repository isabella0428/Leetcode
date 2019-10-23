class Solution:
    # Space consuming
    def majorityElement(self, nums):
        dicts, ret = {}, []
        n = int(len(nums) / 3)
        for item in nums:
            dicts[item] = dicts.get(item, 0) + 1
        for i in list(dicts.keys()):
            if dicts[i] > n:
                ret.append(i)
        return ret

class Solution:
    # Boyer-Moore Majority Vote algorithm
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]


if __name__ == "__main__":
    a = Solution()
    print(a.majorityElement([1,1,1,3,3,2,2,2]))
