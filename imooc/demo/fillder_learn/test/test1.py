class Solution(object):
    def firstMissingPositive(self, nums):

        n = len(nums)
        nums.sort()
        if n == 0: return 1
        if n == 1 and nums[0] != 1: return 1
        if nums[-1] < 1: return 1

        k = 0 # 第一个大于零的元素索引
        for i in range(n):
            j = n-1 - i
            if nums[i] > 0:
                k = i
                break
            if nums[j] < 0:
                k = j+1
                break
        print("k:", k)
        array = [i for i in range(1, n-k+1)]
        for i in range(k, n):
            if nums[i] != array[i-k]:
                return i-k+1
        return len(array)+1

nums = [1,2,0]
solution = Solution()
print(solution.firstMissingPositive(nums))