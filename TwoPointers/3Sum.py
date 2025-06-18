from typing import List
from collections import defaultdict

class Solution1:  # Hash Map.    Time complexity : O(n^2)   Space complexity : O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res


# 2 pointers.    Time complexity : O(n^2)   Space complexity : O(k)(for the output list)
class Solution2:  
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,a in enumerate(nums):
            if a > 0 :
                break
            
            if i > 0 and a == nums[i-1]:
                continue

            l, r  = i+1, len(nums) - 1

            while l < r :
                target = a + nums[l] + nums[r]

                if target < 0 :
                    l += 1
                elif target > 0 :
                    r -= 1
                
                else :
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r :
                        l += 1
        return res
    

if __name__ == "__main__":

    numbers = [-1,0,1,2,-1,-4]

    sol1 = Solution1()
    print(sol1.threeSumSum(numbers))

    sol2 = Solution2()
    print(sol2.threeSumSum(numbers))