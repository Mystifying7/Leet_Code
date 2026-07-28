class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # The height of the container is limited by the shorter line
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            
            # Update maximum area if the current one is larger
            if current_area > max_area:
                max_area = current_area
                
            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area