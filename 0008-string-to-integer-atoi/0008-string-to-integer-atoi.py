class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        
        # 32-bit signed integer limits
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # If we reached the end of the string, return 0
        if i == n:
            return 0
            
        # Step 2: Determine the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3 & 4: Convert characters to integer and clamp if necessary
        result = 0
        while i < n and s[i].isdigit():
            # Convert string digit to integer
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            
            # Check boundaries and clamp to avoid massive number memory usage in edge cases
            if sign == 1 and result > INT_MAX:
                return INT_MAX
            if sign == -1 and -result < INT_MIN:
                return INT_MIN
                
            i += 1
            
        return sign * result