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
