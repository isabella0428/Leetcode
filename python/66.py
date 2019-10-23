class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1
            count, digits[i] = divmod(digits[i] + count, 10)
            if not count:
                return digits
        if count:
            digits.insert(0, count)
        return digits


if __name__ == "__main__":
    a = Solution()
    print(a.plusOne([9, 9]))