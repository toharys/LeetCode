class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits==[9]: # base case
            return [1,0]
        if digits[len(digits)-1]!=9: # "regular" case, we just need to add 1 to the lower digit
                digits[len(digits)-1]+=1
                return digits
        else: # in case we have a 'carry'
            digits[len(digits)-1]=0
            return self.plusOne(digits[0:len(digits)-1]) + digits[len(digits)-1:]      
