import collections

from fiona import collection


def levelOrder(root):
    #initialize a queue for BFS
    q = collections.deque()
    q.append(root)

    #initialize a list to store the result
    res = []

    while q:
        level = []
        #we need to know the length of the queue before we add new elements
        q_length = len(q)
        for i in range(q_length):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        #handle the case that the level is not empty - because we add None to the queue
        if level:
            res.append(level)
    return res
