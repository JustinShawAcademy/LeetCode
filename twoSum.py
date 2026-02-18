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
        for i in range(len(nums)):
            if (target - nums[i]) in dict:
                return [i, dict[target - nums[i]]]
            dict[nums[i]]=i

#Use case 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


