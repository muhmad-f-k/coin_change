# Class for Assignment 1
class Change:
    # Info Got from Assignment
    # I got sum = 1 040 528 NOK-
    # I get coins = {1, 5, 10, 20}-
    # Need to find - outputs the minimum number of coins that sum up to s-

    # This method takes sum as a int and coins as a list of int, this done just to make it esay to see what the method takes in and what expected the output wich is int
    def find_min_change(sum: int, coins=list[int]) -> int:
        # default value [sum +1 ] and initialize array from 0 to sum + 1 | # Max value will be sum + 1 -  1 040 528 +1
        dp = [sum + 1] * (sum + 1)
        dp[0] = 0  # Using tabulaion then start value from 0 at index 0
        # Loop the sum from 1 to sum + 1 so since is tabulation its reversed
        for i in range(1, sum + 1):
            for j in coins:  # loop throw every coin in the coin list
                if i - j >= 0:  # this if statment just to check that dont have negativ value
                    # As long if statment is true will keep searching
                    dp[i] = min(dp[i], 1 + dp[i - j])
        return dp[sum]  # return min. DP wich this answer looking for.
