# store info each pet in order
pets = {
    'dog': ['bull_gog', 'james'],
    'cat': ['pussy_cat', 'john'],
    'bird': ['parrot', 'andrew'],
}
# summarize the order
for name, pet in pets.items():
    print("\n" + name.title() + "'s info is this" )
    for pe in pet:
        print("\t" + pe)