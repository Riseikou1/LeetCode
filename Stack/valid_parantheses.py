class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {")" : "(", "]":"[","}":"{"}
        stack = []

        for ch in s :
            if ch in mapp :
                if stack and stack[-1] == mapp[ch]:
                    stack.pop()
                else :
                    return False
            else :
                stack.append(ch)

        return True if not stack else False


if __name__ == "__main__":

    input = "([])({[[]]})"

    sol1 = Solution()
    print(sol1.isValid(input))