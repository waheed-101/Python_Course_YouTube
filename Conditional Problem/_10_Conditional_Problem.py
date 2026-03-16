# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).



pet_species = "Dog"
age = 3

if pet_species.lower() == 'dog':
    if age < 2:
        recommended_food = f"For {pet_species} recommended food is: Puppy Food."
    else:
        recommended_food = f"For {pet_species} recommended food is: Adult Food."

elif pet_species.lower() == 'cat':
    if age > 5:
        recommended_food = f"For {pet_species} recommended food is: Senior Cat food."
    elif age <= 5:
        recommended_food = f"For {pet_species} recommended food is: Junior Cat food."
    
else:
    recommended_food = "Unknown Species"

print(recommended_food)