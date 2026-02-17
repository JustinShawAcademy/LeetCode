#BruteForce
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:   
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

#Optimal
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict = {}
        for number in nums:
            if number in dict:
                return True
            dict[number] = 1
            #Add each number to the dictionary no matter what
            #dict = {1:1, 2:1, 5:1} if nums = [1,2,5]
            #use 1 as a placeholder
        return False
    
