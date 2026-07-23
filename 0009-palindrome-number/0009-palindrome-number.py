class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_str = str(x)
        if input_str == input_str[::-1]:
            return True
        else:
            return False