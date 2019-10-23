class Solution:
    def findDuplicate(self, nums):
        dicts = {}
        for item in nums:
            if item in dicts:
                return item
            else:
                dicts[item] = True
