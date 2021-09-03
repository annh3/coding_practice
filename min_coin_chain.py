class Solution:
    def coinDP(self,sol_idx, coins, cache):
        if sol_idx in cache:
            return cache[sol_idx]
        
        if sol_idx == 0:
            cache[sol_idx] = 0
            return 0
        
        amt_rem = sol_idx
        
        #print("HELLO")
        
        min_val = 100000
        for c in coins:
            if amt_rem - c >= 0:
                tmp_val = self.coinDP(amt_rem-c, coins, cache)
                if tmp_val >= 0:
                    cur_val = 1 + tmp_val
                else:
                    cur_val = tmp_val
                #print("cur val: ", cur_val)
                if cur_val >= 0 and cur_val < min_val:
                    min_val = cur_val # num coints
        
        if min_val == 100000:
            cache[sol_idx] = -1
            return -1
            
        cache[sol_idx] = min_val
        return min_val
                
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # return the fewest number of coins that you need to make up that aount
        # coins [1,2,5,10]
        # return min( subproblems )
        # assuming that coins are infinite, problems are indexed by (amount left, cur # coins)
        # at each step, we can take any of the available coins
        # for coin in coins,
        #       recurse on solution using that coin, and solution skipping that coin
        # cach by problem index (amount left, cur # coins)
        cache = {}
        return self.coinDP(amount, coins, cache)#annhe
