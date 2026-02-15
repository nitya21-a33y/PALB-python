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




