class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        # Step 1: Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Arrays for Binary Lifting (LCA) and Euler Tour
        up = [[0] * 17 for _ in range(n)]
        depth = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        
        # Step 2: Iterative DFS to populate LCA table and Euler Tour times
        timer = 1
        stack = [(0, -1, 0, True)]
        
        while stack:
            u, p, d, is_entry = stack.pop()
            if is_entry:
                depth[u] = d
                up[u][0] = p if p != -1 else 0
                for i in range(1, 17):
                    up[u][i] = up[up[u][i-1]][i-1]
                    
                in_time[u] = timer
                timer += 1
                
                # Push the exit action to the stack
                stack.append((u, p, d, False))
                
                # Push children to traverse
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, d + 1, True))
            else:
                out_time[u] = timer
                timer += 1
                
        # Step 3: Fenwick Tree (Binary Indexed Tree)
        bit = [0] * (2 * n + 1)
        
        def add(idx, val):
            while idx <= 2 * n:
                bit[idx] ^= val
                idx += idx & -idx
                
        def query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & -idx
            return res
            
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            diff = depth[u] - depth[v]
            for i in range(17):
                if (diff >> i) & 1:
                    u = up[u][i]
                    
            if u == v:
                return u
                
            for i in range(16, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
                    
            return up[u][0]
            
        # Step 4: Initialize the Fenwick tree with starting characters
        current_chars = list(s)
        for i in range(n):
            mask = 1 << (ord(current_chars[i]) - 97) # 97 is ord('a')
            add(in_time[i], mask)
            add(out_time[i], mask)
            
        # Step 5: Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]
                old_char = current_chars[u]
                
                if old_char != new_char:
                    # XOR out the old character mask and XOR in the new character mask
                    diff = (1 << (ord(old_char) - 97)) ^ (1 << (ord(new_char) - 97))
                    add(in_time[u], diff)
                    add(out_time[u], diff)
                    current_chars[u] = new_char
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                # Fetch root-to-node XOR path sums
                mask_u = query(in_time[u])
                mask_v = query(in_time[v])
                
                # Fetch the LCA mask directly
                mask_lca = 1 << (ord(current_chars[lca]) - 97)
                
                # XORing them together gives the exact path between u and v
                path_mask = mask_u ^ mask_v ^ mask_lca
                
                # Validate palindrome condition: at most 1 bit is set
                if (path_mask & (path_mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans
        