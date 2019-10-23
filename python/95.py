class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            for i in range(start, end + 1):
                left_tree = generate_trees(start, i - 1)
                right_tree = generate_trees(i + 1, end)

                for l in left_tree:
                    for r in right_tree:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees
        return generate_trees(1, n) if n else []
