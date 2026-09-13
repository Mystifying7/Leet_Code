import collections

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        
        # Step 1: Collect coordinates of all 1s from both images
        ones1 = []
        ones2 = []
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))
                if img2[r][c] == 1:
                    ones2.append((r, c))
                    
        # If either image contains no 1s, the overlap must be 0
        if not ones1 or not ones2:
            return 0
            
        # Step 2: Count frequencies of each translation vector (dr, dc)
        vector_counts = collections.defaultdict(int)
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                dr = r2 - r1
                dc = c2 - c1
                vector_counts[(dr, dc)] += 1
                
        # Step 3: The maximum count of a single vector is the maximum overlap
        return max(vector_counts.values())