files = open("paragraph.txt", "r").read()
paragraph = files.split() 

       
class BinTreeNode(object):
 
    def __init__(self, value):
        """Tree node constructor"""    
        self.value=value                                              #data value
        self.left=None                                                #left child    
        self.right=None                                               #right child
        self.counter = 1                                              #counter to initialize frequency
 
def TreeTesting(BinTreeNode):
    """Tesitng a couple of aspects of the tree construction."""
    if(BinTreeNode == None):
        return BinTreeNode                                             #Returning False, if a child node is inserted the wrong way (larger number nodes should go right)
    elif(self.right < self.value):
        return False                                                   #Returning False if a node is inserted the wrong way (lower number nodes should go down the neft of the tree)
    elif(self.left > self.value):
        return False




def tree_insert(tree, item):
    """insertion of a new node"""
    if(tree==None):
        tree=BinTreeNode(item)                  
        
    else:
        if item == tree.value:
            tree.counter = counter +1                                   #adds 1 to the counter for the word in the tree (every time it occurs - for the frequency
            
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)                             #data we want to insert is the left child if it is smaller than the current nodes value 
            else:
                tree_insert(tree.left,item)                             #or create a new node and assign it as the left child for that data
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)                            #data we want to insert is set as the right child if it is larger than the current nodes value
            else:
                tree_insert(tree.right,item)                            #or create new node and assign it as right child for that data
    return tree                                                         #returns the structured tree


def count_children(next):
    """takes a reference by counter for the child nodes within the tree, ready for the deletion function and frequencies"""
    count == None
    if(next.left != 0):
        count = count +1

    if(next.right != 0):
        count = count+1

    return count




def bin_tree_find(tree, target):
    if(tree == None):                                                     #Checks to see if the root node value is null
        return False
    elif(tree.value == target):                                           #If current node contains data we are looking for, we return it as true
        return True
            
    elif(target < tree.value):                                            #Checks if node we are looking at is less that the tree roots current value
        print(tree.value)
        return bin_tree_find(tree.left, target)                           #If it is, then it is assigned to the left of the tree (as a child)        
    else:
        print(tree.value)
        return bin_tree_find(tree.right, target)                          #in any other, case, its assigned as the right child
    
    return False
    

   
def preorder(tree):
    """Function which sets the layout of the graph in preorder - allowing it to be called and printed"""
    print(tree.value, tree.counter)                                       #Prints value of the current node
    if(tree.left!=None):                                                  #If there is a traversal on the left child, it calls pre_order to it
        preorder(tree.left)
    if(tree.right!=None):                                                 #if there is a treversal on the right child, its calls pre_order to that
        preorder(tree.right) 

#############################################################################        
 #DO NOT CURRENTLY NEED THESE FUNCTIONS AT THE MOMENT, BUT THEY WOULD WORK       
############################################################################# 
#def postorder(tree):
#    if(tree.left!=None):
#        postorder(tree.left)
#    if(tree.right!=None):
#       postorder(tree.right)
#    print (tree.value)
 
 
#def in_order(tree):
#    if(tree.left!=None):
#        in_order(tree.left)
#    print (tree.value)
#    if(tree.right!=None):
#        in_order(tree.right)
#############################################################################



        
if __name__ == '__main__':
   
    treeval =tree_insert(None,paragraph[0]);                                  #gets the words from 1-6 from the paragraph I had made and then sets those strings as the nodes
    tree_insert(treeval,paragraph[1])
    tree_insert(treeval,paragraph[2])
    tree_insert(treeval,paragraph[3])
    tree_insert(treeval,paragraph[4])
    tree_insert(treeval,paragraph[5])
    tree_insert(treeval,paragraph[6])
    preorder(treeval)                                                         #Calls in the pre_order traversal function
    userinput = input("please search for a word from ones above\n")           #Allows the user to see a path for a node of their choice from node 0-6
    if bin_tree_find(treeval, userinput) == True:
        print("yes, the word was found, the path traversed is shown above in preorder(top to bottom)")        
    else: 
        print("No, word was not found, however a path attempt to find the node in preorder has been made above")

    
    
#print("BST in preorder is: ")
#preorder(t)


#print("BST in, in-order is: ")
#in_order(t)


#print("BST in postorder is: ")
#postorder(t)



