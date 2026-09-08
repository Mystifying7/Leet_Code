class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_commas = 0
        threshold = 1000
        
        # Keep scaling up the threshold by 1,000 
        while n >= threshold:
            # Add 1 comma for every number that reaches or exceeds the current threshold
            total_commas += (n - threshold + 1)
            threshold *= 1000
            
        return total_commas