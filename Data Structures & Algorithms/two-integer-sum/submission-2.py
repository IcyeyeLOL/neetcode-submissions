class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Given an array of numbers a number called target return indexs i and j such that they equal tagret
        #I and j do not equal each other

        for  i in range(len(nums)):
            for j in range(i+1,len(nums)):
                result = nums[i] + nums[j]
                if result == target:
                    return [i,j]