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
target = -2
result = False
for n in arr:
  for j in arr:
    if n == j:
      break
    elif n + j == target:
     result = True
     break;
print(result)
