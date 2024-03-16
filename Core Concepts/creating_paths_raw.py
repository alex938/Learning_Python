from pathlib import Path

dir = "tmp"

pathname = fr"c:/{dir}/file.txt"
print(pathname)

pathname = r"c:/{}/file.txt".format(dir)
print(pathname)

pathname = Path("c:/{}/file.txt".format(dir))
print(pathname)

#with open(pathname, 'w') as file:
#    file.write('hello')