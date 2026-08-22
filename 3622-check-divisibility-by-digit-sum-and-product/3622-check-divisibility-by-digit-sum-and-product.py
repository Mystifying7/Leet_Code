class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = n
        digit_sum = 0
        digit_product = 1
        
        # Extract digits and compute sum and product
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_product *= digit
            temp //= 10
            
        # Check if n is divisible by their combined sum
        total_value = digit_sum + digit_product
        
        return n % total_value == 0