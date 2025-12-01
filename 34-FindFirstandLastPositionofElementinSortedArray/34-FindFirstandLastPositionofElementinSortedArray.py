# Last updated: 12/1/2025, 12:06:23 PM
1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3\
4        def search(nums, target, isSearchLeft):
5            i = 0
6            j = len(nums)-1
7            res = -1
8            while i <= j:
9                mid = (i+j)//2
10                if nums[mid] < target:
11                    i = mid+1
12                elif nums[mid] > target:
13                    j = mid-1
14                else:
15                    res = mid
16                    if isSearchLeft:
17                        j = mid-1
18                    else:
19                        i = mid+1
20            return res
21        
22        left = search(nums,target,True)
23        right = search(nums,target,False)
24
25        return [left,right]
26
27