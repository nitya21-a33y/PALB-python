#Given an array arr[] denoting heights of n towers and a positive integer k.
#For each tower, you must perform exactly one of the following operations exactly once.
#Increase the height of the tower by k
#Decrease the height of the tower by k
#Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        ans = arr[n-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[n-1] - k
        for i in range(1,n):
            if arr[i] - k < 0:
                continue
            minimum = min(smallest, arr[i] - k)
            maximum = max(largest, arr[i - 1] + k)
            ans = min(ans, maximum - minimum)
        return ans
