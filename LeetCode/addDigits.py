def teste (num: int) -> int:
    print (num)
    return num

num = teste(1.5)

print (num)



# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num > 9:
#             soma = 0
#             while num > 0:
#                 soma += num % 10
#                 num -= num % 10
#                 num //= 10
#             return self.addDigits(soma)
#         else:
#             return num
