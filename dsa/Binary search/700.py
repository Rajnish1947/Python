class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr = root
        
        while curr:
            if curr.val == val:
                return curr  # Found the value
            elif curr.val < val:
                curr = curr.right  # Go right
            else:
                curr = curr.left   # Go left
        
        return None  # Value not found
