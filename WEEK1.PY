
#You are given an array of integers arr[]. You have to reverse the given array.
class Solution:
    def reverseArray(self, arr):
        # code here
        left = 0
        right = len(arr)-1
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1


#Given an array arr[]. Your task is to find the minimum and maximum elements in the array.
class Solution:
    def getMinMax(self, arr):
        # code here
        minimum = arr[0]
        maximum = arr[0]
        for i in arr:
            if minimum > i:
                minimum = i
        
        for i in arr:
            if maximum < i:
                maximum = i
        return[minimum,maximum]


#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        arr.sort()
        return arr[k-1]
        
