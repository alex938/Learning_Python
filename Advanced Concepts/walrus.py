primary = "Roger"
backup = "Dave"

if user := (primary or backup):
    print(f"{user} authenticated")
else:
    print("User not found")
