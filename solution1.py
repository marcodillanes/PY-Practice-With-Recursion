# Write code for algorithm 1 below

def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n-1)

print_num(10)