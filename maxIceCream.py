def maxIceCreams(costs , coins):
    count = 0
    costs.sort()
    for i in costs:
        if coins >= i:
            coins -= i
            count += 1
    return count




costs = [2,21]
coins = 20
print(maxIceCreams(costs , coins))




# Example 1:
# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.


# Example 2:
# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.


# Example 3:
# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.