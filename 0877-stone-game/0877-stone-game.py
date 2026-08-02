class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # Alice can always win by choosing all even-indexed piles or all odd-indexed piles.
        return True