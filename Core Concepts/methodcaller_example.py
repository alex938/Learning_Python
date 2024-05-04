from operator import methodcaller

the_people: list[str] = ["Johnny", "Bret", "Jessica", "Andy", "Jeff"]

starts_with_a_j: methodcaller = methodcaller("startswith", "J")
filtered_list: filter = filter(starts_with_a_j, the_people)
print(list(filtered_list))

count_e_in_names: methodcaller = methodcaller("count", "e")
count_of_e: map = map(count_e_in_names, the_people)
print(list(count_of_e))