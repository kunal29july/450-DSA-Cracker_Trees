'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=[]
        res=[]
        queue.append(root)
        flag=True
        
        while(len(queue)>0):
            curr_size=len(queue)
            temp=[]
            while(curr_size>0):
                
                node=queue.pop(0)
                temp.append(node.val)
                if flag==True:
                    if node.right is not None:
                        queue.append(node.right)
                    if node.left is not None:
                        queue.append(node.left)

                    flag=False
                else:
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)

                    
                    
                curr_size=curr_size-1
            res.append(temp)
        return res
        
