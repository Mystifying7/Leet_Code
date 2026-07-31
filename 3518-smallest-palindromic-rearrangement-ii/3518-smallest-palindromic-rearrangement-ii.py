class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        from collections import Counter
        import math
        
        # Step 1: Count frequencies and identify the middle character
        freq = Counter(s)
        odd_char = ""
        for char, count in freq.items():
            if count % 2 != 0:
                odd_char = char
        
        # Determine the counts of characters available for the left half
        half_counts = {}
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if freq[char] > 0:
                half_counts[char] = freq[char] // 2
                
        total_len = sum(half_counts.values())
        
        # Step 2: Calculate the total number of unique permutations
        perms = math.factorial(total_len)
        for count in half_counts.values():
            if count > 1:
                perms //= math.factorial(count)
                
        if k > perms:
            return ""
            
        left_half = []
        
        # FIX: Explicitly sort the characters to absolutely guarantee alphabetical evaluation
        chars = sorted([c for c in half_counts if half_counts[c] > 0])
        
        # Step 3: Construct the k-th permutation
        for i in range(total_len):
            length = total_len - i
            for char in chars:
                # Only evaluate characters we still have available
                if half_counts[char] > 0:
                    # Calculate permutations if we place 'char' at the current position
                    ways = perms * half_counts[char] // length
                    
                    if k <= ways:
                        left_half.append(char)
                        half_counts[char] -= 1
                        perms = ways
                        break
                    else:
                        # Skip this character and subtract its possible branches from k
                        k -= ways
                        
        left_str = "".join(left_half)
        
        # Step 4: Assemble the full palindrome
        return left_str + odd_char + left_str[::-1]