class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a) - 1
        lenb = len(b) - 1
        answer = ''
        carry = 0
        while lena >= 0 or lenb >= 0:
            tempa = int(a[lena]) if lena >=0 else 0
            tempb = int(b[lenb]) if lenb >= 0 else 0
        
            # sum = tempa + tempb + carry
            if tempa + tempb + carry == 2:
                answer = '0' + answer
                carry = 1
            elif tempa + tempb + carry == 3:
                answer = '1' + answer
                carry = 1
            else:
                answer = str(tempa + tempb + carry) + answer
                carry = 0
            
            lena-= 1
            lenb-= 1
            
        if carry == 1:
            answer = str(carry) + answer
            
        return answer