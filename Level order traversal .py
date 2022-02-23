'''
Given a binary tree, find its level order traversal.
Level order traversal of a tree is breadth-first traversal for the tree.


Example 1:

Input:
    1
  /   \ 
 3     2
Output:1 3 2
Example 2:

Input:
        10
     /      \
    20       30
  /   \
 40   60
Output:10 20 30 40 60

Your Task:
You don't have to take any input. Complete the function levelOrder() that takes the root node as input parameter and returns a list of integers containing the level order traversal of the given Binary Tree.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


'''
class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        if root is None:
            return
        
        queue=[]
        ans=[]
        queue.append(root)
        
        while(queue):
            ans.append(queue[0].data)
            node=queue.pop(0)
            
            if node.left is not None:
                queue.append(node.left)
                
            if node.right is not None:
                queue.append(node.right)
        return ans
      
      #second approch to show ans in list
      
          def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        out=[]
        queue=[]
        queue.append(root)
        
        while(len(queue)>0):
            currsize=len(queue)
            temp=[]
            while(currsize>0):
                node=queue.pop(0)
                temp.append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    
                currsize=currsize-1
            out.append(temp)
        return out
