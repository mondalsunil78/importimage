print("\nExercise 1\n")
result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]
count = 0
for item in result:
    if item == "heads":
        count += 1
print("Heads count: ", count)
