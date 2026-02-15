#You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        current_sum = arr[0]
        maximum_sum = arr[0]
        for i in range(1,len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            maximum_sum = max(maximum_sum, current_sum)
        return maximum_sum
        

#Given an array arr, rotate the array by one position in clockwise direction.
class Solution:
    def rotate(self, arr):
        last = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
            
        arr[0] = last
        return arr
            
    
