#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        arr.sort()
        return arr[k-1]
        print(kthSmallest(arr,k))
