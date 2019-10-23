class Solution1:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1 = len(a) - 1
        l2 = len(b) - 1
        count = 0
        result = ""
        while l1 > -1 or l2 > -1:
            val1 = int(a[l1]) if l1 > -1 else 0
            val2 = int(b[l2]) if l2 > -1 else 0
            count, val = divmod(val1 + val2 + count, 2)
            result = str(val) + result
            l1 -= 1
            l2 -= 1
        if count:
            result = str(count) + result
        return str(result)


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        m = max(len(a), len(b))
        ret = []  # reverse
        carry = 0
        for i in range(-1, -m - 1, -1):
            item1 = int(a[i]) if abs(i) <= len(a) else 0
            item2 = int(b[i]) if abs(i) <= len(b) else 0
            carry, val = divmod(item1 + item2 + carry, 2)
            ret.append(str(val))
        if carry:
            ret.append(str(carry))
        ret.reverse()
        return "".join(ret)


if __name__ == "__main__":
    a = Solution2()
    print(a.addBinary("11", "1"))