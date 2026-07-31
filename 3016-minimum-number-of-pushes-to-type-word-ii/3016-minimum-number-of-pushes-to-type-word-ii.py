from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Count letter frequencies and sort them descending
        counts = Counter(word)
        sorted_freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        
        for i, freq in enumerate(sorted_freqs):
            # i // 8 gives 0 for first 8 chars (1 push), 1 for next 8 (2 pushes), etc.
            push_cost = (i // 8) + 1
            total_pushes += freq * push_cost
            
        return total_pushes