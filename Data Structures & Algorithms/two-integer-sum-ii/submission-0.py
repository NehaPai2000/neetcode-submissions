class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)-1):
            half=target-numbers[i]
            start=i+1
            end=len(numbers)-1
            while start<=end:
                   mid=int((start+end)/2)
                   if half==numbers[mid]:
                      return [i+1,mid+1]
                   if half<numbers[mid]:
                      end=mid-1
                   else:
                      start=mid+1
    