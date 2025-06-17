from typing import List

class Solution1:  # brute force.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j :
                    continue
                prod *= nums[j]
            output.append(prod)
        return output


class Solution2:  # suffix and prefix products.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0]*n
        suf = [0]*n
        pre[0] = 1
        suf[n-1] = 1

        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]
        for j in range(n-2,-1,-1):
            suf[j] = suf[j+1] * nums[j+1]

        output = [pre[i] * suf[i] for i in range(n)]

        return output
    
class Solution3:  # suffix and prefix products but space complexity is O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n

        cur = 1
        for i in range(n):
            output[i] *= cur
            cur *= nums[i]
        
        cur = 1
        for i in range(n-1,-1,-1):
            output[i] *= cur
            cur *= nums[i]

        return output


if __name__ == "__main__":
    nums = [1,2,3,4]  # [24,12,8,6]

    solu1 = Solution1()
    output1 = solu1.productExceptSelf(nums)

    solu2 = Solution2()
    output2 = solu2.productExceptSelf(nums)


    solu3 = Solution3()
    output3 = solu3.productExceptSelf(nums)

    print(output3)
