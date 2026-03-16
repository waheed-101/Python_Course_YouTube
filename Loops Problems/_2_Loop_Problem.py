# Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = 100
sum_of_even_number = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_of_even_number += i

print(f"\nwhere n = {n}\n")
print(f"Sum of Even Number = {sum_of_even_number}\n")





# Sum of Odd Numbers
# Problem: Calculate the sum of odd numbers up to a given number n.

n = 100
sum_of_odd_number = 0

for i in range(1, n+1):
    if i % 2 != 0:
        sum_of_odd_number += i

print(f"Sum of Odd Number = {sum_of_odd_number}\n")

print(f"Total Sum (Even + Odd) = {sum_of_even_number + sum_of_odd_number}\n")





# Count Even Numbers
# Problem: Calculate the count of even numbers up to a given number n.

n = 100
even_number_count = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even_number_count += 1

print(f"Even Number Count = {even_number_count}\n")





# Count Odd Numbers
# Problem: Calculate the count of odd numbers up to a given number n.

n = 100
odd_number_count = 0

for i in range(1, n+1):
    if i % 2 != 0:
        odd_number_count += 1

print(f"Odd Number Count = {odd_number_count}\n")

print(f"Sum of Count number (Even + Odd) = {even_number_count + odd_number_count}\n")