class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        intervals = []
        
        # Step 1: Find the shortest valid palindrome for each possible center
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    # Found a valid palindrome >= k. Record it and break.
                    intervals.append((left, right))
                    break
                left -= 1
                right += 1
                
        # Step 2: Greedy interval scheduling
        # Sort by end index to maximize space available for the remaining string
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        
        for start, end in intervals:
            # If the current palindrome starts strictly after the last one ended
            if start > last_end:
                count += 1
                last_end = end
                
        return count