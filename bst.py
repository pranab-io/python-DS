from B_tree_traversal import inorder,inorder_list


class BST:
    to_be_deleted_node = None
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.ROOT = None

    def insert(self, current_node, val):
        if self.ROOT == None:
            self.ROOT = self.Node(val)

        else:
            if val < current_node.data:
                if current_node.left == None:
                    newnode = self.Node(val)
                    current_node.left = newnode
                else:
                    self.insert(current_node.left, val)
            else:
                if current_node.right == None:
                    newnode = self.Node(val)
                    current_node.right = newnode
                else:
                    self.insert(current_node.right, val)

    def searchElement(self, val, current_node):
        """
        val = the value you want to search,
        current_node = The current Node
        """
        if current_node == None:
            print("value not found exiting ........")
            exit()
        else:
            if val == current_node.data:
                return current_node
            elif val < current_node.data:
                return self.searchElement(val, current_node.left)
            else:
                return self.searchElement(val, current_node.right)

    def delete(self, value):
        inorder(self.ROOT) # list will be generated
        """deletion 
            1/ when there is no child of the node :
                ---> directly delete that Node
            2/ when There is One child of the node:
                ---> replace the node with the child Node
            3? when there is Two child of the node :
                ---> replace the node with its inorder predecessor
                OR
                ---> replace the node with its in order successor"""
        BST.to_be_deleted_node = self.searchElement(value, self.ROOT)

        # implementation of condition 1
        if BST.to_be_deleted_node.left == None and BST.to_be_deleted_node.right == None:
            BST.to_be_deleted_node.data = None
        # implementation of condition 2
        elif BST.to_be_deleted_node.left == None or BST.to_be_deleted_node.right == None:
            if BST.to_be_deleted_node.left == None:
                BST.to_be_deleted_node.data = BST.to_be_deleted_node.right.data
                BST.to_be_deleted_node.right.data = None
            else:
                BST.to_be_deleted_node.data = BST.to_be_deleted_node.left.data
                BST.to_be_deleted_node.left.data = None

        # implementation of condition 3 // when there is two child of the node
        else:
            choose = int(input("""
             choose one -->
                1/ inorder predecessor as replacement
                2/ inorder successor as replacement
                
                Choose one : """))

            if choose == 1:
                inord_pred_value = inorder_list[(
                    inorder_list.index(BST.to_be_deleted_node.data)) - 1]
                # first delete the node then replace its value with deleted node value
                pred_index = (inorder_list.index(BST.to_be_deleted_node.data)) - 1
                inorder_list[pred_index] = None
                BST.to_be_deleted_node.data = inord_pred_value

            if choose == 2:
                inord_succ_value = inorder_list[(
                    inorder_list.index(BST.to_be_deleted_node.data)) + 1]
                # first delete the node then replace its value with deleted node value
                succ_index = (inorder_list.index(BST.to_be_deleted_node.data)) + 1
                inorder_list[succ_index] = None
                BST.to_be_deleted_node.data = inord_succ_value

    @classmethod
    def displayTree(cls, RootNode):
        if RootNode == None:
            return
        else:
            print(RootNode.data, end=',')
            BST.displayTree(RootNode.left)
            BST.displayTree(RootNode.right)


if __name__ == '__main__':
    tree = BST()
    treelist = [10, 4, 2, 1, 9, 8, 6]
    tree.insert(tree.ROOT, treelist[0])
    for item in treelist[1:]:
        tree.insert(tree.ROOT, item)
    tree.displayTree(tree.ROOT)
    tree.delete(4)
    print()
    print("After deleting....the value 4 ..")
    tree.displayTree(tree.ROOT)
