class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        stack = []
        union_groups = set()
        current_concat = {""}
        
        for char in expression:
            if char == '{':
                # Push the current state to the stack and start a new context
                stack.append((union_groups, current_concat))
                union_groups = set()
                current_concat = {""}
                
            elif char == '}':
                # Evaluate the result of the current brace context
                brace_result = union_groups.union(current_concat)
                
                # Pop the previous state from the stack
                prev_union, prev_concat = stack.pop()
                
                # The new current_concat is the Cartesian product of previous concat and the brace result
                current_concat = {p + r for p in prev_concat for r in brace_result}
                union_groups = prev_union
                
            elif char == ',':
                # Add the completed concatenation sequence to the union set
                union_groups = union_groups.union(current_concat)
                current_concat = {""}
                
            else:
                # Concatenate the current character to all active strings in current_concat
                current_concat = {c + char for c in current_concat}
                
        # Combine the final active sets, sort them, and return as a list
        final_set = union_groups.union(current_concat)
        return sorted(list(final_set))