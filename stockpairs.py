def stockPairs(stocksProfit, target):
    # Write your code here
    sortedProfits = sorted(stocksProfit)
    
    left = 0
    right = len(sortedProfits) - 1
    pairs = []
    while left < right:
        currentSum = sortedProfits[left] + sortedProfits[right]
        if currentSum == target:
            pair = sorted([sortedProfits[left], sortedProfits[right]])
            pairs.append(pair)
            left += 1
            right -= 1
            continue
        elif currentSum < target:
            left += 1
        else:
            right -= 1
    print(pairs)
    return len(pairs)

stocksProfit = [1,3,46,1,3,9]
target = 47

print(stockPairs(stocksProfit, target))

stocksProfit = [6,6,3,9,3,5,1]
target = 12


print(stockPairs(stocksProfit, target))