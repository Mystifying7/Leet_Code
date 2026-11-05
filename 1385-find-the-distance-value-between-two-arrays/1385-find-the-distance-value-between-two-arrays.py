import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find the insertion point for x in the sorted arr2
            idx = bisect.bisect_left(arr2, x)
            
            is_valid = True
            
            # Check the closest element greater than or equal to x
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                is_valid = False
                
            # Check the closest element strictly less than x
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                is_valid = False
                
            if is_valid:
                distance_value += 1
                
        return distance_value