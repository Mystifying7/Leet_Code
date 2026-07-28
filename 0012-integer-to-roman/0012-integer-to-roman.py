class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the symbols and their values in descending order, 
        # including the special subtractive cases.
        value_symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in value_symbols:
            # If the number has been fully converted, we can stop early
            if num == 0:
                break
                
            # Find out how many times the current value fits into num
            count = num // value
            if count > 0:
                result.append(symbol * count)
                # Update num to the remainder
                num %= value
                
        return "".join(result)