def leap_year(year):
    try:
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Year should be in numbers")


# Example
leap_year(2000)  # prints "2000 is a leap year."
