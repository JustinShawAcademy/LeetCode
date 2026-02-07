class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romandict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        total=0
        for i in range(len(s)):
            current = romandict[s[i]]
            #s[i] -> s value at index position
            #romandict[s[i]] ->integer value using the Letters

            #Check if there is a next character
            #Character after i is still less than the length of the string
            if i+1 < len(s):
                #Store the next value
                next_value = romandict[s[i+1]]
            else:
                next_value = 0

            if current < next_value:
                total = total - current
            else:
                total = total + current
            
        return total