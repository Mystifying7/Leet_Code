class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        # Step 1: Convert knowledge list to a dictionary for O(1) lookups
        knowledge_dict = {k: v for k, v in knowledge}
        
        res = []
        current_key = []
        in_bracket = False
        
        # Step 2: Iterate through the string parsing brackets and text
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                # Reached the end of a key, look it up
                key_str = "".join(current_key)
                res.append(knowledge_dict.get(key_str, "?"))
                
                # Reset for the next potential key
                in_bracket = False
                current_key = []
            elif in_bracket:
                # Accumulate the characters of the key
                current_key.append(char)
            else:
                # Standard characters outside of any brackets
                res.append(char)
                
        # Step 3: Join the list of strings into the final result
        return "".join(res)