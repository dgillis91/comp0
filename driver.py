from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import argparse
from readers import FileReaderDriver, KeyboardReaderDriver


parser = argparse.ArgumentParser()
parser.add_argument('path', nargs='?', help='path to file. do not include ext. defaults to read from keyboard')
args = parser.parse_args()

if args.path is None:
    print('reading from keybaord. press CTRL+D to stop')
    driver = KeyboardReaderDriver()
    tree = driver.parse()
else:
    driver = FileReaderDriver(args.path)
    tree = driver.parse_file()

print('***printing preorder***')
tree.print_preorder()

print('***printing postorder***')
tree.print_postorder()

print('***printing inorder***')
tree.print_inorder()
