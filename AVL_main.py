"""here we will import the Node class 
from the pypy binarytree module so that we can visualise the data well
the binarytree,Node class have value,left and right attribute"""
from binarytree import Node
from B_tree_traversal import preorder


class AVL:
    
    class Node(Node):

        # constructor of the Node class
        def __init__(self, value):
            super().__init__(value)
            self.balance_factor = 0

        def calculate_balance_factor(self):
            return AVL.height_calculator(self)

    # constructor of the AVL class

    def __init__(self):
        """the self.number_of_nodes var will increment by 1 
        whenever a node will be added to the tree and 
        decremented by 1 whenevr a node will deleted from the tree"""
        self.number_of_nodes = 0
        self.ROOT = None

        #it is a dictionary which keep track of degree of every node in a tree
        self.degree = {}

    def insert(self, current_node, value):
        """Insert a node to the tree"""
        """REMEMBER : in AVL tree after every insertion you have to
        calculate the balance factor of the Node and then balance the tree"""
        if self.ROOT == None:
            self.ROOT = self.Node(value)

        else:
            if value < current_node.value:
                if current_node.left == None:
                    newnode = self.Node(value)
                    current_node.left = newnode
                    
                else:
                    self.insert(current_node.left, value)
            else:
                if current_node.right == None:
                    newnode = self.Node(value)
                    current_node.right = newnode
                    
                else:
                    self.insert(current_node.right, value)
    
    # The balance function 
    def balance(self):
        node = self.ROOT
        def preorder(node):
            if node==None:
                return
            else:
                self.degree[node.value] = node.calculate_balance_factor()
                preorder(node.left)
                preorder(node.right)
        # finding the balance factor of every node
        preorder(node)

        # real balancing operation
        


    def delete(self):
        """Delete a Node from the tree"""

    @classmethod
    def height_calculator(cls, node):

        if node.left == None and node.right == None:
            return 0
        elif node.left == None and node.right != None:
            return 1+cls.height_calculator(node.right)
        elif node.left != None and node.right == None:
            return 1+cls.height_calculator(node.left)
        else:
            return 1+ abs(cls.height_calculator(node.left) - 1+cls.height_calculator(node.right))

    def display(self):
        print('\n\n')
        print(self.ROOT)
    
if __name__=='__main__':
    tree = AVL()
    treelist = [10, 4, 2, 1, 9, 8, 6]
    tree.insert(tree.ROOT, treelist[0])
    for item in treelist[1:]:
        tree.insert(tree.ROOT, item)
    tree.display()
    height = AVL.height_calculator(tree.ROOT)
    tree.balance()
    print(f'degree : {tree.degree}')
    