""" Here preorder or inorder or Postorder will be providedd by the user and 
    this program will create BST according to the user needs """
from B_tree_traversal import preorder
from bst import BST
from collections import deque

# generator

root = None
preorder_list = deque([20, 16, 5, 18, 17, 19, 60, 85, 70])


def from_inorder(inord_list):
    global root
    global preorder_list
    # print("\n\n[ CONSTRUCTION FROM INORDER ]\n")

    # we need preorder list or post order list for this , we will use preorder here

    item = preorder_list[0]
    trash = preorder_list.popleft()
    index_at_inorder_list = inord_list.index(item)
    left_subtree = inord_list[:index_at_inorder_list]
    right_subtree = inord_list[index_at_inorder_list+1:]
    newnode = BST.Node(item)
    if root == None:
        root = newnode
    if len(left_subtree) == 0 and len(right_subtree) == 0:
        return newnode
    elif len(left_subtree) == 0 and len(right_subtree) != 0:
        newnode.right = from_inorder(right_subtree)
    elif len(left_subtree) != 0 and len(right_subtree) == 0:
        newnode.left = from_inorder(left_subtree)
    else:
        newnode.left = from_inorder(left_subtree)
        newnode.right = from_inorder(right_subtree)
    
    return newnode  # understand this line well


def from_preorder(preord_list):
    print("\n\n[ CONSTRUCTION FROM PREORDER ]\n")
    pre_tree = BST()
    for item in preord_list:
        pre_tree.insert(pre_tree.ROOT, item)
    pre_tree.displayTree(pre_tree.ROOT)
    print()


def from_postorder(postord_list):
    # it will return root of the Created tree
    print("\n\n[ CONSTRUCTION FROM POSTORDER ]\n")
    post_tree = BST()
    for item in postord_list[::-1]:
        post_tree.insert(post_tree.ROOT, item)
    post_tree.displayTree(post_tree.ROOT)
    print()

def universal_display(root_node):
    if root_node == None:
            return
    else:
        print(root_node.data, end=',')
        universal_display(root_node.left)
        universal_display(root_node.right)


if __name__ == '__main__':
    input_postorder_list = [5, 17, 19, 18, 16, 70, 85, 60, 20]
    input_preorder_list = [20, 16, 5, 18, 17, 19, 60, 85, 70]
    input_inorder_list = [5, 16, 17, 18, 19, 20, 60, 70, 85]
    from_inorder(input_inorder_list)
    from_preorder(input_preorder_list)
    universal_display(root)
    
    
    
