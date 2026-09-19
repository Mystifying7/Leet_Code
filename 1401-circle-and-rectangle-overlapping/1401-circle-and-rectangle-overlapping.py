class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # Step 1: Find the closest point on the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Step 2: Calculate the differences
        dist_x = xCenter - closest_x
        dist_y = yCenter - closest_y
        
        # Step 3: Compare squared distance to squared radius
        return (dist_x ** 2 + dist_y ** 2) <= radius ** 2