list10 = [1,2,3,4,5,6]
first, *unused, last = list10
print(first)
print(unused)
print(last)

string1 = "Python is amazing"
*string2, = string1
print(string2)