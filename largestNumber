from typing import List
class Solution:
  def largestNumber(self,nums:List[int])->str:
    lst=[]
    for ele in nums:
      lst+=[str(ele)]
    n=len(lst)
    for i in range(n):
      for j in range(i+1,n):
        if lst[i]+lst[j]>lst[j]+lst[i]:
          continue
        else:
          lst[i],lst[j]=lst[j],lst[i]
    ans=''.join(lst)
    if int(ans)==0:
      return "0"
    return ans

obj=Solution()
print(obj.largestNumber([10,2]))
