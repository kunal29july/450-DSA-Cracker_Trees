'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        t1=root
        t2=root
        
        def ans(t1,t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None and t2 is not None:
                return False
            
            if t2 is None and t1 is not None:
                return False
            
            if t1.val!=t2.val:
                return False
            
            return ans(t1.left,t2.right) and ans(t1.right,t2.left)
            
            
        return ans(t1,t2)
