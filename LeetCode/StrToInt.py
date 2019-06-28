# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this character,
#  takes an optional initial plus or minus sign followed by as many numerical digits
# as possible, and interprets them as a numerical value.


def myAtoi(self, str: str) -> int:
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0