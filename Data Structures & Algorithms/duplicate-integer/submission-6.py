class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Given a number return True if any number appears more than once in the array else false

        #Firstlt irrate over the array
        #.seen() that pushes the number in array into the seen
        #if in .seen() return true

        NumSenn =  set()

        for i in range(len(nums)):
            if nums[i] in NumSenn:
                return True 
            else:
                 NumSenn.add(nums[i])
        
        return False
        