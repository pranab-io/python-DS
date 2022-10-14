# here we will code the logic of Binary Tree traversal
# Inorder [Left , Root , Right]
# Preorder [root,left,right]
# Postorder [left,right,root]

from b_tree_main import BTree

inorder_list = []
def inorder(root):

    #terminating condition
    if root==None:
        return
    else:

        inorder(root.left)
        # print(root.data,end=', ')
        # if you want to store in a list uncomment the below line
        inorder_list.append(root.data)
        inorder(root.right)


def preorder(root):
    
    if root==None:
        return
    else:
        print(root.data,end=', ')
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root==None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=', ')


if __name__ == '__main__':
    bt = BTree()
    print('inorder representation : ',inorder(bt.ROOT))
    print('preorder representation : ',preorder(bt.ROOT))
    print('postorder representation : ',postorder(bt.ROOT))
