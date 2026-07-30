class Solution(object):
    def letterCombinations(self, digits):
        # If the input is empty, return an empty list immediately
        if not digits:
            return []
            
        # Dictionary mapping digits to their corresponding letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, current_string):
            # Base case: if the string length matches digits length, we found a combination
            if len(current_string) == len(digits):
                result.append(current_string)
                return
                
            # Get the letters that the current digit maps to
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]
            
            # Explore all possible letters for this digit
            for letter in possible_letters:
                # Recurse with the next index and the updated string
                backtrack(index + 1, current_string + letter)
                
        # Start the backtracking process from index 0 with an empty string
        backtrack(0, "")
        
        return result