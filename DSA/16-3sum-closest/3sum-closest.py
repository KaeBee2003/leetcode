import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        abs_delta = math.inf
        best = None
        
        for j in range(0,n-2):
            i = j+1
            k = n-1
            while i < k:

                total = nums[i] + nums[j] + nums[k]
                delta = total - target

                if abs(delta) < abs_delta:
                    abs_delta = abs(delta)
                    best = total

                if delta > 0:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1

                elif delta < 0:
                    i += 1
                    while i < k and nums[i] == nums[i-1]:
                        i += 1

                else:
                    return total


        return best