class Solution:
    def findCircleNum(self, M: 'List[List[int]]') -> 'int':
        def findFriend(i):
            for friend, relation in enumerate(M[i]):
                if relation and friend not in seen:
                    seen.add(friend)
                    findFriend(friend)

        seen = set()
        circle = 0
        for i in range(len(M)):
            if i not in seen:
                findFriend(i)
                circle += 1
        return circle


if __name__ == "__main__":
    a = Solution()
    print(a.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))