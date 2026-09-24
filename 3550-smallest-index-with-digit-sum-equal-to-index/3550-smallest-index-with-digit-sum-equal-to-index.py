class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            # Calculate the sum of the digits of the current number
            digit_sum = sum(int(digit) for digit in str(num))
            
            # If the digit sum matches the index, return it immediately
            if digit_sum == i:
                return i
                
        # If no such index is found after checking all elements
        return -1