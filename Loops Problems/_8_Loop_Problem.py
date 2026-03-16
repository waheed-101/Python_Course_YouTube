# Prime Number Checker
# Problem: Check if a number is prime.
# Prime Number: a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).


number = 29

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(f"Is {number} a Prime Number ???")
print(is_prime)

