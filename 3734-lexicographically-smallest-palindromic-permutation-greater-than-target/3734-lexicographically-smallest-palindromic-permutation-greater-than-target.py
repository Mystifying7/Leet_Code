import collections

class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        counts = collections.Counter(s)
        
        # Step 1: Validate if a palindrome is even possible
        odds = 0
        mid_char = ""
        for char, count in counts.items():
            if count % 2 != 0:
                odds += 1
                mid_char = char
                
        # For even length, no odd counts allowed. For odd length, exactly one odd count allowed.
        if n % 2 == 0 and odds > 0:
            return ""
        if n % 2 != 0 and odds != 1:
            return ""
            
        # Step 2: Extract the character pool for the left half of the palindrome
        half_counts = collections.Counter()
        for char, count in counts.items():
            if count // 2 > 0:
                half_counts[char] = count // 2
                
        m = n // 2
        t_left = target[:m]
        
        # Step 3: Check if the exact left half of the target can be formed
        # If it can, we test if the resulting palindrome is strictly greater than target
        if collections.Counter(t_left) == half_counts:
            p_cand = t_left + mid_char + t_left[::-1]
            if p_cand > target:
                return p_cand
                
        # Step 4: Find the smallest permutation of half_counts strictly greater than t_left
        if m > 0:
            req_counts = collections.Counter(t_left[:-1])
        else:
            req_counts = collections.Counter()
            
        # Iterate backward to find the longest matching prefix we can salvage
        for i in range(m - 1, -1, -1):
            possible = True
            for char, count in req_counts.items():
                if count > half_counts.get(char, 0):
                    possible = False
                    break
                    
            if possible:
                found_char = None
                # Look for the smallest available character greater than t_left[i]
                for code in range(ord(t_left[i]) + 1, ord('z') + 1):
                    c = chr(code)
                    if half_counts.get(c, 0) - req_counts.get(c, 0) > 0:
                        found_char = c
                        break
                        
                if found_char:
                    rem = []
                    # Gather all remaining characters to append in sorted alphabetical order
                    for code in range(ord('a'), ord('z') + 1):
                        c = chr(code)
                        rem_count = half_counts.get(c, 0) - req_counts.get(c, 0)
                        if c == found_char:
                            rem_count -= 1
                        if rem_count > 0:
                            rem.append(c * rem_count)
                            
                    new_left = t_left[:i] + found_char + "".join(rem)
                    return new_left + mid_char + new_left[::-1]
                    
            # Decrement the requirement for the next loop iteration
            if i > 0:
                req_counts[t_left[i-1]] -= 1
                
        return ""