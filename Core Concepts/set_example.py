names: list[str] = ["Alice", "Bob", "alice", "bob", "Charlie", "charlie"]

lowercase_names: map = map(str.lower, names)

unique_names: set = set(lowercase_names)

print(list(unique_names))