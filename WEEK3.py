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
        




#
