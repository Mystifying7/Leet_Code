class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        count0 = 0
        count1 = 0
        count2 = 0
        
        # Count the frequencies of each remainder modulo 3
        for stone in stones:
            rem = stone % 3
            if rem == 0:
                count0 += 1
            elif rem == 1:
                count1 += 1
            else:
                count2 += 1
                
        # If the number of 0s is even, Alice wins if both 1s and 2s are present
        if count0 % 2 == 0:
            return count1 > 0 and count2 > 0
            
        # If the number of 0s is odd, Alice needs a large imbalance to win
        else:
            return abs(count1 - count2) > 2