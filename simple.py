score = 33

if score < 6:
    price =  0
elif score < 20:
    price = 100
elif score < 30:
    price = 1000
else:
    price = 30
print("to view your results it cost MWK" + str(price) + ".")