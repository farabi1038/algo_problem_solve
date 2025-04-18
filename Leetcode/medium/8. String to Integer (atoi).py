class Solution:
    def myAtoi(self, s: str) -> int:
        actual_string = ''
        sign = 1
        start_point = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        n = len(s)

        # 1. Skip leading whitespaces
        while start_point < n and s[start_point] == ' ':
            start_point += 1

        # 2. Check for sign
        if start_point < n and (s[start_point] == '+' or s[start_point] == '-'):
            if s[start_point] == '-':
                sign = -1
            start_point += 1    

        # 3. Build the actual number string
        while start_point < n and s[start_point].isdigit():
            actual_string += s[start_point]
            start_point += 1

        # 4. Return 0 if no digits found
        if len(actual_string) == 0:
            return 0

        # 5. Convert to integer
        result = sign * int(actual_string)

        # 6. Clamp to 32-bit range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result