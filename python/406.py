class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # try to guarantee that the newly added item will not change
        # the previous state of the former
        # here sort their value in ascending order
        if not people:
            return []
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        ans = [people[0]]
        for item in people[1:]:
            if item[1] == len(ans):
                ans.append(item)
            else:
                ans.insert(item[1], item)
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))