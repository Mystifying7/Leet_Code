import itertools

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        unique_numbers = set()
        
        # Generate all permutations of length 3 using different indices of digits
        for a, b, c in itertools.permutations(digits, 3):
            # Check conditions: no leading zero and must be an even number
            if a != 0 and c % 2 == 0:
                number = a * 100 + b * 10 + c
                unique_numbers.add(number)
                
        return len(unique_numbers)