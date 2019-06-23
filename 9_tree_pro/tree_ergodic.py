# -*- encoding=utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def binary_tree_in_order(tree):
    """

    :param tree:
    :return:
    """
    result = []
    stack = [tree]
    while len(stack) != 0:
        if stack[-1].left is None:
            tmp = stack.pop()
            result.append(tmp.data)
            if tmp.right is not None:
                stack.append(tmp.right)
        else:
            stack.append(stack[-1].left)
    return result



def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    # 用于递归判断树的每个节点是否相同
    # 需要注意的地方是: 前两个if语句不可以颠倒顺序
    # 如果颠倒顺序, 会先判断pRoot1是否为None, 其实这个时候pRoot2的结点已经遍历完成确定相等了, 但是返回了False, 判断错误
    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1haveTree2


