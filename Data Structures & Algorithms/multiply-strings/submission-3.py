class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        def d(x):
            return ord(x) - ord('0')

        adds = []

        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        nstart = 0
        for i in range(len(num2) - 1, -1, -1):
            n = nstart
            cur = [0] * (len(num2) + len(num1))
            carry = 0
            for j in range(len(num1) - 1, -1, -1):
                p = d(num2[i]) * d(num1[j]) + carry
                cur[n] = p % 10
                carry = p // 10
                n += 1
            if carry:
                cur[n] = carry
                n += 1
            adds.append(cur)
            nstart += 1


        print(adds)
        out = ''

        carry = 0
        
        for digit in range(n):
            cur = 0
            for i in range(len(adds)):
                cur += adds[i][digit]
            cur += carry
            d = cur % 10
            carry = cur // 10
            out = str(d) + out
        
        return out


        
        

        