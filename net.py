# packing each dict into a list
# we loop through the list
# print each bird
bird_1 = {'colour': 'blue', 'speed': 5}
bird_2 = {'colour': 'green', 'speed': 7}
bird_3 = {'colour': 'yellow', 'speed': 8}
birds = [bird_1,  bird_2, bird_3]
for bird in birds:
    print(bird)
# make an empy list for storing birds
birds = []
# make 12 birds
for bird_num in range(12):
    new_bird = {'colour': 'red', 'speed': 6, 'points': 7}
    birds.append(new_bird)
# show the first 4 birds
for bird in birds[:4]:
    print(bird)
print("...")
# show how many birds have been created
print("Total birds: " + str(len(birds)))