import math

class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        mod = 10**9 + 7
       
        block_size = int(math.sqrt(n))
        
        light_queries = [[] for _ in range(block_size + 1)]
        
        for l, r, k, v in queries:
            if k > block_size:
                
                curr = l
                while curr <= r:
                    nums[curr] = (nums[curr] * v) % mod
                    curr += k
            else:
                light_queries[k].append((l, r, v))
        
        
        for k in range(1, block_size + 1):
            if not light_queries[k]:
                continue
            
            
            diff = [1] * (n + k + 1)
            for l, r, v in light_queries[k]:
               
                diff[l] = (diff[l] * v) % mod
                
                
                inv_v = pow(v, mod - 2, mod)
                last_pos = l + ((r - l) // k) * k
                if last_pos + k < n:
                    diff[last_pos + k] = (diff[last_pos + k] * inv_v) % mod
            
            
            for i in range(k, n):
                diff[i] = (diff[i] * diff[i-k]) % mod
            
            
            for i in range(n):
                if diff[i] != 1:
                    nums[i] = (nums[i] * diff[i]) % mod
                    
        
        ans = 0
        for x in nums:
            ans ^= x
        return ans