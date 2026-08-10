class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base case for n = 1
        result = "1"
        
        # We need to generate the sequence n - 1 times
        for _ in range(n - 1):
            next_result = []
            count = 1
            curr_char = result[0]
            
            # Iterate through the current result to build the next one
            for i in range(1, len(result)):
                if result[i] == curr_char:
                    # Same character continues the run
                    count += 1
                else:
                    # Different character found, record the previous run
                    next_result.append(str(count))
                    next_result.append(curr_char)
                    
                    # Reset tracker for the new character
                    curr_char = result[i]
                    count = 1
                    
            # Don't forget to append the final run after the loop ends
            next_result.append(str(count))
            next_result.append(curr_char)
            
            # Join the list into a single string for the next iteration
            result = "".join(next_result)
            
        return result