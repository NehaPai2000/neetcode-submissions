class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        count=0
        for i in nums:
            if i==0:
               if count==1:
                  product=0
                  count+=1
                  
               else:
                  count+=1
                  continue

            product=product*i
        output=[0]*len(nums)
        for i in range(0,len(nums)):
            if count>=1:
                if nums[i]==0:
                    output[i]=product
                else:
                    output[i]=0
            else:
                output[i]=int(product/nums[i])
        return output
            
