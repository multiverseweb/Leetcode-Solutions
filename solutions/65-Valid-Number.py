class Solution(object):
    def isNumber(self, s):
        s=s.replace('E','e')
        if s=="e" or s=="." or s==".e" or s[-1] in ['+','-']:
            return False
        temp=s
        temp=temp.replace('.','')
        temp=temp.replace('+','')
        temp=temp.replace('-','')
        if len(temp)==0:
            return False
        for i in s:
            if (not (i.isnumeric()) and i!='e') and i not in ['+','-','.']:
                return False
        if 'e' not in s:
            c=0
            c2=0
            for i in s:
                if i in ['+','-']:
                    c+=1
                if i=='.':
                    c2+=1
            if c>1 or c2>1:
                return False
            if ('+' in s or '-' in s) and s[0] not in ['+','-']:
                return False
            
        if 'e' in s:
            c=0
            for i in s:
                if i=='e':
                    c+=1
            if c>1:
                return False
            arr=s.split('e')
            arr[0]=arr[0].replace('.','',1)
            if '.' in arr[0]:
                return False
            flag=False
            for i in arr:
                c=0
                for j in i:
                    if j in ['+','-']:
                        c+=1
                if c>1:
                    return False
            for i in arr:
                if len(i)==0:
                    return False
                if i == "." or i=="+" or i=='-':
                    return False
                if i[-1] in ['+','-']:
                    return False
                if ('+' in i or '-' in i) and i[0] not in ['+','-']:
                    return False
                if ((i[0].isnumeric() or i[0] in ['+','-'])) and '.' not in arr[-1]:
                    flag=True
                else:
                    flag=False
            return flag
            
        s=s.replace('.','',1)
        if '.' in s:
            return False
        if not (s.isnumeric()) and s.isalnum() and 'e' not in s:
            return False
        if s.isnumeric():
            return True
        if s[0].isnumeric() or s[0] in ['+','-']:
            return True