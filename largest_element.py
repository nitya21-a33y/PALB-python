# Given an array arr[]. The task is to find the largest element and return it.

class Solution:
    def largest(self, arr):
        # code here
        maxim = arr[0]
        for num in arr:
            if maxim < num:
                maxim = num
        return maxim

#USING INBUILT FUNCTION
class Solution:
    def largest(self, arr):
        # code here
        return(max(arr))
