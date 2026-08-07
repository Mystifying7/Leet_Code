class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            # Helper logic to calculate the product of the digits
            temp = n
            prod = 1
            
            # Explicitly handle 0 if n starts at 0
            if temp == 0:
                prod = 0
            else:
                while temp > 0:
                    prod *= temp % 10
                    temp //= 10
                    
                    # Optional optimization: If prod becomes 0, it will stay 0.
                    # We can break early to save unnecessary multiplications.
                    if prod == 0:
                        break
            
            # Check if the product is divisible by t
            if prod % t == 0:
                return n
                
            # Increment and check the next number
            n += 1