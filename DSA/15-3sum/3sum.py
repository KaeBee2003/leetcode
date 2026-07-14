class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        a = []
        n = len(nums)
        nums.sort()
        for j in range(0,n-2):
            i = j+1
            k = n-1
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            
            while i<k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                    while k > 1 and nums[k] == nums[k+1]:
                        k -= 1
                    
                elif s == 0:
                    three_sum = [nums[i],nums[j],nums[k]]
                    a.append(three_sum)
                    i += 1
                    while i < n-1 and nums[i] == nums[i-1]:
                        i += 1
                    k -= 1
                    while k > 1 and nums[k] == nums[k+1]:
                        k -= 1

                elif s < 0:
                    i += 1
                    while i < n-1 and nums[i] == nums[i-1]:
                        i += 1

                else:
                    pass

        return a 