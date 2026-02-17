class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """


        for i in range(len(nums)-1,-1,-1): 
            if nums[i]==val:
                nums.pop(i)

    
    #Explanation: Starting from the right side of the array, keep going back and remove the val value in the array until its left