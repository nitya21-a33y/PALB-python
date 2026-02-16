#Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that -
     # i. Each student gets exactly one packet.
     #ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.
class Solution:
    def findMinDiff(self, arr,M):
        arr.sort()
        n = len(arr)
        min_diff = float('inf')
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]
            min_diff = min(min_diff, diff)
            
        return min_diff

#Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.
class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        start = 0
        current_sum = 0
        min_len = float('inf')
        for end in range(n):
            current_sum += arr[end]
            while current_sum > x:
                min_len = min(min_len, end-start + 1)
                current_sum -= arr[start]
                start += 1
        return 0 if min_len == float('inf') else min_len
        



#Given an array and a range a, b. The task is to partition the array around the range such that the array is divided into three parts.
#1) All elements smaller than a come first.
#2) All elements in range a to b come next.
#3) All elements greater than b appear in the end.
#The individual elements of three sets can appear in any order. You are required to return the modified array.
class Solution:
	def threeWayPartition(self, arr, a, b):
	    low = 0
        mid = 0
        high = len(arr) - 1
        while mid <= high:
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif a <= arr[mid] <= b:
                mid += 1
            else:  
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr




#Given an array arr and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.

class Solution:
    def minSwap (self,arr, k) : 
        n = len(arr)
        good = sum(1 for x in arr if x <= k)
        if good == 0:
            return 0
        bad = sum(1 for x in arr[:good] if x > k)
        ans = bad
        for i in range(good, n):
            if arr[i] > k:
                bad += 1
            if arr[i - good] > k:
                bad -= 1
            ans = min(ans, bad)
        return ans
        




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




#You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.
class Solution:
    def spirallyTraverse(self, mat):
        if not mat:
            return []
        n = len(mat)
        m = len(mat[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        result = []
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                result.append(mat[top][j])
            top += 1
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(mat[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        return result
       




#The first integer of each row is greater than the last integer of the previous row. Given an integer target, return true if target is in matrix or false otherwise.
class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        if not mat or not mat[0]:
            return False
        n = len(mat)
        m = len(mat[0])
        left = 0
        right = n * m - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // m
            col = mid % m
            mid_val = mat[row][col]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False



#Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix
import bisect
class Solution:
    def median(self, mat):
    	n = len(mat)
        m = len(mat[0])
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        required = (n * m) // 2
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid)
            if count <= required:
                low = mid + 1
            else:
                high = mid - 1
        return low



#You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.
class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        max_ones = 0
        ans = -1
        for i in range(n):
            row = arr[i]
            left, right = 0, m - 1
            first_one = m
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    first_one = mid
                    right = mid - 1
                else:
                    left = mid + 1
            ones_count = m - first_one
            if ones_count > max_ones:
                max_ones = ones_count
                ans = i
        return ans
