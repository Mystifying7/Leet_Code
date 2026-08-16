class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        used = [False] * len(nums)
        
        def backtrack(current_path):
            # Base Case: The permutation is complete
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
                
            # Iterate through all available choices
            for i in range(len(nums)):
                # Skip if the number is already used in the current permutation
                if used[i]:
                    continue
                    
                # 1. Choose the number
                used[i] = True
                current_path.append(nums[i])
                
                # 2. Explore further
                backtrack(current_path)
                
                # 3. Backtrack (undo the choice)
                current_path.pop()
                used[i] = False
                
        # Start backtracking with an empty path
        backtrack([])
        
        return result