class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1 if x > 0 else -1
        x = abs(x)
        num = []
        reverse = ""
        while 1:
            num.append(x % 10)
            x = int(x / 10)
            if x == 0:
                break

        for i in range(len(num)):
            reverse = reverse + str(num[i])

        reverse = int(reverse) * sign
        if reverse > 2147483648 or reverse <= -2147483648:
            return 0
        else:
            return reverse


if __name__ == "__main__":
    x = 543
    a = Solution()
    print(a.reverse(x))