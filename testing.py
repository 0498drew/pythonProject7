# list of items
vegs = ['spinach', 'tomato', 'onion', 'cooking oil']
# looping thru list
for veg in vegs:
# assigning a  statment  that can handle a list loop
    if veg == 'tomato':
        print("run out of tomato")
# print the list
    else:
        print("adding " + veg + ".")
print("\nfinished cooking vegs\n")
# printing all relevant items
if 'spinach' in vegs:
    print("add  spinach")
if 'tomato' in vegs:
    print("add pilled tomato")
if 'onion' in vegs:
    print("pour in you onion")
if 'cooking oil' in vegs:
    print("add cooking oil")

print("\nFinished cooking vegs")