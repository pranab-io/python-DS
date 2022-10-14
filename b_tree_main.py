class BTree:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    # Constructor of the BTree
    def __init__(self):
        self.number_of_nodes = 0
        data = (input("Enter The grand root data : "))
        self.ROOT = self.createTree(data)

    # Fully functional code

    def createTree(self, data):

        newnode = self.Node(data)
        self.number_of_nodes += 1

        if data == '-1':
            return None
        else:
            newnode.data = data

        lchild_data = (input(f'Enter left child of {newnode.data} : '))
        newnode.left = self.createTree(lchild_data)
        rchild_data = (input(f'Enter Right child of {newnode.data} : '))
        newnode.right = self.createTree(rchild_data)

        return newnode

    def max_no_of_nodes(self, n=1):
        if self.number_of_nodes in range(2**(n-1), ((2**n))):
            return 2**(n-1)-1
        else:
            n += 1
            return self.max_no_of_nodes(n)

    def array_representation(self):
        pass
        

    @classmethod
    def displayTree(cls, RootNode):
        if RootNode == None:
            return
        else:
            print(RootNode.data, end=',')
            BTree.displayTree(RootNode.left)
            BTree.displayTree(RootNode.right)

    


if __name__ == '__main__':
    # creation of BTree

    Bt = BTree()
    # v = Bt.ROOT
    BTree.displayTree(Bt.ROOT)
    print("\nThe max number of nodes : ", Bt.max_no_of_nodes())
