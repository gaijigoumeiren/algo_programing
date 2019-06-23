# -*- encoding=utf-8 -*-

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildtree_inorder_preorder(inorder, preorder):
    """
    前序和中序建树
    :param inorder:
    :param preorder:
    :return:
    """
    if inorder is None or preorder is None or len(inorder) == 0 or len(preorder) == 0:
        return
    if len(inorder) != len(preorder):
        return

    new_node = TreeNode(inorder[0])
    


