import heapq

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        cost = [float('inf')] * n
        
        # Two heaps for Sliding Window Median
        lo = []  # Max-heap (lower half), stores (-val, index)
        hi = []  # Min-heap (upper half), stores (val, index)
        
        lo_sum = hi_sum = 0
        lo_size = hi_size = 0
        in_lo = [False] * n  # Tracks which heap an active element belongs to
        
        # Helper for lazy deletion
        def clean(h, current_i):
            while h and h[0][1] <= current_i - x:
                heapq.heappop(h)
                
        # Step 1: Compute the equalization cost for every sliding window of size x
        for i in range(n):
            val = nums[i]
            
            # Insert new element
            if not lo or val <= -lo[0][0]:
                heapq.heappush(lo, (-val, i))
                lo_sum += val
                lo_size += 1
                in_lo[i] = True
            else:
                heapq.heappush(hi, (val, i))
                hi_sum += val
                hi_size += 1
                in_lo[i] = False
                
            # Logically remove the element that falls out of the window
            if i >= x:
                out_idx = i - x
                out_val = nums[out_idx]
                if in_lo[out_idx]:
                    lo_size -= 1
                    lo_sum -= out_val
                else:
                    hi_size -= 1
                    hi_sum -= out_val
                    
            # Rebalance the heaps so `lo` always has the median
            target_lo = (min(i + 1, x) + 1) // 2
            
            while lo_size > target_lo:
                clean(lo, i)
                v, idx = heapq.heappop(lo)
                v = -v
                lo_sum -= v
                lo_size -= 1
                in_lo[idx] = False
                
                heapq.heappush(hi, (v, idx))
                hi_sum += v
                hi_size += 1
                
            while lo_size < target_lo:
                clean(hi, i)
                v, idx = heapq.heappop(hi)
                hi_sum -= v
                hi_size -= 1
                in_lo[idx] = True
                
                heapq.heappush(lo, (-v, idx))
                lo_sum += v
                lo_size += 1
                
            # If the window is fully formed, compute its cost
            if i >= x - 1:
                clean(lo, i)
                median = -lo[0][0]
                # Derived mathematically: difference sums for values >= med and <= med
                cost[i] = hi_sum - median * hi_size + median * lo_size - lo_sum
                
        # Step 2: Dynamic Programming to pick k non-overlapping windows
        # Space-optimized DP holding the previous row's states
        prev_dp = [0] * n
        
        for j in range(1, k + 1):
            curr_dp = [float('inf')] * n
            # The earliest a sequence of j windows can end is at index (j * x) - 1
            for i in range(j * x - 1, n):
                skip_cost = curr_dp[i-1] if i > 0 else float('inf')
                
                # Fetch optimal previous non-overlapping sequence end
                pick_cost = prev_dp[i-x] if i - x >= 0 else (0 if j == 1 else float('inf'))
                pick_cost += cost[i]
                
                curr_dp[i] = min(skip_cost, pick_cost)
                
            prev_dp = curr_dp
            
        return prev_dp[-1]