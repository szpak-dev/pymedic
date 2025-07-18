cities: dict[str, int] = {'Walencja': 791413, 'Marsylia': 861635, 'Lyon': 2000000, 'Turyn': 3000000, 'Porto': 4000000, 'Helsinki': 261635, 'Malmo': 961635}
total_population = 0
for city, population in cities.items():
    if population > 1000000:
        print(city)
        total_population += population

print(f'Toatl population cities >1M: {total_population}')