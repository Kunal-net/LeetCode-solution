class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        for i in digits :
            num = num*10 + i
        num = num + 1
        digits = []
        for i in range(len(str(num))):
            j = num % 10
            digits.append(j)
            num = num // 10
        
        digits.reverse()
        return digits

