from json import load
class Json:
    #executed before init, creates the object manually
    def __new__(cls, file):
        print("object called")
        inst = object.__new__(cls)
        return inst

    #class variable
    how_many_times_used = 0

    def __init__(self, filename):
        self.__fn = open(filename, "rt")
        self.__data = load(self.__fn)
        Json.how_many_times_used += 1
    
    def __enter__(self):
        return self.__data
    
    def __exit__(self, tipe, value, traceback):
        self.__fn.close()

with Json("student.json") as data:
    print(data)
    print(data[0]['name'])

print(Json.how_many_times_used)