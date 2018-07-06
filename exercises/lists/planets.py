planet_list = ["Mercury", "Mars"]

planet_list.append('Jupiter')
planet_list.append('Saturn')

planet_list.extend(['Earth', 'Venus'])

planet_list.append('Pluto')
rocky_planets = planet_list[1:5]
del planet_list[6]
print(planet_list)
print(rocky_planets)

