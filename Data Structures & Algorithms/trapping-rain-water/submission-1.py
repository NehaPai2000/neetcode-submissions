class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxl=height[0]
        maxr=height[len(height)-1]
        area=0
        while l<r:
            if maxl<maxr:
                l+=1
                if maxl<height[l]:
                    area+=0
                else:
                    area+=maxl-height[l]
                maxl=max(maxl,height[l])
            else:
                r-=1
                if maxr<height[r]:
                    area+=0
                else:
                    area+=maxr-height[r]
                maxr=max(maxr,height[r])
        return area
              
