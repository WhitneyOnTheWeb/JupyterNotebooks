import copy
import numpy as np

# Create BinarySearchTree Class---------------------------------------------------------
class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        
    
# Create TreeNode Class-------------------------------------------------
    class TreeNode(object):
        
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None   
        
        # TreeNode logical functionality----------------
        def getValue(self): return self.value
        def setValue(self, value): self.value = value 
        def hasLeftChild(self): return self.left != None
        def getLeftChild(self): return self.left     
        def setLeftChild(self, value): self.left = self.TreeNode(value)
        def hasRightChild(self): return self.right != None
        def getRightChild(self): return self.right     
        def setRightChild(self, value): self.right = self.TreeNode(value)
        
        def TreeNode(self, value):
            self.value = value
            self.left = None
            self.right = None

#---End TreeNode Class--------------------------------------------------
#--- BinarySearchTree logical functionality
            
    def setRoot(self, value): self.root = self.TreeNode(value)
    def copyNode(self, node): return copy.copy(node)
    def isEmpty(self): return self.root == None 
    def isSymmetric(self, root): return self.isMirror(root, root)
    
#--- Return the left most child TreeNode
    def findLeftMost(self, root):
        if root.hasLeftChild():
            return self.findLeftMost(root.getLeftChild())
        return root
    
#-- Return the right most child TreeNode
    def findRightMost(self, root):
        if root.hasRightChild():
            return self.findRightMost(root.getRightChild())
        return root
    
# Insert Values----------------------------------------
#--- Iterative insert for random number array----------
    def insert(self, values):
        if self.isEmpty():
            self.setRoot(values.pop(0))
        for v in values:
            self.insertTreeNodes(self.root, v)
        return print('Data Loaded Successfully')

#--- Smaller values to the left
#--- Larger values to the right
    def insertTreeNodes(self, curr_node, v):
        new_node = self.TreeNode(v)
        if v <= curr_node.value:
            if curr_node.hasLeftChild():
                self.insertTreeNodes(curr_node.left, v)
            else:
                curr_node.left = new_node
        elif v > curr_node.value:
            if curr_node.hasRightChild():
                self.insertTreeNodes(curr_node.right, v)
            else:
                curr_node.right = new_node  
                
    def buildTree(self, preOrder, postOrder):
        return
                
#--- Creates a mirrored SubTree based on a root
    def mirror(self, root, type):
        mirr_root = self.copyNode(root)
        if type == 'random':
            return self.insertMirror(root, mirr_root)
        elif type == 'reflect':
            return self.mirrorSubTree(mirr_root)
        else: return 'Mirror type not valid'


#--- Currently destroys the root already in place
    def insertMirror(self, root, mirr_root):
        if root:  # Needs Work
            if mirr_root == None: return mirr_root

            left = self.insertMirror(root.left, mirr_root.left)
            mirr_root.right = left
            
            right = self.insertMirror(root.right, mirr_root.right)
            mirr_root.left = right
        
        return mirr_root
    
        
#--- Doesn't properly mirror after the second level
    def mirrorSubTree(self, mirr_root):
        if mirr_root: # Needs Work

            left = self.mirrorSubTree(mirr_root.left)
            right = self.mirrorSubTree(mirr_root.right)
            
            mirr_root.right = left
            mirr_root.left = right
        
        return mirr_root
        
                
# Remove Values----------------------------------------
    #def remove(self):  #Coming soon
        

# Search Binary TreeNodes------------------------------
# Practice Search Functions Inspired by LeetCode

#--- Visit root, then left subtree, then right subtree
    def preorderTraversal(self, root, order):
        if root:
            order.append(root.value)   
            self.preorderTraversal(root.left, order) 
            self.preorderTraversal(root.right, order)
        return order
    
#--- Visit left subtree, then root, then right subtree    
    def inorderTraversal(self, root, order):
        if root:
            self.inorderTraversal(root.left, order)
            order.append(root.value)   
            self.inorderTraversal(root.right, order)
        return order

#--- Visit right subtree, then root, then left subtree
    def revorderTraversal(self, root, order):
        if root:
            self.revorderTraversal(root.right, order)
            order.append(root.value)   
            self.revorderTraversal(root.left, order)
        return order

#--- Visit left subtree, then right subtree, then root
    def postorderTraversal(self, root, order):
        if root:
            self.postorderTraversal(root.left, order)
            self.postorderTraversal(root.right, order)
            order.append(root.value)
        return order 

#--- Visit level of SearchTree, then nodes left to right 
    def levelOrderTraversal(self, root, order):
        if root:
            self.levelOrder(root, 0, order)
        return order
    
    def levelOrder(self, root, level, order):
        if root:
            if len(order) < level+1: 
                order.append([])
            self.levelOrder(root.left, level+1, order)
            order[level].append(root.value)
            self.levelOrder(root.right, level+1, order)  
            
#--- Display BinarySearchTree Traversal Output
    def showOrder(self, order):
        for i in range(0, len(order)):
            print('[{0}]: {1}'.format(i, order[i]))

    
# Depth and Measurement Functions--------------------------
     
#--- Return size of SearchTree starting from node    
    def getSize(self, root):
        if root is None: return 0
        else:
            return self.getSize(root.left) + 1 \
                 + self.getSize(root.right)
    
#--- Return number of levels in the SearchTree
    def findDepth(self, root):
        if not root:
            return 0
        left = self.findDepth(root.left)
        right = self.findDepth(root.right)
        return max(left, right) + 1
    
#--- Checks left/right subtrees for symmetry, returns boolean
    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.value == root2.value:
                return self.isMirror(root1.left, root2.right) \
                and self.isMirror(root1.right, root2.left)
        return False

#--- Calculates sum of each root-to-leaf path--------------
    def pathSum(self, root1, root2, sum, sums):
        if root1:
            if self.pathSum(root1.left, root1.right, 
                            sum + root1.value, sums): 
                sums.append(sum)
        if root2:
            if self.pathSum(root2.left, root2.right, 
                            sum + root2.value, sums): 
                sums.append(sum)
        return sums.append(sum)
    
#--- Checks for root-to-leaf paths = sum
    def hasPathSum(self, root, sum):
        sums = []
        self.pathSum(root, root, 0, sums)
        return sum in sums[0:-1] 
    
#--- Returns array of summed root-to-leaf paths
    def sumPath(self, root):
        sums = []
        self.pathSum(root, root, 0, sums)
        return sums[0:-1]  
    
#--- Returns sum of all node values
    def sumTree(self, root):
        sums = []
        self.pathSum(root, root, 0, sums)
        return sum(sums[0:-1])   

#--- Returns count of subtrees with nodes of same value
    def countUnivalSubtrees(self, root):
        count = [0]
        self.countSubtrees(root, count)
        return count[0]

    def countSubtrees(self, root, count):
        if root is None: return True
        
        left = self.countSubtrees(root.left, count)
        right = self.countSubtrees(root.right, count)
        
        if not left or not right: return False
        if root.left and (root.value != root.left.value):
            return False
        if root.right and (root.value != root.right.value):
            return False
        
        count[0] += 1
        return True
    
    def BinarySearchTree(self):
        self.root = None   
        
#---End BinarySearchTree Class------------------------------------------------------------------------