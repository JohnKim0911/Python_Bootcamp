age = input("What is your current age? ")

left_years = 90 - int(age)
left_months = left_years * 12
left_weeks = left_years * 52
left_days = left_years * 365

print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")

# ----------------------- Result ------------------------ #
# What is your current age? 30
# You have 21900 days, 3120 weeks, and 720 months left.
