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
            if node: # null이 아닌 경우
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: # null인 경우
                result.append('#')

        return ' '.join(result)  # 문자열로 변환

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        queue = collections.deque()  # 부모노드들을 넣어준다
        data = data.split()  # 배열로 변환 

        if data:
            root = TreeNode(int(data.pop(0)))
            queue.append(root)

        else: #예외처리
            return None

        while queue:
            node = queue.popleft()
            left = data.pop(0) # pop의 중복을 막기위해 변수에 할당
            right = data.pop(0)

            if left != '#':
                node.left = TreeNode(int(left))
                queue.append(node.left)

            if right != '#':
                node.right = TreeNode(int(right))
                queue.append(node.right)

        return root