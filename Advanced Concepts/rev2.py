#coins in pence
coins = [1, 2, 5, 10, 20, 50, 100]

#amount target
two_pounds = 200

#the global counter
total_combinations = 0

#find and print combinations
def find_combinations(target, coins, combination, start_index):
    global total_combinations
    if target == 0: #valid combination
        print(combination)
        total_combinations += 1 
        return
    if target < 0: #not valid as its gone under
        return
    
    #each coin starting from the current index
    for i in range(start_index, len(coins)):
        coin = coins[i]
        #reduce target by coin value and add coin to the combination
        find_combinations(target - coin, coins, combination + [coin], i)

find_combinations(two_pounds, coins, [], 0)

#the total number of combinations found
print("Total number of combinations:", total_combinations)