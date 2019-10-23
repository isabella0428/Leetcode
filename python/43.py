class Solution1:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        count = 0
        total = 0
        local = ""
        for m2 in range(len(num2) - 1, -1, -1):
            for m1 in range(len(num1) - 1, -1, -1):
                count, partial = divmod(int(num2[m2]) * int(num1[m1]) + count, 10)
                local = str(partial) + local
            if count != 0:
                local = str(count) + local
                count = 0
            total += int(local) * 10 ** (len(num2) - 1 - m2)
            local = ""
        return str(total)


class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        sum, carry, base = 0, 0, 1
        if len(num1) < len(num2):
            num2, num1 = num1, num2
        num1, num2 = list(num1)[::-1], list(num2[::-1])
        for d2 in num2:
            # num2 :shorter
            carry, d, tmp = 0, base, 0
            for d1 in num1:
                d2, d1 = int(d2), int(d1)
                carry, val = divmod(d2 * d1 + carry, 10)
                tmp += val * d
                d *= 10
            if carry != 0:
                tmp += d * carry
            sum += tmp
            base *= 10
        return str(sum)


if __name__ == "__main__":
    a = Solution2()
    print(a.multiply("999", "999"))