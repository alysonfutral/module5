"""
File that contains multiple methods to iterator over binary tree.
    PreOrderIterator, PostOrderIterator, InOrderIterator (new methods)
    Create unit tests for all NEW ITERATORS (COVER ALL POSSIBILITIES)
        and a test that a binary tree can be included in a for loop for
        in order traversal


"""

class BinaryTreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.parent = None
        self._left_child = left_child
        self._right_child = right_child
        if left_child:
            left_child.parent = self
        if right_child:
            right_child.parent = self

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, r):
        self._root = r

    def iter(self): # must return an InOrderIterator over the tree
        pass

class PreOrderIterator():
    pass

class PostOrderIterator():
    pass

class InOrderIterator():
    pass


# sample
if __name__ == '__main__':
    n1 = BinaryTreeNode("A")
    n2 = BinaryTreeNode("B")
    n3 = BinaryTreeNode("C", n1, n2)
    n4 = BinaryTreeNode("D")
    n5 = BinaryTreeNode("E", n4, n3)
    n6 = BinaryTreeNode("F", n5)
    n7 = BinaryTreeNode("G")
    n8 = BinaryTreeNode("H", n6, n7)
    tree = BinaryTree(n8)
    print(tree.root.value)
    print(tree.root.left_child.left_child.value)
