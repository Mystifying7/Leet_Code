import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Augment intervals with their original indices and sort by start time
        indexed_intervals = sorted(
            [(interval[0], interval[1], interval[2], i) for i, interval in enumerate(intervals)]
        )
        n = len(indexed_intervals)

        # Helper container for DP results
        class Result(object):
            __slots__ = ('weight', 'selected')
            def __init__(self, weight, selected):
                self.weight = weight
                self.selected = selected

        # Manual memoization dictionary for universal platform compatibility
        memo = {}

        # Step 2: DP function with explicit memoization
        def dp(i, quota):
            if i == n or quota == 0:
                return Result(0, ())
            
            if (i, quota) in memo:
                return memo[(i, quota)]
            
            # Option 1: Skip the current interval
            skip_res = dp(i + 1, quota)
            
            # Option 2: Pick the current interval
            l, r, weight, original_index = indexed_intervals[i]
            
            # Find the first interval that starts strictly after 'r' (non-overlapping)
            j = bisect.bisect_right(indexed_intervals, (r, float('inf'), float('inf'), float('inf')))
            next_res = dp(j, quota - 1)
            
            pick_weight = weight + next_res.weight
            pick_selected = tuple(sorted((original_index,) + next_res.selected))
            pick_res = Result(pick_weight, pick_selected)
            
            # Compare pick vs skip based on weight, then lexicographical order of indices
            if pick_res.weight > skip_res.weight:
                res = pick_res
            elif skip_res.weight > pick_res.weight:
                res = skip_res
            else:
                # Weights are equal: pick the lexicographically smaller index list
                if pick_res.selected < skip_res.selected:
                    res = pick_res
                else:
                    res = skip_res
            
            memo[(i, quota)] = res
            return res

        # Start the DP from index 0 with a quota of up to 4 intervals
        final_result = dp(0, 4)
        return list(final_result.selected)