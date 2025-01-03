# Method - 1 (Brute Force):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Method - 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            somewhat = target - nums[i]
            if somewhat in dict:
                return [dict[somewhat], i]
            dict[nums[i]] = i
        return []
