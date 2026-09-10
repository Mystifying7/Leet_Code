# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.matching_nodes = 0
        
        def post_order(node):
            # Base case: empty nodes contribute 0 to sum and 0 to count
            if not node:
                return 0, 0
                
            # Traverse left and right subtrees
            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)
            
            # Calculate totals for the current subtree
            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            
            # Check if the integer average matches the node's value
            if curr_sum // curr_count == node.val:
                self.matching_nodes += 1
                
            # Bubble up the totals to the parent node
            return curr_sum, curr_count
            
        post_order(root)
        return self.matching_nodes