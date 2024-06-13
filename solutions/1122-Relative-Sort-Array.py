import collections
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        freq=collections.Counter(arr1)
        print(freq)
        arr1=[]
        rest=[]
        for i in arr2:
            for j in range(freq[i]):
                arr1.append(i)
        for i in freq.keys():
            if i not in arr1:
                for j in range(freq[i]):
                    rest.append(i)
        rest.sort()
        arr1.extend(rest)
        return arr1
