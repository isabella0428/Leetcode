import math


class Solution1(object):
    # BFS
    num = 0
    def numSquares(self, n):
        toCheck = [n]
        squares = []
        for i in range(int(math.sqrt(n)) + 1):
            squares.append(i ** 2)
        while toCheck:
            self.num += 1
            temp = []
            for x in toCheck:
                for y in squares:
                    if x == y:
                        return self.num
                    if x < y:
                        break
                    temp.append(x - y)
                    toCheck = temp


class Solution2(object):
    # DP
    squares = [0]

    def numSquares(self, n):
        perfect_squares = []
        for i in range(1, int(math.sqrt(n)) + 1):
            perfect_squares.append(i * i)
        for index in range(1, n + 1):
            min_term = []
            for sqrt in perfect_squares:
                if sqrt > index:
                    break
                min_term.append(1 + self.squares[index - sqrt])
            self.squares.append(min(min_term))
        return self.squares[n]


if __name__ == "__main__":
    a = Solution2()
    print(a.numSquares(13))