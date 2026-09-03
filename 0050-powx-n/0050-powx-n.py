class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Step 1: Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1.0
        
        # Step 2: Binary exponentiation loop
        while n > 0:
            # Step 3: If n is odd, multiply the current x into the result
            if n % 2 != 0:
                res *= x
                
            # Step 4: Square x and halve n
            x *= x
            n //= 2
            
        return res