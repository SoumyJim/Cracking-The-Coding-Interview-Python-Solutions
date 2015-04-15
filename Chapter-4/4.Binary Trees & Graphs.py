__author__ = 'Jim'

class BinaryTreeNode:
    def __init__(self,value,left=None,right =None):
        self.value = value
        self.left = left
        self.right = right

    def getValue(self):
        return self.value

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def __str__(self):
        return '(Left->'+str(self.left)+', Value->'+str(self.value) +', Right->'+str(self.right)+')'


def pre_order_traversal(tree):
    if tree == None:
        return
    print(tree.value)
    pre_order_traversal(tree.left)
    pre_order_traversal(tree.right)

#tree_pre = BinaryTreeNode(5,BinaryTreeNode(BinaryTreeNode(BinaryTreeNode(BinaryTreeNode(1)))),BinaryTreeNode(BinaryTreeNode(BinaryTreeNode(BinaryTreeNode(9)))))
#pre_order_traversal(tree_pre)

def post_order_traversal(tree):
    if tree== None:
        return
    post_order_traversal(tree.left)
    post_order_traversal(tree.right)
    print(tree.value)

#post_order_traversal(tree_pre)

def in_order_traversal(tree):
    if tree==None:
        return
    in_order_traversal(tree.left)
    print(tree.value)
    in_order_traversal(tree.right)

#in_order_traversal(tree_pre)

#GRAPHS:

