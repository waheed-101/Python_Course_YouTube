# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)



password = "aa11njkl@p"

if len(password) < 6:
    password_strength = "Weak"

elif len(password) <= 10:
    password_strength = "Medium"

elif len(password) > 10:
    password_strength = "Strong"

print(f"Password Strength: {password_strength}\n"
      f"Password Character: {len(password)}")
