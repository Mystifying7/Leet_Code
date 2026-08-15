class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        # Iterate up to the second to last element. 
        # (Once we reach the last element, we don't need to jump anymore).
        for i in range(len(nums) - 1):
            # Update the farthest index reachable from our current position
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the limit of our current jump, we must make another jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
                
                # Optional Optimization: If our next jump range already reaches or passes 
                # the end of the array, we can stop early.
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps