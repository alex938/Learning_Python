results = [True, 0, True, False]
if False in results:
    print("False found")

results = [True, True, True]

if all(results): print("All true")

results = [0, 0, 1]

if any(results): print("True value found")