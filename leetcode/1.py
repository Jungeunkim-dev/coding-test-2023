class Solution(object):
    def twoSum(self, nums, target):
        save = {}
        for i in range(len(nums)):
            if nums[i] in save and nums[i] * 2 == target:
                return [save.get(nums[i]), i]
            save[nums[i]] = i

        for num in nums:
            expect = target - num
            if expect != num and expect in save:
                return [save.get(num), save.get(target - num)]
