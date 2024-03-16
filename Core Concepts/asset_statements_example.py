def proc(a, b, c):
    assert all([a,b,c]), "Must all have values"
    assert a > 2, "The 'a' variable must be larger than 2"
    print(a, b, c)
proc(a=3, b=2, c=1)
#proc(3,0,2) Will cause assertion error
#proc(2,0,2) Will cause assertion error