class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            if target - n1 in nums:
                for j , n2 in enumerate(nums):
                    if i != j and n1 + n2 == target:
                        return [i, j]

