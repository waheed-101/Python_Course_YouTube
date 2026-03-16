# Reverse a String
# Problem: Reverse a string using a loop.



input_str_1= "waheed"
reversed_str_1 = ""

for char in input_str_1:
    reversed_str_1 = char + reversed_str_1 # here char is before the reversed_str_1

print(reversed_str_1)





input_str_2 = "waheed"
reversed_str_2 = ""

for char in input_str_2:
    reversed_str_2 = reversed_str_2 + char # why it did not reverse because "char" is after the "reversed_str_2"

print(reversed_str_2)