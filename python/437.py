class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        def countPath(node, sum):
            if not node:
                return 0
            count = 0
            if node.val == sum:
                count += 1
            count += countPath(node.left, sum - node.val)
            count += countPath(node.right, sum - node.val)
            return count

        if not root:
            return 0
        count = countPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return count
