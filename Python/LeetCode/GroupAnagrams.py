# def sortingString (string):
#     # if (len(string) <= 1):
#     #     return string
#     # i = 1
#     # string = list(string)
#     # while (i<len(string)):
#     #     j = i
#     #     while (j>0):
#     #         if string[j] > string[j-1]:
#     #             tmp = string[j-1]
#     #             string[j-1] = string[j]
#     #             string[j] = tmp
#     #             j -= 1
#     #         else:
#     #             break
#     #     i += 1

#     return ''.join(sorted(string))

#     # return ''.join(string)

# def isAnagram (str1, str2):
#     str11 = sortingString(str1)
#     str22 = sortingString(str2)

#     if (str11 == str22):
#         return True
#     return False

# class Solution:
#     def groupAnagrams(self, strs):

#         answer = []
#         while len(strs) > 0:
#             string = strs[0]
#             tmpAnswer = [string]
#             i = 1
#             while i < len(strs):
#                 if isAnagram (string, strs[i]):
#                     tmpAnswer.append(strs[i])
#                     del strs[i]
#                     i -= 1
#                 i += 1 
#             answer.append(tmpAnswer)
#             del strs[0]
        

#         return answer



# solution = Solution ()

# strs = ["eat","tea","tan","ate","nat","bat"]
# print(solution.groupAnagrams(strs))
# # print(sortingString("eat"))

# # strs = []

# # string = "bat"
# # tmpAnswer = ["bat"]
# # answer = [["eat", "tea", "ate"],["tan", "nat"],["bat"]]


class Solution:
    def groupAnagrams(self, strs):
        res = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            tuple_count = tuple(count)

            if tuple_count in res:
                res[tuple_count].append(s)
            else:
                res[tuple_count] = [s]

        return list(res.values())
    

solution = Solution ()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))

