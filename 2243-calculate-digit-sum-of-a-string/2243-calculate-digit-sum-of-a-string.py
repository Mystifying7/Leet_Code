class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Continue the process until the length of s is k or less
        while len(s) > k:
            new_s = []
            
            # Step through the string in chunks of size k
            for i in range(0, len(s), k):
                chunk = s[i:i+k]
                
                # Sum the integer values of each character in the chunk
                chunk_sum = sum(int(digit) for digit in chunk)
                
                # Append the string representation of the sum
                new_s.append(str(chunk_sum))
                
            # Form the new string for the next potential iteration
            s = "".join(new_s)
            
        return s