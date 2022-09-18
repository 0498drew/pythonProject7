def make_iceream(size, *flavours):
    """"print the list of flavours that are being orded"""
    print("\nmake me " + str(size) + " corn icecream with the following flavours")
    for flavour in flavours:
        print("- " + flavour)
make_iceream(2,'strawberry')
make_iceream(4,  'chocolate', 'cheese', 'orange')

def make_iceream(flav, typ, USD, **info):
    """"make a dict contaning everthing we now about the order"""
    customer = {}
    customer['flavour'] = flav
    customer['type'] = typ
    customer['price'] = USD
    for key, value in info.items():
        customer[key] = value
    return customer
customer_order = make_iceream('chocolate', 'corn', 5,
                              size='medium')
print(customer_order)
