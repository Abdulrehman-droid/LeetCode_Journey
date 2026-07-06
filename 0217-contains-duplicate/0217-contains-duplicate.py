class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map={}
        count=0
        for i in nums:
            if i in hash_map:
                return True
            hash_map[i] = count + 1
        return False