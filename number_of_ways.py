#A box contains a number of chocolates that can only be removed 1 at a time or 3 at a time.
#Hoe many ways can the box be emptied?

# for n = 7
# 1, 1, 1, 1, 1, 1, 1
# 1, 1, 1, 1, 3
# 1,1,1,3,1
# 1,1,3,1,1
# 1,3,1,1,1
# 3,1,1,1,1
# 1,3,3
# 3,1,3
# 3,3,1

#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def numberOfWaysMemory(n,memory):
    # Write your code here
    if n in memory:
        return memory[n]
    if n < 0:
        memory[n] = 0
        return 0
    if n == 0:
        memory[n] = 1
        return 1
    memory[n] = numberOfWaysMemory(n-1,memory) + numberOfWaysMemory(n-3, memory)
    return memory[n]

def numberOfWays(n):
    # Write your code here
    memory = {}
    return numberOfWaysMemory(n,memory)

print(numberOfWays(7))
print(numberOfWays(3))
print(numberOfWays(2))