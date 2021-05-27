age = input("What is your current age?: ")

days = int(age) * 365
weeks = int(age) * 52
months = int(age) * 12

days_left = 90 * 365 - days
weeks_left = 90 * 52 - weeks
months_left = 90 * 12 - months

print(f"you have {days} days, {weeks} weeks, and {months} months.")
print(f"and you have {days_left} days, {weeks_left} weeks, and {months_left} months left till you're 90. Use it wisely")