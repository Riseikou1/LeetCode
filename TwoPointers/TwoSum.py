from typing import List

class Solution1:  # hash map.       Time complexity - O(n) , Space complexity - O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        temuujin = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in temuujin :
                return [temuujin[complement]+1, i+1]
            temuujin[numbers[i]] = i
        
        return []

class Solution2:  # binary search.   Time complexity - O(nlogn) , Space complexity - O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        return 

    

class Solution3:  # two pointers.    Time complexity - O(n) , Space complexity - O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0,len(numbers)-1

        while l < r :
            cur = numbers[l] + numbers[r]

            if cur > target :
                r -= 1     
            elif cur < target :
                l += 1
            else :
                return [l + 1, r + 1]

        return []
    
if __name__ == "__main__":

    numbers = [1,2,3,4]
    target = 7

    sol1 = Solution1()
    print(sol1.twoSum(numbers,target))

    sol2 = Solution2()
    print(sol2.twoSum(numbers,target))

    sol3 = Solution3()
    print(sol3.twoSum(numbers,target))