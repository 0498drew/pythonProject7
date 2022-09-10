cities = {
    'mzuzu': {
        'country': 'malawi',
        'population': '1 million',
        'facts': 'green city'
    },
    'harare': {
        'country': 'zimbabwe',
        'population': '2 million',
        'facts': 'city that dont sleep'
    },
    'capetown': {
        'country': 'south africa',
        'population': '3 million',
        'facts': 'cape of good hope',
    },
}
for cityname, city_info in cities.items():
    print("\nCityname: " + cityname)
    country = city_info['country']
    population = city_info['population']
    about = city_info['facts']
    print("\tCountry: " + country)
    print("\tPopulation: " + population)
    print("\tAbout: " + about)

