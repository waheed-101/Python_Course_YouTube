# Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso(a type of strong black coffee).



coffee_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = f"{coffee_size} coffee with an extra shot."

else:
    coffee = f"{coffee_size} coffee."

print(f"Order: {coffee}")
