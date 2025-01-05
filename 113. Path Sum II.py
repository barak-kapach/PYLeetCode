# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
idea -  we can run a DFS or inorder travel and hold the list 
of the current path, if we get null we can return withhout append a copy
"""
def pathSumW(root, targetSum):
    #sol with pop - we can use the recursive stack  to store the path we do that below
    res = []
    def inorder(node, path):
        if node is None:
            return
        path.append(node.val)
        if sum(path) == targetSum and (not node.left and not node.right):
            res.append(path[:])
        inorder(node.left, path )
        inorder(node.right, path )
        path.pop()

    inorder(root, [])
    return res


def pathSumTryWithRecursionStac(root, targetSum):
    # sol with pop - we can use the recursive stack  to store the path we do that below
    res = []

    def inorder(node, path):
        if node is None:
                if sum(path) == targetSum:
                    res.append(path[:])
                    # return
            # return
        # path.append(node.val)
        # if sum(path) == targetSum and not node:
        #     res.append(path[:])
        inorder(node.left, path + [node.val])
        inorder(node.right, path + [node.val])
        # path.pop()

    inorder(root, [])
    return res


#check
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
print(pathSumW(root, 22))  # [[5, 4, 11, 2], [5, 8, 4, 5]]