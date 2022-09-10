# store information about favorite food of each person
fav_foods = {
    'chisomo': ['chicken', 'nkodowole'],
    'festas': ['rice', 'fish'],
    'james': ['beans', 'nsima']
}
# summarize the favorite food of each person
for name, foods in fav_foods.items():
    print("\n" + name.title() + "'s favorite foods is:")
    for food in foods:
        print("\t" + food)