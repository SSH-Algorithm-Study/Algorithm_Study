import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = collections.deque()

        if root:
            queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        return result


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        queue = collections.deque()  # 부모노드들을 넣어준다

        if data:
            root = TreeNode(data.pop(0))
            queue.append(root)

        while queue:
            node = queue.popleft()
            if data and data.pop(0):
                left = TreeNode(data.pop(0))
                node.left = left
                queue.append(left)

            if data and data.pop(0):
                right = TreeNode(data.pop(0))
                node.right = right
                queue.append(right)

        return root



def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    queue = collections.deque()  # 부모노드들을 넣어준다
    i = -1
    length = len(data)

    if data:
        root = TreeNode(data[0])
        queue.append(root)

    while queue:
        i += 1
        node = queue.popleft()
        if i*2+1 < length:
            if data[i*2+1]:
                left = TreeNode(data[i*2+1])
                node.left = left
                queue.append(left)
            else:
                node.left = None

        if i * 2 + 2< length:
            if data[i * 2 + 2]:
                right = TreeNode(data[i * 2 + 2])
                node.right = right
                queue.append(right)
            else:
                node.right = None

    return root