from scipy.ndimage import rotate


def searchBST(root, val):
    """
    easy problem - we implement a search func in BST - we need to do than on O(log(n)) time comp

    :param root:
    :param val:
    :return: the node with the val target - with his subtree
    """
    node = root
    while node:
        # case 1 - node val > target val -> we need to check in the left subtree
        if node.val > val:
            node = node.left
        #case 2 - node vak < target val -> we need to check in the right subtree
        elif node.val< val:
            node = node.right
        #case 3 - we are on the relevant node
        else:
            return node
    return None