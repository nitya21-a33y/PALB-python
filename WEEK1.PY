
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



#You are given two arrays a[] and b[], return the Union of both the arrays in any order.
#METHOD 1
class Solution:    
    def findUnion(self, a, b):
        # code here
        return list(set(a) | set(b))

#METHOD 2
class Solution:    
    def findUnion(self, a, b):
        # code here
        result = []
        for x in a:
            if x not in result:
                result.append(x)
        
        for y in b:
            if y not in result:
                result.append(y)
        return result


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


#You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
#Kadane's Algorithm
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



#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
