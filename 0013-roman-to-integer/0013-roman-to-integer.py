class Solution(object):
    def romanToInt(self, s):
        # Dictionary mapping Roman numerals to integer values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If there is a next character and the current value is less than the next, subtract it
            if i + 1 < n and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            # Otherwise, add it
            else:
                total += roman_values[s[i]]
                
        return total