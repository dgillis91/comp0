from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


class TreeNode:
    def __init__(self, key=None, initial_value=None):
        self.left = self.right = None
        
        self._key = key
        
        self.data = set()
        if initial_value:
            self.data.add(initial_value)

    def insert(self, data):
        token_len = len(data)
        if len(self.data) > 0:
            if token_len < self.key:
                if self.left is None:
                    self.left = TreeNode(token_len, data)
                else:
                    self.left.insert(data)
            elif token_len > self.key:
                if self.right is None:
                    self.right = TreeNode(token_len, data)
                else:
                    self.right.insert(data)
            else:
                self.data.add(data)
        else:
            self.data.add(data)
            self._key = token_len

    @property
    def key(self):
        return self._key

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.data)
        if self.right:
            self.right.print_inorder()

    def print_preorder(self):
        print(self.data)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_postorder(self):
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()
        print(self.data)
