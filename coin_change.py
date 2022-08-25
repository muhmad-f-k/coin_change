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
        # create max value - Add 1 since it start at index 0
        #dp = [int for x in range(len(sum)+1)]
        dp[0] = 0  # Using tabulaion then start value from 0 at index 0
        # Loop the sum from 1 to sum + 1 so since is tabulation its reversed
        for i in range(1, sum + 1):
            for j in coins:  # loop throw every coin in the coin list
                if i - j >= 0:  # this if statment just to check that dont have negativ value
                    # So here it check will searching if dp[i -j] +1 is less then min(dp[i]) if it true then it will update if not true will keep old value.
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[sum]  # return min. DP wich this answer looking for.


print(Change.find_min_change(1040528, [1, 5, 10, 20]))
