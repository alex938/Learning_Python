import functools
def fmtprice(amount, sign):
    return f"{sign}{amount}"

print(fmtprice(20, "£"))

fmtUS = functools.partial(fmtprice, sign="$")
print(fmtUS(20))