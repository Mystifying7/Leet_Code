class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # Sort to easily skip duplicates
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(current_path):
            # Base Case: Permutation is complete
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
                
            for i in range(len(nums)):
                # Skip if the element is already used in this path
                if used[i]:
                    continue
                    
                # Pruning condition to avoid duplicate permutations:
                # If the current number is the same as the previous one,
                # AND the previous one was just evaluated and removed in this same depth level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                    
                # 1. Choose the number
                used[i] = True
                current_path.append(nums[i])
                
                # 2. Explore further
                backtrack(current_path)
                
                # 3. Backtrack (undo the choice)
                current_path.pop()
                used[i] = False
                
        # Start the backtracking process
        backtrack([])
        
        return result