# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        res = 0

        while q:
            for _ in range(len(q)):
                node, prevMax = q.popleft()
                if prevMax <= node.val:
                    res += 1
                if node.left:
                    q.append((node.left, max(node.val, prevMax)))
                if node.right:
                    q.append((node.right, max(node.val, prevMax)))

        return res


