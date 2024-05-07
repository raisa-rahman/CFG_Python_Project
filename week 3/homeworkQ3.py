#Question 3
#Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
# quickly categorise books by the century and decade that they were written.
#Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Nineteenth Century,
# Seventies")

def categorize_year(year):
    if year < 1800 or year > 1950:
        return "Year out of range"

    century = (year - 1) // 100 + 1
    decade = ((year - 1) % 100) // 10 + 1

    century_str = {
        1: "Eighteenth",
        2: "Nineteenth",
        3: "Twentieth"
    }.get(century, "Twenty-first")

    decade_str = {
        1: "Tens",
        2: "Twenties",
        3: "Thirties",
        4: "Forties",
        5: "Fifties",
        6: "Sixties",
        7: "Seventies",
        8: "Eighties",
        9: "Nineties"
    }.get(decade, "Unknown decade")

    return f"{century_str} Century, {decade_str}"


year = int(input("Enter a year between 1800 and 1950: "))
print(categorize_year(year))

