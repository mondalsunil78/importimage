print("\nExercise 4\n")

for i in range(5):
    print(f"You ran {i+1} miles")
    # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4:# 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")
