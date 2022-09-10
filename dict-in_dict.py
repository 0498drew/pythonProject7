# store information of each user in  dict values of dict dict values
users = {
    'capchiz': {
        'first': 'chisomo',
        'last': 'banda',
        'location': 'lilongwe'
    },
    'cbox': {
        'first': 'malifu',
        'last': 'phiri',
        'location': 'blantrye',
    },
    'drew': {
        'first': 'andrew',
        'last': 'mwase',
        'location': 'mzuzu'
    },
}
# store each key in variable username
# dict associated with username goes to variable user.info
for username, user_info in users.items():
    print("\nUsername: " + username)
# access the inner dict
# variable info contains keys  'first', 'last', 'loc'
# use each key to generate full fomatted name and location of each user
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
# summarize users infomation in order
    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())