# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.


input_str = "teeteracdacd"
print(input_str)


for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print(f"First Non-Repeated Character is: {char}")
        break

