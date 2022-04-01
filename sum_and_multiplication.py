#evaluate strings like "3*2+1" = 7 or "3+2*1" = 5
# only + and * are allowed


def evaluate(expression: str) -> int:
    s = expression.split("+")
    sum = 0
    for i in s:
        if "*" in i:
            s2 = i.split("*")
            p = 1
            for j in s2:
                p *= int(j)
            sum += p
        else:
            sum += int(i)
    return sum

s = evaluate("3*2+1")
print(s)
s = evaluate("3+2*1")
print(s)

s = evaluate("3*3*3 + 1*1*1*1*1*1")
print(s)

