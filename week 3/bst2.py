class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BST:
    def __init__(self):
        self.root=None
        print("empty bst has been created")
    def add_node(self,data):
        new_node = node(data)
        if self.root==None:
            self.root = new_node
            return
        temp1 = self.root
        temp2 =None
        while temp1 != None:
            temp2 = temp1
            if temp1.data > new_node.data:
                temp1 = temp1.left
            else:
                temp1=temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else :
            temp2.right =new_node

    def tree_height(self,node):
        if node == None:
            return -1
        else:
            left_height= self.tree_height(node.left)
            right_height = self.tree_height(node.right)
            return 1+max(left_height,right_height)
        
bst1 = BST()
for value in [2, 3, 4, 5, 6, 7, 8, 9]:
    bst1.add_node(value)

print("Tree Height =", bst1.tree_height(bst1.root))






