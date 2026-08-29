class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        # Pair each number with its original index and sort by the number's value
        pairs = sorted([(val, i) for i, val in enumerate(nums)])
        
        result = [0] * len(nums)
        
        group_vals = []
        group_indices = []
        
        for val, idx in pairs:
            # If the group is empty or the current value is within the limit 
            # from the maximum value in the current group (which is the previous one)
            if not group_vals or val - group_vals[-1] <= limit:
                group_vals.append(val)
                group_indices.append(idx)
            else:
                # The chain is broken. Process the current group.
                # Sort the indices so we can place the smallest values in the earliest spots
                group_indices.sort()
                
                for v, index in zip(group_vals, group_indices):
                    result[index] = v
                    
                # Start a new group
                group_vals = [val]
                group_indices = [idx]
                
        # Don't forget to process the very last group after the loop finishes
        if group_vals:
            group_indices.sort()
            for v, index in zip(group_vals, group_indices):
                result[index] = v
                
        return result