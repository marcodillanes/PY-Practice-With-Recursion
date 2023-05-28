# Write code for algorithm 4 below

def power(a, b):
    return a ** b

print(power(3, 3))

#below is the recursion way

def powers(a, b):
    if b < 1:
        return a
    return a * powers(a, b-1)

for i in range(10):
    print(powers(i, i))