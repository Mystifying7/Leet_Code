class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the array is empty, there are 0 unique elements
        if not nums:
            return 0
            
        # insert_index tracks where the next unique element should be placed
        insert_index = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If we find a new unique element
            if nums[i] != nums[i - 1]:
                # Place it at the insert_index and increment the pointer
                nums[insert_index] = nums[i]
                insert_index += 1
                
        # insert_index now represents the count of unique elements (k)
        return insert_index