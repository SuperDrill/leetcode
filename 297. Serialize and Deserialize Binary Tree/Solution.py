# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        # write your code here
        queue = [root]
        result = ""
        while len(queue) != 0:
            node = queue.pop(0)
            if node != None:
                result = result + str(node.val)+"." 
            else:
                result = result + "#."
            if node != None:
                queue.append(node.left)
                queue.append(node.right)
        return result
    def deserialize(self, data):
        nd = data.split(".")
        if len(nd) <=2:
            return None
        root = TreeNode(nd[0])
        nd.pop(0)
        queue = [root]
        while len(queue) != 0:
            now = queue.pop(0)
            now.left = TreeNode(nd[0]) if nd[0] != "#" else None
            nd.pop(0)
            now.right = TreeNode(nd[0]) if nd[0] != "#" else None
            nd.pop(0)
            if now.left != None:
                queue.append(now.left)
            if now.right != None:
                queue.append(now.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))