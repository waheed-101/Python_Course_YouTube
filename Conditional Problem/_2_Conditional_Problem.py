# Prblem: 2 - Movie Ticket Pricing
# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
print()


user_age = int(input("Enter Your age: "))

print("\nSelect a Day: ")
print("1. Monday")
print("2. Tuesday") 
print("3. Wednesday")
print("4. Thursday")
print("5. Friday")
print("6. Saturday")
print("7. Sunday\n")
    
day_choice = int(input("Enter your day choice (1-7): "))

price = 12 if user_age >= 18 else 8

if day_choice == 3:
    price = price - 2


print(f"Your Ticket Price is ${price}\n")