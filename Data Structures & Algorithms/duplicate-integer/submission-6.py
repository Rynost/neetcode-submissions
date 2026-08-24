class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myhash = set()
        for i, n in enumerate(nums):
            if n in myhash:
                return True
            myhash.add(n)
        return False