class Solution1:
    def __init__(self):
        self.memo = [None, 1]
        self.ans = ""

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def fact (n):
            def fact (_n,  acc):
                if _n == n:
                    return acc
                else:
                    return fact(_n + 1, acc * n)
            return fact(1, 1)

        def get_num(n):             # self.memo[0] is empty
            if n == 1:
                return 1
            if self.memo[n]:
                return self.memo[n]
            self.memo[n] = get_num(n - 1) * n
            return self.memo[n]

        def Findkth(n, ret, rest, k):
            if len(rest) == 1:
                return ret + str(rest[0])

            first_loc, k = divmod(k, (get_num(n) / n))
            if k == 0:
                first_loc -= 1
            first_loc = int(first_loc)
            ret += str(rest[first_loc])
            rest.pop(first_loc)
            return Findkth(n - 1, ret, rest, k)

        if n == 1:
            return [1]
        self.memo = [None for i in range(n + 1)]        # 0 empty
        first_loc, k = divmod(k, (get_num(n) / n))
        if k == 0:
            first_loc -= 1
        first_loc = int(first_loc)
        rest = list(range(1, n + 1))
        ret = str(rest[first_loc])
        rest.pop(first_loc)
        return Findkth(n - 1, ret, rest, k)


class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(n):
            def fact(_n, multi):
                if _n == n:
                    memo[n] = n * multi
                    return memo[n]
                else:
                    memo[_n - 1] = multi
                    return fact(_n + 1, _n * multi)

            if memo[n] != -1:
                return memo[n]
            return fact(1, 1)

        memo = [-1 for i in range(n + 1)]
        memo[0], memo[1] = 1, 1
        ret, rest = [], list(range(1, n + 1))
        for i in range(n):
            num = fact(n - i) / (n - i)
            index, k = divmod(k, fact(n - i) / (n - i))
            index = int(index)
            if k != 0:
                index += 1
            ret.append(str(rest[index - 1]))
            rest.pop(index - 1)
        return "".join(ret)


if __name__ == "__main__":
    a = Solution2()
    print(a.getPermutation(1, 1))