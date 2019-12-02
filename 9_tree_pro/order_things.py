# -*- encoding=utf-8 -*-

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree_preorder_inorder(preorder, inorder):
    """
    前序中序建树，这个方式超级慢，而且空间大，
    :param preorder:
    :param inorder:
    :return:
    """
    if preorder is None or inorder is None or len(preorder) == 0 or len(inorder) == 0:
        return None
    if len(preorder) != len(inorder):
        return None

    root_val = preorder[0]
    new_node = TreeNode(root_val)
    if len(preorder) == 1:
        return TreeNode(root_val)
    in_root_index = inorder.index(root_val)
    if in_root_index == -1:
        return None
    if in_root_index == 0:
        new_node.right = build_tree_preorder_inorder(preorder[in_root_index + 1:], inorder[in_root_index + 1:])
    elif in_root_index == len(preorder) - 1:
        new_node.left = build_tree_preorder_inorder(preorder[1:], inorder[:in_root_index])
    else:
        new_node.left = build_tree_preorder_inorder(preorder[1: in_root_index + 1], inorder[0: in_root_index])
        new_node.right = build_tree_preorder_inorder(preorder[in_root_index + 1:], inorder[in_root_index + 1:])

    return new_node

def build_tree_preorder_inorder_1(preorder, inorder):
    """
    依然是前序中序建树，这个就快含多，而且空间小，主要是上一个用了切片。太TM慢了。
    :param preorder:
    :param inorder:
    :return:
    """
    if preorder is None or inorder is None or len(preorder) == 0 or len(inorder) == 0:
        return
    if len(preorder) == len(inorder) == 1:
        return TreeNode(preorder[0])
    in_order_map = {v: i for i, v in enumerate(inorder)}

    def build_tree(plow, phigh, ilow, ihigh):
        if phigh < plow or ilow > ihigh:
            return
        new_node = TreeNode(preorder[plow])
        in_idx = in_order_map[preorder[plow]]
        new_node.right = build_tree(in_idx-ilow+plow+ 1, phigh, in_idx + 1, ihigh) # 注意这里的plow入参必须是相对位置，因为preorder和inorder只是保持长度相同，但下标体系已经不一样了，在上一个里面我们是进行了切片，所以不需要考虑相对位置的关系
        new_node.left = build_tree(plow + 1, in_idx-ilow+plow, ilow, in_idx - 1) # # 注意这里的plow入参必须是相对位置，

        return new_node

    return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)


def build_tree_demo():
    preorder = [1, 2, 3]
    inorder = [2, 3, 1]
    build_tree_preorder_inorder_1(preorder, inorder)

if __name__ == '__main__':
    build_tree_demo()

