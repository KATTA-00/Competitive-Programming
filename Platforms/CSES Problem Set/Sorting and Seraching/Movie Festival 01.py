n = int(input())
movies = []

for _ in range(n):
    a, b = map(int, input().strip().split())
    movies.append((a, b))

# Sort the movies by their ending times
movies.sort(key=lambda x: x[1])

max_movies = 0
end_time = 0

for movie in movies:
    if movie[0] >= end_time:
        max_movies += 1
        end_time = movie[1]

print(max_movies)
