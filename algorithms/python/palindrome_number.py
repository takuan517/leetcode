class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = str(x)
        hoge = i[::-1]
        print(i)
        print(hoge)
        if i == hoge:
            return True
        else:
            return False
