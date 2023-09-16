# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        if root is None:
            root = new_node
            return root

        if val < root.val:
            if root.left is None:
                root.left = new_node
            else:
                self.insertIntoBST(root.left, val)
        else:       # val > root.val
            if root.right is None:
                root.right = new_node
            else:
                self.insertIntoBST(root.right, val)

        return root
# ---------------------------------------------------------------


def levelOrder(root):
    # prints the nodes of the tree in breadth-first order, i.e. each level
    q = []      # an empty queue, represented by a list
    print("The root node's value is: ", root.val)

    q.append(root)
    print("The queue's first element is now: ", q[0].val)

    # while not q:        # while the q is not empty
    #     print(q[0].val)  # print the first element in the queue's value
    #     q.pop(0)

    q.pop(0)

    print("The queue is now: ", q)
    # -------------------------------------------------------------------


if __name__ == '__main__':
    myTree = TreeNode(17)
    print(myTree.val)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level


