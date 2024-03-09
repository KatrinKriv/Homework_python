from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    birthdays_by_weekday = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        delta_days = (birthday_this_year - today).days

        if delta_days < 0:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days
        weekday = birthday_this_year.strftime("%A")

        birthdays_by_weekday[weekday].append(name)

    for weekday, names in birthdays_by_weekday.items():
        if weekday == "Saturday" or weekday == "Sunday":
            monday = today + timedelta(days=(7 - today.weekday()))
            birthdays_by_weekday["Monday"].extend(names)
        else:
            print(f"{weekday}: {', '.join(names)}")

    if birthdays_by_weekday["Monday"]:
        print(f"Monday: {', '.join(birthdays_by_weekday['Monday'])}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1987, 5, 30)},
]
get_birthdays_per_week(users)
