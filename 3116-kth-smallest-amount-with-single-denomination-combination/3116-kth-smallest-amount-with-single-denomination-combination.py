class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Sort and filter out redundant coins
        coins.sort()
        filtered_coins = []
        for c in coins:
            # Keep the coin if it is not a multiple of any previously kept smaller coin
            if not any(c % fc == 0 for fc in filtered_coins):
                filtered_coins.append(c)
                
        # Safe upper bound for the binary search
        high = filtered_coins[0] * k
        
        # Helper function for Greatest Common Divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        # Helper function for Least Common Multiple
        def lcm(a, b):
            return a * b // gcd(a, b)
            
        # Step 2: Precompute all LCMs for Inclusion-Exclusion
        lcm_list = []
        n = len(filtered_coins)
        
        # Iterate through all non-empty subsets using bitmasking
        for i in range(1, 1 << n):
            current_lcm = 1
            count = 0
            
            for j in range(n):
                if (i >> j) & 1:
                    current_lcm = lcm(current_lcm, filtered_coins[j])
                    count += 1
            
            # If the LCM exceeds our maximum possible answer, it contributes 0 to the count,
            # so we can safely discard it to save memory and operations.
            if current_lcm <= high:
                # Add 1 for odd subset sizes (add), -1 for even (subtract)
                sign = 1 if count % 2 == 1 else -1
                lcm_list.append((current_lcm, sign))
                
        # Step 3: Binary Search to find the k-th smallest amount
        low = 1
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Use Inclusion-Exclusion to count valid amounts <= mid
            current_count = sum(sign * (mid // l) for l, sign in lcm_list)
                
            if current_count >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # We need a larger number to reach k amounts
                
        return ans