age = int(input())

if age > 60:
    movie = "Breakfast at Tiffany's"
elif age > 40:
    movie = "Pulp Fiction"
elif age > 25:
    movie = "Matrix"
elif age > 16:
    movie = "Trainspotting"
else:
    movie = "Lion King"

print(movie)
