import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Dictionary to map the character count tuple to the list of anagrams
        anagram_map = collections.defaultdict(list)
        
        for s in strs:
            # Initialize an array of 26 zeros to represent the character counts
            count = [0] * 26
            
            # Count the frequency of each character in the string
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            # Tuples are immutable and hashable, making them valid dictionary keys
            anagram_map[tuple(count)].append(s)
            
        # Return all the grouped anagram lists
        return anagram_map.values()