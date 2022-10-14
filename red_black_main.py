"""Implementation of red black tree"""
from binarytree import Node
class RBTree:

    class NODE(Node):
        def __init__(self,value):
            super().__init__(self,value)
            self.color = 'red'
    
    # Tree's constructor
    def __init__(self):
        self.ROOT = None


    def insert(self):
        pass