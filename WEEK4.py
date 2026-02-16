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





#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, curr, total):
            if total == target:
                result.append(curr[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, total + candidates[i])  # reuse allowed
                curr.pop()
        backtrack(0, [], 0)
        return result



#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#Each number in candidates may only be used once in the combination.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(start, curr, total):
            if total == target:
                result.append(curr[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])  # move forward (no reuse)
                curr.pop()
        backtrack(0, [], 0)
        return result




#You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
#Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
#0 <= j <= nums[i] and
#i + j < n
#Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        current_end = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps




#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            mp[key].append(word)
        return list(mp.values())




#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits



#

 
