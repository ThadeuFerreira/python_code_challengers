# A photography set consists of NN cells in a row, numbered from 11 to NN in order, and can be represented by a string CC of length NN. Each cell ii is one of the following types (indicated by C_iC 
# i
# ​
#  , the iith character of CC):
# If C_iC 
# i
# ​
#   = “P”, it is allowed to contain a photographer
# If C_iC 
# i
# ​
#   = “A”, it is allowed to contain an actor
# If C_iC 
# i
# ​
#   = “B”, it is allowed to contain a backdrop
# If C_iC 
# i
# ​
#   = “.”, it must be left empty
# A photograph consists of a photographer, an actor, and a backdrop, such that each of them is placed in a valid cell, and such that the actor is between the photographer and the backdrop. Such a photograph is considered artistic if the distance between the photographer and the actor is between XX and YY cells (inclusive), and the distance between the actor and the backdrop is also between XX and YY cells (inclusive). The distance between cells ii and jj is |i - j|∣i−j∣ (the absolute value of the difference between their indices).
# Determine the number of different artistic photographs which could potentially be taken at the set. Two photographs are considered different if they involve a different photographer cell, actor cell, and/or backdrop cell.

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
    stack = []
    count = 0
    for i in range(len(C)):
        if C[i] == 'P':
            stack.append(i)
        elif C[i] == 'A':
            if len(stack) >= 2:
                if abs(stack[-1] - stack[-2]) >= X and abs(stack[-1] - i) >= X:
                    count += 1
                stack.pop()
        elif C[i] == 'B':
            if len(stack) >= 1:
                if abs(stack[-1] - i) >= X:
                    count += 1
                stack.pop()
    return count


N = 5
C = 'APABA.'
X = 1
Y = 2

print(getArtisticPhotographCount(N, C, X, Y))

N = 5
C = 'APABA'
X = 2
Y = 3

print(getArtisticPhotographCount(N, C, X, Y))


N = 8
C = '.PBAAP.B'
X = 1
Y = 3

print(getArtisticPhotographCount(N, C, X, Y))