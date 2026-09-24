class Solution(object):
    def plusOne(self, digits):
        digits=int("".join(map(str,digits)))
        digits+=1
        digits=list(map(int,str(digits)))
        return digits

