class MySolution:
    # Time Exceeded
    def grayCode(self, n: 'int') -> 'List[int]':
        def recursive(grey, tmp):
            nonlocal code
            if len(tmp) == 2 ** n:
                code.append(tmp)
                return
            for i in range(n):
                cur = grey[:i] + str(1 - int(grey[i])) + grey[i + 1:]
                if cur not in tmp:
                    tmp.append(cur)
                    recursive(cur, tmp[:])
                    tmp.pop()
        if n == 0:
            return [0]
        code = []
        grey = '0' * n
        for i in range(n):
            tmp = [grey]
            cur = grey[:i] + str(1 - int(grey[i])) + grey[i + 1:]
            tmp.append(cur)
            recursive(cur, tmp[:])
        for item in code:
            for i in range(len(item)):
                item[i] = int(item[i], 2)
        return code[-1]


class Solution1:
    # @return a list of integers
    '''
    from up to down, then left to right

    0   1   11  110
            10  111
                101
                100

    start:      [0]
    i = 0:      [0, 1]
    i = 1:      [0, 1, 3, 2]
    i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
    '''
    def grayCode(self, n):
        result = [0]
        for i in range(n):
            result += [x + pow(2, i) for x in reversed(result)]
        return result


class Solution2:
    def grayCode(self, n: 'int') -> 'List[int]':
        ans = []
        for i in range(1 << n):
            q = i >> 1          # i / 2
            p = i ^ q           # based on digits
            ans.append(i ^ i >> 1)  # G(i) ^ G(n-1)
        return ans


if __name__ == "__main__":
    a = Solution2()
    print(a.grayCode(5))

