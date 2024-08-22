from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        A.sum = A.item.val # sum
        if A.left: 
            A.sum += A.left.sum
        if A.right: 
            A.sum += A.right.sum
        left = float('-inf') 
        right = float('-inf')
        mid = A.item.val
        if A.left:
            left = A.left.max_prefix
            mid +=A.left.sum
        if A.right:
            right = mid + A.right.max_prefix
        A.max_prefix = max(left,mid,right)
        if left == A.max_prefix: # max prefix key
              A.max_prefix_key = A.left.max_prefix_key
        elif mid == A.max_prefix:
            A.max_prefix_key = A.item.key
        else:
            A.max_prefix_key = A.right.max_prefix_key        

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        
        k, s = 0, 0
        k=self.root.max_prefix_key
        s = self.root.max_prefix
        return (k, s)

def tastiest_slice(toppings):
   
    B = Part_B_Tree()   
    X, Y, T = 0, 0, 0
    length=len(toppings)
    toppings.sort(key=lambda topping :topping[0])
    for(x,y,t) in toppings:
        B.insert(Key_Val_Item(y,t))
        (mY,mT) = B.max_prefix()
        if T<mT:
            X,Y,T=x,mY,mT
    return (X, Y, T)
