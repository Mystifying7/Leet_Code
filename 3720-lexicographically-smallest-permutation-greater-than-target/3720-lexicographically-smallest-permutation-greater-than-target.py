from collections import Counter

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        s_count = Counter(s)
        # Initialize t_count with the characters in target[0 ... n-2]
        t_count = Counter(target[:-1])
        
        # Iterate the differing index i from n-1 down to 0
        for i in range(n - 1, -1, -1):
            # Check if it's possible to form the prefix target[0 ... i-1]
            possible = True
            for char, count in t_count.items():
                if count > s_count.get(char, 0):
                    possible = False
                    break
            
            if possible:
                # Find the smallest available character strictly greater than target[i]
                found_char = None
                for o in range(ord(target[i]) - ord('a') + 1, 26):
                    char = chr(o + ord('a'))
                    rem = s_count.get(char, 0) - t_count.get(char, 0)
                    if rem > 0:
                        found_char = char
                        break
                
                if found_char:
                    # Construct the resulting string
                    res = []
                    if i > 0:
                        res.append(target[:i])
                    res.append(found_char)
                    
                    # Calculate the remaining characters to be appended
                    rem_counts = {}
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        rem = s_count.get(char, 0) - t_count.get(char, 0)
                        if char == found_char:
                            rem -= 1
                        if rem > 0:
                            rem_counts[char] = rem
                            
                    # Append remaining characters in sorted (alphabetical) order
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if char in rem_counts:
                            res.append(char * rem_counts[char])
                            
                    return "".join(res)
            
            # Decrement the count of target[i-1] for the next iteration's prefix check
            if i > 0:
                char_to_remove = target[i - 1]
                t_count[char_to_remove] -= 1
                if t_count[char_to_remove] == 0:
                    del t_count[char_to_remove]
                    
        return ""