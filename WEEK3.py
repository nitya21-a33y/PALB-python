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
        



#
