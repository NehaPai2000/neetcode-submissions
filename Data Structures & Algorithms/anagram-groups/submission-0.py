class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr=[0]*26
        hm={}
        
        for i in strs:
            for j in i:
                x=ord(j)-ord('a')
                arr[x]+=1
            if tuple(arr) in hm:
                hm[tuple(arr)].append(i)
            else:
                hm[tuple(arr)] = [i]
            arr=[0]*26
        strs1=[]
        for i in hm:
             strs1.append(hm[i])
        return strs1

