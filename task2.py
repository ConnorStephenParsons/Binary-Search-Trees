class BinTreeNode(object):
 
    def __init__(self, value):
        """Tree node constructor"""
        self.value=value                                          #Data Value
        self.left=None                                            #Left Child
        self.right=None                                           #Right Child
 
       
def tree_insert( tree, value):
    if(tree==None):
        tree=BinTreeNode(value)
    else:
        if(value < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(value)
            else:
                tree_insert(tree.left,value)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(value)
            else:
                tree_insert(tree.right,value)
    return tree


    
    
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)                                           #Start at left most leaf
    if(tree.right!=None):
        postorder(tree.right)                                          #Bubble up from the bottom left most sub tree to the right until reach the root
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)                           
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)                          

        
def preorder(tree):
    """Function that sets the layout of the tree traversal in pre-order ready to be called and printed in that format"""
    print(tree.value)
    if(tree.left!=None):
        preorder(tree.left)                                            #Visit node, traverse left child
    if(tree.right!=None):
        preorder(tree.right)                                           #If at leaf, go back and traverse right nodes
        
        
def MinimumNodeValue(tree):   
    """sets a minimum node value for the BST when deleting, so it cannot traverse past it"""
    currentnode = tree
    
    while(currentnode.right != None):
        currentnode = currentnode.right
        
    return currentnode    
        
        
        
def nodedeleter(tree, value):
    """A function which allows a node in the binary search tree to be deleted"""
    if(tree == None):
        return tree                                                      #Sets a base case
    
    elif(value < tree.value):                                            
        tree.left = nodedeleter(tree.left, value)                        #If value to be deleted is smaller than the roots, then it is a left child
        
    elif(value > tree.value):
        tree.right = nodedeleter(tree.right, value)                      #If value to be deleted is larger than the roots, then it is a right child
        
    else:
        if(tree.left == None):                                           #Node with one child or no children
            temporaryvalue = tree.right
            tree = None
            return temporaryvalue
        
        elif(tree.right == None):
            temporaryvalue = tree.left
            tree = None
            return temporaryvalue
        
        temporaryvalue = MinimumNodeValue(tree.right)                    #A node with 2 children - get the smallest child on the right of the node using a tempory value pointer
        tree.value = temporaryvalue.value                                #Get the content of this node (in_order children)
        tree.right = nodedeleter(tree.right, temporaryvalue.value)       #Delete this node
    return tree                                                           #Return the tree with the deleted node value
        
      


#####################################################################################################################
    
#################################################################################################################

def bin_tree_find(tree, target):
    if(tree == None):
        return False
    elif(tree.value == target):
        return True
            
    elif(target < tree.value):
        print(tree.value)
        return bin_tree_find(tree.left, target)
    else:
        print(tree.value)
        return bin_tree_find(tree.right, target)
    
    return False
            
            
 
if __name__ == '__main__':
    
    ######################################
    tree = tree_insert(None, 10);
    tree = tree_insert(tree, 8)
    tree = tree_insert(tree, 5)
    tree = tree_insert(tree, 9)
    tree = tree_insert(tree, 14)
    tree = tree_insert(tree, 12)
    tree = tree_insert(tree, 11)
    tree = tree_insert(tree, 13)
    tree = tree_insert(tree, 17) 
    in_order(tree)
    
    ########################################
        
      

    tree = nodedeleter(tree, int(input("please select a node to delete from the ordered BST above: ")))    
    print("in order traversal with the selected node removed is: ")    
    in_order(tree)


#print("BST in, in-order is: ")
#in_order(tree)
    
