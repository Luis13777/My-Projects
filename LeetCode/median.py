from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        merged = []

        i = 0
        j = 0

        while (i<size1 or j<size2):
            if (i == size1):
                merged.append(nums2[j])
                j += 1
            elif (j == size2):
                merged.append(nums1[i])
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1

        if ((size1 + size2)%2 == 0):
            x = int((size1 + size2)/2)
            return (merged[x] + merged[x - 1])/2
        else:
            return merged [int((size1 + size2 - 1)/2)]

        

solucao = Solution()
print(solucao.findMedianSortedArrays([1,2,2,99],[1,2,3,4]))