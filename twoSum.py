# Brute Force 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j]==target:
                    return [i,j]


# O(n) using a dictionary
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}
        for i, numbers in enumerate(nums): # iterate through index (i) and value (numbers) of array nums
            complement = target - numbers #calculate for the complement
            if complement in dict:
                return [dict[complement],i]  #if complement is in dictionary, return the complement and its index
            else:
                dict[numbers] = i #otherwise set the dictionary to value

#Use case 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


