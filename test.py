# variables
lists = ['education', 'hustle', 'job', 'farming']
# list each string
for list in lists:
# if hustle is in list
    if list == 'hustle':
# return true with a statment
        print(list + " is virtal")
# if true or false print the list
    else:
        print(list)

# test for equality and inequality
life = 'Education'
print("\nis education  a must?")
# resting using lowercase fuction
print(life.lower() == 'education')
if list != 'hustle':
    print("hustle always pays\n")

# checking numbers conditions
num = 19
if num  == 20:
    print("numbers are amazing")
elif num >= 4:
    print('this is jut some randon test\n')
print(num < 20)
print(num >= 25)
print(num == 20)
print(num != 17)

# checking  a value in a list or not
numbers = [3, 4, 5, 6]
print(3 in numbers)
print(8 in numbers)

# checking usin and keyword
num_1 = 33
num_2 = 23
print(num_1 >= 23 and num_2 >= 22)
print(num_1 <= 30 and num_2 <= 24)