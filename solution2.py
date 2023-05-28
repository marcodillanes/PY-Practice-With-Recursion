# Write code for algorithm 2 below

def natural_numbers(num, high_point):
    if num > high_point:
        return
    print(num)
    natural_numbers(num + 1, high_point)

natural_numbers(1, 10)
