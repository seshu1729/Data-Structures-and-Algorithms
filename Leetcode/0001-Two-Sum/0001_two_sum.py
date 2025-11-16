class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in nums_dict:
                return [nums_dict[compliment], i]
            nums_dict[num] = i