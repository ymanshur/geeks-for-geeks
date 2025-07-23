class Solution:
    def canAttend(self, arr):
        arr.sort(key=lambda x: x[0])
        for i in range(1, len(arr)):
            if arr[i - 1][1] > arr[i][0]:
                return False
            
        return True
        