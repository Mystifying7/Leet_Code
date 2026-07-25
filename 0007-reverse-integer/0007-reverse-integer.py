class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Maximum value divided by 10 to check for overflow beforehand
        MAX_LIMIT = 214748364  
        
        # Store sign and work with the absolute value
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        res = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for potential overflow before updating the result
            if res > MAX_LIMIT or (res == MAX_LIMIT and digit > 7):
                return 0
                
            res = res * 10 + digit
            
        return res * sign