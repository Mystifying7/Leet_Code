class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Segment tree arrays
        # total_prod[node] stores the product of the range modulo k
        total_prod = [0] * (4 * n)
        # pref_counts[node][v] stores the count of prefixes in the range with product % k == v
        pref_counts = [[0] * k for _ in range(4 * n)]
        
        def build(node, l, r):
            if l == r:
                val = nums[l] % k
                total_prod[node] = val
                pref_counts[node][val] = 1
                return
                
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            
            # Merge left and right children
            left = 2 * node
            right = 2 * node + 1
            
            total_prod[node] = (total_prod[left] * total_prod[right]) % k
            
            # Copy prefixes from the left child
            for i in range(k):
                pref_counts[node][i] = pref_counts[left][i]
                
            # Extend with prefixes from the right child
            lp = total_prod[left]
            for i in range(k):
                if pref_counts[right][i] > 0:
                    pref_counts[node][(lp * i) % k] += pref_counts[right][i]

        if n > 0:
            build(1, 0, n - 1)
            
        def update(node, l, r, idx, val):
            if l == r:
                v = val % k
                total_prod[node] = v
                for i in range(k):
                    pref_counts[node][i] = 0
                pref_counts[node][v] = 1
                return
                
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
                
            # Merge left and right children after update
            left = 2 * node
            right = 2 * node + 1
            
            total_prod[node] = (total_prod[left] * total_prod[right]) % k
            
            for i in range(k):
                pref_counts[node][i] = pref_counts[left][i]
                
            lp = total_prod[left]
            for i in range(k):
                if pref_counts[right][i] > 0:
                    pref_counts[node][(lp * i) % k] += pref_counts[right][i]

        def query(node, l, r, ql, qr):
            # If the current range is completely within the query range
            if ql <= l and r <= qr:
                return total_prod[node], pref_counts[node]
                
            mid = (l + r) // 2
            
            # If the query is completely in the left or right half
            if qr <= mid:
                return query(2 * node, l, mid, ql, qr)
            if ql > mid:
                return query(2 * node + 1, mid + 1, r, ql, qr)
                
            # If the query overlaps both halves, fetch and merge them
            l_prod, l_counts = query(2 * node, l, mid, ql, qr)
            r_prod, r_counts = query(2 * node + 1, mid + 1, r, ql, qr)
            
            res_prod = (l_prod * r_prod) % k
            res_counts = list(l_counts)
            
            for i in range(k):
                if r_counts[i] > 0:
                    res_counts[(l_prod * i) % k] += r_counts[i]
                    
            return res_prod, res_counts

        ans = []
        for index, value, start, x in queries:
            # 1. Update the value at 'index' persistently
            update(1, 0, n - 1, index, value)
            
            # 2. Query the requested subsegment and retrieve valid prefix counts
            if start < n:
                _, counts = query(1, 0, n - 1, start, n - 1)
                ans.append(counts[x])
            else:
                ans.append(0)
                
        return ans
    
    # Aliasing just in case the platform expects 'xValue' or another signature
    xValue = resultArray