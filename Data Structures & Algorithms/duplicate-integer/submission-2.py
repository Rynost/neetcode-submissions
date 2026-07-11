class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myhash = set()
        for i in nums:
            if i in myhash:
                return True
            myhash.add(i)
        return False