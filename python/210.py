from collections import defaultdict


class Solution1:
    def __init__(self):
        self.is_possible = True

    White = 1
    Grey = 2
    Black = 3

    def findOrder(self, numCourses, prerequisites):
        # create adjGraph
        adjGraph = defaultdict(list)
        for course, prev in prerequisites:
            adjGraph[prev].append(course)       #prev->course

        topo = []
        color = {k:Solution1.White for k in range(numCourses)}

        def dfs(node):
            if not self.is_possible:
                return

            color[node] = Solution1.Grey

            if node in adjGraph:
                for neighbour in adjGraph[node]:
                    if color[neighbour] == Solution1.White:
                        dfs(neighbour)
                    elif color[neighbour] == Solution1.Grey:
                        self.is_possible = False
            color[node] = Solution1.Black
            topo.append(node)

        for i in range(numCourses):
            if color[i] == Solution1.White:
                dfs(i)
        return topo[::-1] if self.is_possible else[]


class Solution2:
    def findOrder(self, numCourses, prerequisites):

        adjGraph = defaultdict(list)
        inDegree = {}
        for course, prev in prerequisites:
            adjGraph[prev] .append(course)
            inDegree[course] = inDegree.get(course, 0) + 1
        queue = [k for k in range(numCourses) if k not in inDegree]
        topo = []

        while len(queue) != 0:
            out = queue.pop(0)
            topo.append(out)
            for neighbour in adjGraph[out]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        return topo if len(topo) == numCourses else []


if __name__ == "__main__":
    a = Solution2()
    print(a.findOrder(2, [[1, 0]]))






# Python program for Morris Preorder traversal

# A binary tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder traversal without
# recursion and without stack
def MorrisTraversal(root):
    curr = root

    while curr:
        # If left child is null, print the
        # current node data. And, update
        # the current pointer to right child.
        if curr.left is None:
            print(curr.data, end=" ")
            curr = curr.right

        else:
            # Find the inorder predecessor
            prev = curr.left

            while prev.right is not None and prev.right is not curr:
                prev = prev.right

            # If the right child of inorder
            # predecessor already points to
            # the current node, update the
            # current with it's right child
            if prev.right is curr:
                prev.right = None
                curr = curr.right

            # else If right child doesn't point
            # to the current node, then print this
            # node's data and update the right child
            # pointer with the current node and update
            # the current with it's left child
            else:
                print(curr.data, end=" ")
                prev.right = curr
                curr = curr.left

            # Function for sStandard preorder traversal


def preorfer(root):
    if root:
        print(root.data, end=" ")
        preorfer(root.left)
        preorfer(root.right)

    # Driver program to test


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)

root.left.right.left = Node(10)
root.left.right.right = Node(11)

MorrisTraversal(root)
print("\n")
preorfer(root)

# This code is contributed by 'Aartee'
