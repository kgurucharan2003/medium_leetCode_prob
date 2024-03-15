from typing import List 
class Solution:
  def maxProfit(self,prices:List[int]):
    n=len(prices)
    profit=0
    for i in range(1,n):
      if prices[i]>prices[i-1]:
        profit+=prices[i]-prices[i-1]
    return profit
    
obj=Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
