class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myhash = set()
        for i in range(len(nums)):
            if nums[i] in myhash:
                return True
            myhash.add(nums[i])
        return False
