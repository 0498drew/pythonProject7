# Store informatio about piza being ordered
food = {'breakfast': 'full',
        'mixtures': ['eggs', 'cornflakes', 'coffee', 'milk']
        }
# sumarize thr order
print("You ordered a " + food['breakfast'] + "-breakfast food" +
      " with the folowing mixtures:")
for mixture in food['mixtures']:
    print("\t" + mixture)