# Make an empty list for storing birds
birds = []

# Make 30 blue birds
for bird_number in range(0, 30):
    new_bird = {'color': 'blue', 'points': 5,
                'speed': 'fast'}
    birds.append(new_bird)
for bird in birds[0:3]:
    if bird['color'] == 'blue':
        bird['color'] == 'yellow'
        bird['speed'] == 'slow'
        bird['points'] == 10
    elif bird['color'] == 'yellow':
        bird['color'] == 'red'
        bird['speed'] == 'slow'
        bird['points'] == 15
# show the fist 5 birds
for bird in birds[0:5]:
    print(bird)
print("...")