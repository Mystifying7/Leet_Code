class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        
        left_max = height[left]
        right_max = height[right]
        
        trapped_water = 0
        
        while left < right:
            # The right side is taller, so the bottleneck for water is on the left
            if height[left] < height[right]:
                # Update left_max if we found a taller boundary
                if height[left] >= left_max:
                    left_max = height[left]
                # Otherwise, water can be trapped
                else:
                    trapped_water += left_max - height[left]
                left += 1
                
            # The left side is taller (or equal), so the bottleneck is on the right
            else:
                # Update right_max if we found a taller boundary
                if height[right] >= right_max:
                    right_max = height[right]
                # Otherwise, water can be trapped
                else:
                    trapped_water += right_max - height[right]
                right -= 1
                
        return trapped_water