class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = ''
        number = str(num)

        while number != '':
            if len(number) == 4:
                for i in range(int(number [0])):
                    Roman += "M"
                number = number[1::1]
            elif len(number) == 3:
                if int(number [0]) == 9:
                    Roman += "CM"
                elif int(number [0]) >= 5:
                    Roman += "D"
                    for i in range (int(number [0])-5):
                        Roman += "C"
                elif int(number [0]) == 4:
                     Roman += "CD"
                else:
                    for i in range (int(number [0])):
                        Roman += "C"
                number = number[1::1]
            elif len(number) == 2:
                if int(number [0]) == 9:
                    Roman += "XC"
                elif int(number [0]) >= 5:
                    Roman += "L"
                    for i in range (int(number [0])-5):
                        Roman += "X"
                elif int(number [0]) == 4:
                     Roman += "XL"
                else:
                    for i in range (int(number [0])):
                        Roman += "X"
                number = number[1::1]
            elif len(number) == 1:
                if int(number [0]) == 9:
                    Roman += "IX"
                elif int(number [0]) >= 5:
                    Roman += "V"
                    for i in range (int(number [0])-5):
                        Roman += "I"
                elif int(number [0]) == 4:
                     Roman += "IV"
                else:
                    for i in range (int(number [0])):
                        Roman += "I"
                number = ''
                
        return Roman


solution = Solution()

print(solution.intToRoman(777))
