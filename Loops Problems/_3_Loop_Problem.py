# Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.


n = 3

for i in range(1, 11):
    if i == 5:           # now this will remove the fifth iteration
        continue
    print(f"{n} x {i} = {n * i}")   # 3 x 1 = 3

print()







# Print the whole 78 table

n = 78

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")