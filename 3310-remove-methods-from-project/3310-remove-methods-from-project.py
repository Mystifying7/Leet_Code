class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        
        # Step 1: Build the directed graph using an adjacency list
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 2: Use BFS to find all suspicious methods starting from k
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Validate if any non-suspicious method invokes a suspicious method
        can_remove = True
        for u, v in invocations:
            # If 'u' is outside the group and 'v' is inside, we cannot remove the group
            if u not in suspicious and v in suspicious:
                can_remove = False
                break
                
        # Step 4: Return the remaining methods based on the validation check
        if can_remove:
            return [i for i in range(n) if i not in suspicious]
        else:
            return list(range(n))