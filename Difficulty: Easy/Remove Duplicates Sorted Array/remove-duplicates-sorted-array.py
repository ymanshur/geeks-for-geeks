class Solution:
    def removeDuplicates(self, arr):
        j = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                continue
            
            arr[j] = arr[i]
            j += 1
        
        return arr[:j]
