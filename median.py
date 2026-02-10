# Given an array arr[] of integers, calculate the median.
class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n = len(arr)
        if n%2 == 1:
            median = arr[n//2]
        else:
            median = (arr[n//2 - 1] + arr[n//2]) / 2
            
        return median
            
