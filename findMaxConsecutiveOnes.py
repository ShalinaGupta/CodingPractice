class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        count = 0
        res = 0
        n = 1
        for i in nums:
            if i==n:
                count=count+1
                res = max(res, count)
            else:
                count=0
        return res
            
    
        
    

nums = [0,1,1,0,0,1,1,1,0,1,1]
sol = Solution()
output = sol.findMaxConsecutiveOnes(nums)
print(output)
