class Solution(object):
    def validMountainArray(self, arr):
        if len(arr)<3:
            return False
        peak=max(arr)
        if arr[0]>=peak or arr[-1]>=peak:
            return False
        peak_pos=arr.index(peak)
        temp=arr[0]
        for i in arr[1:peak_pos]:
            if i<=temp:
                return False
            temp=i
        temp=peak
        for i in arr[peak_pos+1:]:
            if i>=temp:
                return False
            temp=i
        return True
