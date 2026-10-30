import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        # Step 1: Build the adjacency list
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            
        # dist[u][run] represents the min distance to node 'u' ending with a 'run' of identical chars
        # Initialize the state space with infinity
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        # Step 2: Min-heap for Dijkstra's algorithm
        # Stores tuples of (distance, current_node, consecutive_run_length)
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, run = heapq.heappop(pq)
            
            # Since edge weights are non-negative, the first time we pop the destination, it is optimal
            if u == n - 1:
                return d
                
            # Prune stale states (paths that were strictly improved before we popped this one)
            if d > dist[u][run]:
                continue
                
            # Step 3: Evaluate neighbors and attempt transitions
            for v, w in g[u]:
                # Calculate the consecutive identical characters count if we move to neighbor v
                nxt_run = run + 1 if labels[u] == labels[v] else 1
                
                # We only proceed if the path stays within the 'k' limit and offers a strictly shorter distance
                if nxt_run <= k and d + w < dist[v][nxt_run]:
                    dist[v][nxt_run] = d + w
                    heapq.heappush(pq, (d + w, v, nxt_run))
                    
        # If the priority queue empties and we never reached n-1, no valid path exists
        return -1