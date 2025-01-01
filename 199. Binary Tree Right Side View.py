import collections

from fiona import collection


def rightSideView(root):
    """
    the idea of the sol - we run a dfs, for every level we will take the right node for the res
    :param root:  root of the tree
    :return: the nodes than we can see from the right - list of those nodes
    """
    res = []


    def bfs(node):
        q = collections.deque()
        q.append(node)
        while q:
            level = []
            q_length = len(q)
            for i in range(q_length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level[-1])
    bfs(root)
    return res