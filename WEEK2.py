#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        arr.sort()
        return arr[k-1]



#Given an array arr[] denoting heights of n towers and a positive integer k.
#For each tower, you must perform exactly one of the following operations exactly once.
#Increase the height of the tower by k
#Decrease the height of the tower by k

class Solution:
    def getMinDiff(self, arr, k):
        # code here
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
            



#You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
class Solution:
	def minJumps(self, arr):
	    # code here
	    n = len(arr)
	    if n <= 1:
	        return 0
        if arr[0] == 0:
            return -1
        maxReach = arr[0]
        steps = arr[0]
        jumps = 1
        for i in range(1,n):
            if i == n-1:
                return jumps
            maxReach = max(maxReach, i + arr[i])
            steps -= 1
            if steps == 0:
                jumps += 1
                if i >= maxReach:
                    return -1
                steps = maxReach -i
        return -1




#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#There is only one repeated number in nums, return this repeated number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow



#Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.
import math
class Solution:
    def mergeArrays(self, a, b):
        n, m = len(a), len(b)
        gap = math.ceil((n + m)/2)
        while gap > 0:
            i = 0
            j = gap
            while j < n + m:
                if i < n and j < n:
                    if a[i] > a[j]:
                        a[i], a[j] = a[j], a[i]
                elif i < n and j >= n:
                    if a[i] > b[j-n]:
                        a[i], b[j-n] = b[j-n], a[i]
                else:
                    if b[i-n] > b[j-n]:
                        b[i-n], b[j-n] = b[j-n], b[i-n]
                i += 1
                j += 1
            if gap == 1:
                gap = 0
            else:
                gap = math.ceil(gap/2)



#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1],end)
        return merged




#Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array. In this case, the output will be -1.
class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k =0
        res = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                if not res or res[-1] != arr1[i]:
                    res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                mn = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == mn:
                    i += 1
                elif arr2[j] == mn:
                    j += 1
                else:
                    k += 1
        return res if res else [-1]




#Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.
class Solution:
    def factorial(self, n):
        res = [1]
        for i in range(2 , n + 1):
            carry = 0
            for j in range (len(res)):
                product = res[j] * i + carry
                res[j] = product % 10
                carry = product // 10
            while carry:
                res.append(carry % 10)
                carry //= 10
        return res[::-1]



#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].
class Solution:
    def isSubset(self, a, b):
        f = {}
        for x in a:
            f[x] = f.get(x,0) + 1
        for y in b:
            if y not in f or f[y] == 0:
                return False
            f[y] -= 1
        return True




        
#Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.
class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)
        for i in range(n-2):
            left = i + 1
            right = n-1
            while left < right:
                s = arr[i] + arr[left] + arr[right]
                if s == target:
                    return True
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return False




#Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

class Solution:
    def maxWater(self, arr):
        n = len(arr)
        left = 0
        right = n-1
        left_max = 0
        right_max = 0
        water = 0
        while left < right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1
        return water
        
