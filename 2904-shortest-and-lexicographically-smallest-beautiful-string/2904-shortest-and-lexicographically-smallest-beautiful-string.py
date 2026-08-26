class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Step 1: Record all indices where a '1' appears
        ones = [i for i, char in enumerate(s) if char == '1']
        
        # Step 2: If there aren't enough 1s, return an empty string
        if len(ones) < k:
            return ""
            
        best_str = ""
        min_len = float('inf')
        
        # Step 3: Slide a window of size k over the indices of '1's
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            
            # Extract the substring and its length
            current_len = end - start + 1
            current_str = s[start:end + 1]
            
            # Step 4: Update the best candidate based on length and lexicographical order
            if current_len < min_len:
                min_len = current_len
                best_str = current_str
            elif current_len == min_len:
                if current_str < best_str:
                    best_str = current_str
                    
        return best_str