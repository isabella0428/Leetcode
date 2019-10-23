class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        Degree = [[] for i in range(numCourses)]
        for item in prerequisites:
            lesson, pre = item[0], item[1]
            Degree[lesson].append(pre)
        stack, visited = [], 0
        for i in range(numCourses):
            if not Degree[i]:
                stack.append(i)
                visited += 1
        while stack:
            lesson = stack.pop()
            for i in range(numCourses):
                if lesson in Degree[i]:
                    Degree[i].remove(lesson)
                    if not Degree[i]:
                        stack.append(i)
                        visited += 1
            if visited == numCourses:
                return True
        return False


if __name__ == "__main__":
    a = Solution()
    print(a.canFinish(2, [[1, 0]]))