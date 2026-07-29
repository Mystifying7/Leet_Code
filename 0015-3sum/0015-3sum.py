class Solution(object):
    def threeSum(self, nums):
        # Sort the array to use two pointers and easily handle duplicates
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Optimization: If the smallest number is greater than 0, 
            # no triplet can ever sum to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Triplet sums to zero, add to results
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate elements for the second position
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate elements for the third position
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers inward to search for the next distinct triplet
                    left += 1
                    right -= 1
                    
        return result