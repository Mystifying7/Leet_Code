class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        # Frequency map of the words we need to find
        word_count = Counter(words)
        result = []
        
        # We only need to run the sliding window for 'word_len' different offsets
        for i in range(word_len):
            left = i
            right = i
            seen_words = Counter()
            count = 0
            
            # Slide the right pointer in jumps of 'word_len'
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                # If the word is part of the given words array
                if word in word_count:
                    seen_words[word] += 1
                    count += 1
                    
                    # If we've seen this word too many times, shrink the window from the left
                    while seen_words[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen_words[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    # If our valid word count matches the total words needed, we found a match
                    if count == num_words:
                        result.append(left)
                        
                else:
                    # An invalid word breaks the contiguous sequence, reset everything
                    seen_words.clear()
                    count = 0
                    left = right
                    
        return result