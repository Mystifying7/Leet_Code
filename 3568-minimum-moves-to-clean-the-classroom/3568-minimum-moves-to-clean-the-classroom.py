from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m = len(classroom)
        n = len(classroom[0])
        
        start = None
        litter_to_id = {}
        litter_id = 0
        
        # Parse the grid to find the start and all litter positions
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_to_id[(r, c)] = litter_id
                    litter_id += 1
                    
        num_litter = litter_id
        target_mask = (1 << num_litter) - 1
        
        # If there is no litter to collect, it takes 0 moves
        if target_mask == 0:
            return 0
            
        # Queue stores: (moves, r, c, mask, curr_energy)
        q = deque([(0, start[0], start[1], 0, energy)])
        
        # visited maps (r, c, mask) to the maximum energy recorded at that state
        visited = {}
        visited[(start[0], start[1], 0)] = energy
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            moves, r, c, mask, curr_energy = q.popleft()
            
            # If the student is stranded with 0 energy (and not on an 'R'), they can't move
            if curr_energy == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    
                    # If we don't have enough energy to make the move, skip
                    if next_energy < 0:
                        continue
                        
                    next_mask = mask
                    cell = classroom[nr][nc]
                    
                    if cell == 'L':
                        next_mask |= (1 << litter_to_id[(nr, nc)])
                    elif cell == 'R':
                        next_energy = energy
                        
                    # Early exit if we collected everything
                    if next_mask == target_mask:
                        return moves + 1
                        
                    state = (nr, nc, next_mask)
                    # We only process this state if it offers strictly more energy than previously seen
                    if state not in visited or visited[state] < next_energy:
                        visited[state] = next_energy
                        q.append((moves + 1, nr, nc, next_mask, next_energy))
                        
        return -1