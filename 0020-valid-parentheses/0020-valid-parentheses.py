class Solution(object):
    def isValid(self, s):
        c=0
        s1=[]
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="[" or s[i]=="{"):
                s1.append(s[i])
                c+=1
            elif(s[i]==")" or s[i]=="]" or s[i]=="}"):
                if(c==-1):
                    return False
                elif(not s1):
                    return False
                top=s1.pop()
                if((s[i]==")" and top=="(") or (s[i]=="]" and top=="[") or (s[i]=="}" and top=="{") ):
                    c-=1
                else:
                    return False
        if(c==0):
            return True
        else:
            return False