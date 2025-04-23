# Python code to generate all possible birth numbers (rodná čísla) for people born after the year 2000
# that have distinct digits.

# The structure of a rodné číslo (birth number) after 2000 is: 'YYMMDD/XXXX'
# YY - last two digits of the year (for people born after 2000, it's between 00 and 99)
# MM - month (01 to 12)
# DD - day (01 to 31 depending on the month)
# XXXX - a 4-digit number where each digit should be unique

from itertools import permutations

# Helper function to check if a date is valid
def is_valid_date(year, month, day):
    # List of days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Check for leap year
        days_in_month[1] = 29  # February has 29 days in a leap year
    return 1 <= month <= 12 and 1 <= day <= days_in_month[month - 1]

# List to store valid birth numbers
valid_birth_numbers = []

# Generate all possible years, months, and days for people born after 2000
for year in range(2000, 2100):
    for month in range(1, 13):
        for day in range(1, 32):
            if is_valid_date(year, month, day):
                # Get the last two digits of the year
                year_suffix = str(year)[2:]
                # Generate all unique permutations of 4 digits
                for perm in permutations("0123456789", 4):
                    # Create the rodné číslo in the form of 'YYMMDD/XXXX'
                    rodne_cislo = f"{year_suffix.zfill(2)}{str(month).zfill(2)}{str(day).zfill(2)}/" + "".join(perm)
                    # Add it to the list
                    valid_birth_numbers.append(rodne_cislo)

# Display the number of valid rodná čísla generated
len(valid_birth_numbers), valid_birth_numbers[:10]  # Show the first 10 as an example
