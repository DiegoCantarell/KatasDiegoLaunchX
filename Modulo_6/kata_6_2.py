
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

user_planet = input('Ingresar nombre del planeta (Comenzando con letra mayuscula)')
planet_index = planets.index(user_planet)
print('Planetas cercanos a:' + user_planet)
print(planets[0:planet_index])
print('Planetas lejanos a ' + user_planet)
print(planets[planet_index + 1:])