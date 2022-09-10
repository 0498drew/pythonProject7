# make a list in a dict
rivers = {'amazon': 'brazil',
          'zambezi': 'zamabia',
          'kinshasha': 'rwanda',
          'shire': ' malawi',
          'rweya': 'malawi'
          }
# show a massage with keys and values
for name, river in rivers.items():
    print(name + " runs through " + river.title())
# show values
for river in rivers.keys():
    print(river)