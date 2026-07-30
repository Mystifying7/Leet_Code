class Solution(object):
    def minimumPushes(self, word):
        total_pushes = 0
        n = len(word)
        
        # Calculate the number of pushes for each distinct character
        for i in range(n):
            # Every 8 characters, the cost increases by 1
            cost = (i // 8) + 1
            total_pushes += cost
            
        return total_pushes