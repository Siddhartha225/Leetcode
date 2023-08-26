#Two Sum


# 2 Pass solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hashmap = {}
        output = []

        for i in range(len(nums)):
            Hashmap[nums[i]] = i

        for i in range(len(nums)):

            key = target - nums[i]

            if Hashmap.get(key, 'null') != 'null' and Hashmap.get(key, 'null') != i:
                output.extend([i, Hashmap.get(key)])
                break

        return output


# 1 Pass solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hashmap = {}
        output = []

        for i in range(len(nums)):

            key = target - nums[i]

            if key in Hashmap.keys():
                output.extend([Hashmap.get(key), i])
            else:
                Hashmap[nums[i]] = i

        return output

