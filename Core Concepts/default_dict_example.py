from collections import defaultdict
import time

my_def_dict = defaultdict(lambda : ("Epoch time is: {:.0f}".format(time.time())))

my_def_dict["first"]
print(my_def_dict)

time.sleep(2)
my_def_dict["second"]
print(my_def_dict)

for key, value in my_def_dict.items():
    print(f"Key: '{key}', Value: {value}")