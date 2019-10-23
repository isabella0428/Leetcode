class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        space = False
        bit = False
        sign = 1
        sum = 0
        for i in str:
            if i == " " and space == False:
                continue
            if space == False and i == "-" and bit == False:
                sign = -1
                bit = True
                space = True
                continue
            if space == False and i == "+" and bit == False:
                bit =True
                space = True
                continue
            if "0" <= i <= "9":
                sum = sum * 10 + int(i)
                space = True
                continue
            break

        sum = sum * sign

        if sum > 2147483647:
            return 2147483647
        if sum < -2147483648:
            return -2147483648

        return sum


if __name__ == "__main__":
    a = Solution()
    print(a.myAtoi("0-1"))



