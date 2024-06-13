class Solution(object):
    def replaceWords(self, dictionary, sentence):
        arr=sentence.split()
        r=""
        for i in range(len(arr)):
            for j in dictionary:
                if arr[i][:len(j)] == j:
                    arr[i]=j
            r+=arr[i]
            r+=" "
        return r.rstrip()