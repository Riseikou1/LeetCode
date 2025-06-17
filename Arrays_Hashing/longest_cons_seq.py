from typing import List
from collections import defaultdict

class Solution1:  # brute force kinda shit.
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for num in nums :
            streak, cur = 0 , num
            while cur in store :
                streak += 1
                cur += 1
            res = max(res,streak)
        return res
    

class Solution2:  # sorted shit. O(n*log n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        longest = 1
        cur_streak = 1
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:  # skipping duplicates
                continue
            elif nums[i] == nums[i-1] + 1 :
                cur_streak += 1
                longest = max(longest,cur_streak)
            else :
                cur_streak = 1
        return longest
    

class Solution3:  # hash set.  O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums :
            if num-1 not in num_set :
                length = 1

                while num + length in num_set :
                    length += 1
                
                longest = max(longest,length)
        return longest
    

class Solution4:  # hash map.  O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        temuujin = defaultdict(int)
        res = 0
        for num in nums :
            if not temuujin[num]:
                temuujin[num] = temuujin[num-1] + temuujin[num+1] + 1
                temuujin[num - temuujin[num-1]] = temuujin[num]
                temuujin[num + temuujin[num+1]] = temuujin[num]
                res = max(res,temuujin[num])
        return res
    
    
if __name__ == "__main__":
    nums = [100,4,200,1,3,2] # output - 4

    solu1 = Solution1()
    output1 = solu1.longestConsecutive(nums)

    solu2 = Solution2()
    output2 = solu2.longestConsecutive(nums)

    solu3 = Solution3()
    output3 = solu3.longestConsecutive(nums)

    solu4 = Solution4()
    output4 = solu4.longestConsecutive(nums)

    print(output2)
    print(output3)
    print(output4)
