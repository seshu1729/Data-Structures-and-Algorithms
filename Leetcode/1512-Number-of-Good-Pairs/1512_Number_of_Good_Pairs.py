class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if i < j and nums[i]==nums[j]:
                    c = c + 1
        #print(c)
        return c