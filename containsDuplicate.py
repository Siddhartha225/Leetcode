#Find Duplicates

#Sort Method

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(len(nums) - 1):
            print(nums[i], nums[i + 1])
            if nums[i] == nums[i + 1]:
                return True
            else:
                pass

        return False

#HashSet Method

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)

        return False