class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if(nums[i]==target):
                return i
        for i in range(len(nums)):        
            if(nums[i]!=target):
                nums.append(target)
                nums.sort()
        for i in range(len(nums)):    
            if(nums[i]==target):
                return i

            