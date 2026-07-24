class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to minimize the binary search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            # Use negative and positive infinity for out-of-bounds indices
            A_left = nums1[i - 1] if i > 0 else float('-inf')
            A_right = nums1[i] if i < m else float('inf')
            
            B_left = nums2[j - 1] if j > 0 else float('-inf')
            B_right = nums2[j] if j < n else float('inf')
            
            # Check if we have found the correct partition
            if A_left <= B_right and B_left <= A_right:
                # If the total length is odd, the median is the max of the left elements
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                # If the total length is even, average the max of lefts and min of rights
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            # If A's left is too big, move the search space to the left
            elif A_left > B_right:
                right = i - 1
            # If B's left is too big, move the search space to the right
            else:
                left = i + 1