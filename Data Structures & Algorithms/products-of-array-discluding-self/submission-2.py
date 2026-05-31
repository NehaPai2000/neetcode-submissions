class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=suffix=1
        output=[1]*len(nums)
        for i in range(1,len(nums)):
            prefix*=nums[i-1]
            output[i]=prefix
        for i in range(len(nums)-2,-1,-1):
            suffix*=nums[i+1]
            output[i]*=suffix
        return output