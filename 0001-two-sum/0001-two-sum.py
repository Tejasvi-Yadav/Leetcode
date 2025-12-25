class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i , nums in enumerate(nums):
            sub = target - nums

            if sub in hashmap:
                return (hashmap[sub], i)

            hashmap[nums]=i