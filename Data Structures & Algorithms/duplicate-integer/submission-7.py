class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHash = set()
        for num in nums:
            if num in myHash:
                return True
            myHash.add(num)
        return False