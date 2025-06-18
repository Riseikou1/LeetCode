class Solution1:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for ch in s :
            if ch.isalnum():
                new_s += ch.lower()
        
        return new_s == new_s[::-1]
    

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s) - 1
        while l < r :
            while l < r and not s[l].isalnum() :
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    

if __name__ == "__main__":
    string = "Was it a car or a cat I saw?"

    sol1 = Solution1()
    print(sol1.isPalindrome(string))

    sol2 = Solution2()
    print(sol2.isPalindrome(string))