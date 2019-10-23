from collections import Counter


class Solution1:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)   # type collections.Counter
        array = [val == 1   for item, val in count.items()]
        index = array.index(True)
        return list(count.keys())[index]  # Counter({2: 1, 1: 2, 4: 1, 5: 1}) element:count


class Solution2:
    # list operation
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_list = [[]]
        for item in nums:
            flag = False
            for element in element_list:
                if element == item:
                    flag = True
            if flag:
                element_list.remove(item)
            else:
                element_list.append(item)
        return element_list[-1]


class Solution3:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for item in nums:
            try:
                dict.pop(item)
            except:
                dict[item] = 1
        return dict.popitem()[0]


class Solution4:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # math:2∗(a+b+c)−(a+a+b+b+c)=c
        return 2 * sum(list(set(nums))) - sum(nums)


class Solution5:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 4: Bit Manipulation
        # Concept
        #
        # If we take XOR of zero and some bit, it will return that bit
        # a ⊕ 0 = a
        # If we take XOR of two same bits, it will return 0
        # a ⊕ a = 0
        # a ⊕ b ⊕ a = (a ⊕ a) ⊕ b = 0 ⊕ b = b
        a = 0
        for item in nums:
            a ^= item
        return a


if __name__ == "__main__":
    a = Solution5()
    print(a.singleNumber([4, 1, 2, 1, 2]))



