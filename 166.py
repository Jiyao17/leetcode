
# Notes
# 1. Basic steps of integer division: get quotient and remainder,
# set numerator=remainder (*10 for the next division), 
# always keep denominator unchanged, repeat integer division until
# (quotient repeats or remainder == 0).
#
# 2. After the first time integer division, the remainder is always 
# smaller than the denominator.
#
# 3. We can know if the result of a division contains a fraction part
# from the first integer divisoin: if there is a remainder, 
# then there is a fraction, else there is not.
#
# 4. Sufficient and Required condition of loop in the fraction part:
# the quotient repeats.
#
# Marginal notes
# 5. No need to detect recurring quotiont before decimal part.
# 
# 6. We can always do an integer division before the loop
# to simplify the logic.


class Solution:
    def __init__(self):
        # numerator, denominator -> quotient, remainder, step
        self.divisions: 'dict[(int, int), (int, int, int)]' = {}

    def _divide(self, numerator, denominator):
        """
        division with remainder
        """
        quotient = numerator // denominator
        remainder = numerator - denominator*quotient

        return (quotient, remainder)


    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        result = ""
        if numerator == 0:
            return "0"
        elif denominator == 0:
            return ""
        elif numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1
        elif numerator < 0 or denominator < 0:
            result += "-"
            numerator = abs(numerator)
            denominator = abs(denominator)

        q, r = self._divide(numerator, denominator)
        result += str(q)
        if r == 0:
            return result
        else:
            result += "."
            numerator = r*10

        while numerator != 0:

            if (numerator, denominator) not in self.divisions:
                q, r = self._divide(numerator, denominator)
                self.divisions[(numerator, denominator)] = (q, r, len(result))

                result += str(q)
                numerator = r*10
            else: # found recurring fraction
                q, r, idx = self.divisions[(numerator, denominator)]
                result = result[:idx] + "(" + result[idx:] + ")"
                break

        return result


# print(Solution().fractionToDecimal(13, 20))