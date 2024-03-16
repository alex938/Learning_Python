import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))

repr_string = repr(today)
print(repr_string)
print(type(repr_string))

#repr_string = "datetime.datetime(2024, 3, 16, 12, 34, 56, 789012)"

#manually parsing the string to extract the date and time components
components = repr_string.strip("datetime.datetime()").split(", ")
year, month, day, hour, minute, second, microsecond = map(int, components)

#reconstructing the datetime object
reconstructed_today = datetime.datetime(year, month, day, hour, minute, second, microsecond)

print(reconstructed_today)
print(type(reconstructed_today))