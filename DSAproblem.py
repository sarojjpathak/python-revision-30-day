# PROBLEM 1 : Two Sum - Pair with given Sum
# Last Updated : 26 Jul, 2025
# Given an array arr[] of n integers and a target value, check if there exists a pair whose sum equals the target. This is a variation of the 2-Sum problem.

# Examples: 

# Input: arr[] = [0, -1, 2, -3, 1], target = -2
# Output: true
# Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.

# Input: arr[] = [1, -2, 1, 0, 5], target = 0
# Output: false
# Explanation: There is no pair with sum equals to given target.

arr = [0, -1, 2, -3, 1]
arr_2 = [1, -2, 1, 0, 5]
target = -2
target_2 = 0
result = False
for n in arr_2:
  for j in arr_2:
    if n == j:
      break
    elif n + j == target_2:
     result = True
     break;
print(result)
# here we can solve the above problem bye changing variables  in the above i have written code to solve for target 0 and with list arr_2





# PROBLEM : 2  Given an array prices[] of non-negative integers, representing the prices of the stocks on different days, find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

# Note: Stock must be bought before being sold.

# Examples:

# Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
# Output: 8
# Explanation: Buy for price 1 and sell for price 9. 

# Input: prices[] = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

# Input: prices[] = [1, 3, 6, 9, 11]
# Output: 10
# Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]
