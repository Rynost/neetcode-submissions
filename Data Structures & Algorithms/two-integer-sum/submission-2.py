class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if nums[i] in hash:
                return [hash[nums[i]], i]
            hash[diff] = i
        return []