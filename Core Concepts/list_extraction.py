the_people: list[str] = ["Johnny", "Bret", "Jessica", "Andy", "Jeff"]

first, second, *_, last = the_people

print("First Person: {}".format(first))
print("Second Person: {}".format(second))
print("Last Person: {}".format(last))

'''
First Person: Johnny
Second Person: Bret
Last Person: Jeff
'''