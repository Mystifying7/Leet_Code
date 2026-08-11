class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        # Sort the array to easily handle duplicates and enable early stopping
        candidates.sort()
        
        def backtrack(start_index, current_combo, current_target):
            # Base Case: We hit exactly our target sum
            if current_target == 0:
                result.append(list(current_combo))
                return
                
            for i in range(start_index, len(candidates)):
                # If the current number is bigger than our remaining target,
                # all subsequent numbers will be too big as well. Stop exploring.
                if candidates[i] > current_target:
                    break
                    
                # Skip duplicate elements at the same depth level
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                    
                # 1. Choose the candidate
                current_combo.append(candidates[i])
                
                # 2. Explore further (pass i + 1 to not reuse the same element)
                backtrack(i + 1, current_combo, current_target - candidates[i])
                
                # 3. Backtrack (undo the choice)
                current_combo.pop()
                
        # Start backtracking from index 0 with an empty combination
        backtrack(0, [], target)
        
        return result