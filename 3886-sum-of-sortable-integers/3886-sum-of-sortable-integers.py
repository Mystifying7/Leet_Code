import math

class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Find all divisors of n
        divisors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        # Step 2: Precalculate "drops" (where an element is strictly greater than the next)
        drops_pref = [0] * (n + 1)
        curr = 0
        for i in range(n):
            drops_pref[i] = curr
            if i < n - 1 and nums[i] > nums[i+1]:
                curr += 1
        drops_pref[n] = curr
        
        total_sortable_sum = 0
        
        # Step 3: Check each divisor k
        for k in divisors:
            valid = True
            prev_max = -float('inf')
            
            for i in range(0, n, k):
                L = i
                R = i + k
                
                # Check internal cyclic shift condition (Condition 1)
                if k > 1:
                    ndrops = drops_pref[R - 1] - drops_pref[L]
                    if ndrops > 1:
                        valid = False
                        break
                    # If there's exactly 1 drop, the last element must be <= the first element
                    if ndrops == 1 and nums[R - 1] > nums[L]:
                        valid = False
                        break
                
                # Check global ordering condition (Condition 2)
                block_min = min(nums[L:R])
                if block_min < prev_max:
                    valid = False
                    break
                    
                prev_max = max(nums[L:R])
                
            if valid:
                total_sortable_sum += k
                
        return total_sortable_sum