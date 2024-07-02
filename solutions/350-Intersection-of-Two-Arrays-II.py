class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1)<len(nums2):
            a=nums1
            b=nums2
        else:
            a=nums2
            b=nums1
        sol=[]
        n=len(a)
        c=0
        while c!=n:
            c+=1
            for i in a:
                if i in b:
                    sol.append(i)
                    a.remove(i)
                    b.remove(i)
                    print(a,b)
        return sol
