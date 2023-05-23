def partition(string, low, high):
    i = low - 1
    pivot = string[high]
  
    for j in range(low, high):
        if string[j] <= pivot:
            i = i + 1
            string[i], string[j] = string[j], string[i]
  
    string[i + 1], string[high] = string[high], string[i + 1]
    return i + 1
  
def quickSort(string, low, high):
    if low < high:
        pi = partition(string, low, high)
  
        quickSort(string, low, pi - 1)
        quickSort(string, pi + 1, high)
  
def sortString(string):
    # Converter a string em uma lista mutável
    string = list(string)
  
    # Chamar o algoritmo de classificação QuickSort
    quickSort(string, 0, len(string) - 1)
  
    # Converter a lista de volta para uma string
    sorted_string = ''.join(string)
  
    return sorted_string


# Exemplo de uso
input_string = "acbaaaccca"
sorted_string = sortString(input_string)
print(sorted_string)  # Output: "abcdxyz"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False
        
        s = sortString(s)
        t = sortString(t)

        if t == s:
            return True
    
        return False
    
solution = Solution ()

s = "anagram"
t = "nagaram"

print(solution.isAnagram(s,t))