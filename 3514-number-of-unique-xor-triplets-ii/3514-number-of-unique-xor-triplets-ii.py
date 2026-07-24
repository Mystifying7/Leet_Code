class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Extract all unique elements to eliminate redundant calculations
        unique_nums = list(set(nums))
        n = len(unique_nums)
        
        # Step 2: Compute all unique XOR values from pairs of numbers
        # We only need to compute combinations (i <= j) since XOR is commutative
        s2 = {unique_nums[i] ^ unique_nums[j] for i in range(n) for j in range(i, n)}
        
        # Step 3: Compute all unique XOR values from the pairs (s2) and single elements
        s3 = {pair_xor ^ num for pair_xor in s2 for num in unique_nums}
        
        # Return the number of unique triplet XOR results
        return len(s3)