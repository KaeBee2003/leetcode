class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        a = set()
        n = len(nums)
        nums.sort()
        for j in range(1,n-1):
            i = 0
            k = n-1
            while i<j and j<k:
                s = nums[i] + nums[j] +nums[k]
                if s > 0:
                    k -= 1
                    
                elif s == 0:
                    three_sum = tuple(sorted([nums[i],nums[j],nums[k]]))
                    a.add(three_sum)
                    i += 1
                    k -= 1

                elif s < 0:
                    i += 1

                elif i>k:
                    break
                else:
                    pass

        return [list(x) for x in a] 