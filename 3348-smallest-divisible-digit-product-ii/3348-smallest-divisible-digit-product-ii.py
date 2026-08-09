class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # 1. Factorize t
        temp = t
        req = [0, 0, 0, 0] # 2, 3, 5, 7
        for idx, p in enumerate([2, 3, 5, 7]):
            while temp % p == 0:
                req[idx] += 1
                temp //= p
        
        # If t has prime factors other than 2, 3, 5, 7, it's impossible
        if temp > 1:
            return "-1"
            
        # 2. DP to find min digits needed for r2 twos and r3 threes
        dp = [[float('inf')] * 32 for _ in range(50)]
        dp[0][0] = 0
        
        # Digits that provide factors of 2 and 3
        moves = [
            (1, 0), # 2
            (0, 1), # 3
            (2, 0), # 4
            (1, 1), # 6
            (3, 0), # 8
            (0, 2)  # 9
        ]
        
        for i in range(50):
            for j in range(32):
                if i == 0 and j == 0:
                    continue
                best = float('inf')
                for f2, f3 in moves:
                    ni = max(0, i - f2)
                    nj = max(0, j - f3)
                    if 1 + dp[ni][nj] < best:
                        best = 1 + dp[ni][nj]
                dp[i][j] = best
                
        def get_factors(d):
            f2 = f3 = f5 = f7 = 0
            if d in (2, 4, 6, 8):
                temp = d
                while temp % 2 == 0: f2 += 1; temp //= 2
            if d in (3, 6, 9):
                temp = d
                while temp % 3 == 0: f3 += 1; temp //= 3
            if d == 5: f5 = 1
            if d == 7: f7 = 1
            return (f2, f3, f5, f7)
            
        # 3. Check if num itself is valid
        if '0' not in num:
            f2 = f3 = f5 = f7 = 0
            for char in num:
                c2, c3, c5, c7 = get_factors(int(char))
                f2 += c2; f3 += c3; f5 += c5; f7 += c7
            if f2 >= req[0] and f3 >= req[1] and f5 >= req[2] and f7 >= req[3]:
                return num
                
        # 4. Precompute prefix factors up to the first '0'
        z_idx = num.find('0')
        if z_idx == -1:
            z_idx = len(num)
            
        pref = [[0, 0, 0, 0]]
        for i in range(z_idx):
            c2, c3, c5, c7 = get_factors(int(num[i]))
            pref.append([
                pref[-1][0] + c2, pref[-1][1] + c3,
                pref[-1][2] + c5, pref[-1][3] + c7
            ])
            
        def check_valid(curr_req, rem_len):
            r2, r3, r5, r7 = curr_req
            if r5 + r7 > rem_len: return False
            return dp[r2][r3] + r5 + r7 <= rem_len
            
        n = len(num)
        
        # 5. Find the longest valid prefix and replacement digit
        for i in range(min(n - 1, z_idx), -1, -1):
            p_f2, p_f3, p_f5, p_f7 = pref[i]
            start_d = int(num[i]) + 1
            
            for d in range(start_d, 10):
                d_f2, d_f3, d_f5, d_f7 = get_factors(d)
                rem_req = (
                    max(0, req[0] - p_f2 - d_f2), max(0, req[1] - p_f3 - d_f3),
                    max(0, req[2] - p_f5 - d_f5), max(0, req[3] - p_f7 - d_f7)
                )
                rem_len = n - 1 - i
                
                if check_valid(rem_req, rem_len):
                    ans = num[:i] + str(d)
                    curr_r2, curr_r3, curr_r5, curr_r7 = rem_req
                    
                    # Greedily build remainder string 
                    for k in range(rem_len):
                        for c in range(1, 10):
                            c_f2, c_f3, c_f5, c_f7 = get_factors(c)
                            n_r2, n_r3 = max(0, curr_r2 - c_f2), max(0, curr_r3 - c_f3)
                            n_r5, n_r7 = max(0, curr_r5 - c_f5), max(0, curr_r7 - c_f7)
                            
                            if check_valid((n_r2, n_r3, n_r5, n_r7), rem_len - 1 - k):
                                ans += str(c)
                                curr_r2, curr_r3, curr_r5, curr_r7 = n_r2, n_r3, n_r5, n_r7
                                break
                    return ans
                    
        # 6. If no valid number of the same length exists, build a longer one
        min_len_for_t = req[2] + req[3] + dp[req[0]][req[1]]
        new_len = max(n + 1, min_len_for_t)
        
        ans = ""
        curr_r2, curr_r3, curr_r5, curr_r7 = req
        for k in range(new_len):
            for c in range(1, 10):
                c_f2, c_f3, c_f5, c_f7 = get_factors(c)
                n_r2, n_r3 = max(0, curr_r2 - c_f2), max(0, curr_r3 - c_f3)
                n_r5, n_r7 = max(0, curr_r5 - c_f5), max(0, curr_r7 - c_f7)
                
                if check_valid((n_r2, n_r3, n_r5, n_r7), new_len - 1 - k):
                    ans += str(c)
                    curr_r2, curr_r3, curr_r5, curr_r7 = n_r2, n_r3, n_r5, n_r7
                    break
                    
        return ans