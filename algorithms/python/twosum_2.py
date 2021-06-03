class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            d[n] = i
        for i,n in enumerate(nums):
            tmp = target - nums[i]
            if tmp in d.keys() and d[tmp] != i:
                return [i,d[tmp]]
        return []
