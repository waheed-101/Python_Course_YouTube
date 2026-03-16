# Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).


weather = "Rainy"

if weather == 'Sunny':
    activity = "Go for a walk"

elif weather == 'Rainy':
    activity = "Read a book"

elif weather == 'snowy':
    activity = "Build a snowman"

print(f"Weather: {weather}\n"
      f"Activity: {activity}")
