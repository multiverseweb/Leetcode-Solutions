class Solution:
    def maxSatisfied(self,customers, grumpy, minutes):
        n=len(customers)
        ans=0
        for i in range(n):
            if grumpy[i]==0:
                ans += customers[i]
                customers[i]=0

        max_count=sum(customers[:minutes])
        cur_count=max_count
        for i in range(1,n-minutes+1):
            cur_count=cur_count-customers[i-1] +customers[i+minutes-1]
            max_count=max(max_count, cur_count)
        return ans+max_count
