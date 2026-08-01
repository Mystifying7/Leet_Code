class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # dp array to store the maximum score difference for sub-arrays.
        # We only need a 1D array to keep track of the current and previous states.
        dp = [0] * n
        
        # Iterate backwards for the starting index i
        for i in range(n - 1, -1, -1):
            # Base case: When the sub-array has only one element (i == j), 
            # the player has no choice but to take it.
            dp[i] = nums[i]
            
            # Iterate forwards for the ending index j
            for j in range(i + 1, n):
                # Calculate the max score difference if we pick left (nums[i]) or right (nums[j])
                # dp[j] currently holds the opponent's best from nums[i+1...j]
                # dp[j-1] holds the opponent's best from nums[i...j-1]
                pick_left = nums[i] - dp[j]
                pick_right = nums[j] - dp[j - 1]
                
                dp[j] = max(pick_left, pick_right)
                
        # If the final max score difference is >= 0, Player 1 wins or ties
        return dp[n - 1] >= 0