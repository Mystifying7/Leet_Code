class Solution(object):
    def threeSumClosest(self, nums, target):
        # Sort the array to enable the two-pointer approach
        nums.sort()
        n = len(nums)
        
        # Initialize closest_sum with infinity to guarantee the first sum replaces it
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update the closest_sum if the current one is strictly closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                # Adjust pointers based on how the current sum compares to the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the sum perfectly matches the target, return immediately
                    return current_sum
                    
        return closest_sum