# Require compatibility for python 2. Pull commmon
# changes.
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from tree import TreeNode


DEFAULT_FILE_EXT = '.sp2020'


# In python3, raw_input is input
try:
    input = raw_input
except NameError:
    pass


class FileReaderDriver:
    def __init__(self, filename):
        self._filename = filename + DEFAULT_FILE_EXT

    def parse_file(self):
        tree = TreeNode()
        tokens = self._tokenize()
        for token in tokens:
            tree.insert(token)
        return tree

    def _tokenize(self):
        with open(self._filename, 'r') as input_file:
            return input_file.read().split()


class KeyboardReaderDriver:
    def __init__(self):
        pass

    def parse(self):
        tree = TreeNode()
        while True:
            try:
                tree.insert(input())
            except EOFError:
                break
        return tree
