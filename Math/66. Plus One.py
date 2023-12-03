class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        flag, i = 1, 0
        n = len(digits) - 1

        while flag:
            if i < len(digits):
                if digits[n-i] == 9:
                    digits[n-i] = 0
                else:
                    digits[n-i] += 1
                    flag = 0 ## stop the while loop
            else:
                digits.insert(0, 1)
                flag = 0
            i += 1
        
        return digits