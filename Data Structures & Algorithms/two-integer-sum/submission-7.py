class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in myhash:
                return [myhash[diff], i]
            myhash[n] = i
        