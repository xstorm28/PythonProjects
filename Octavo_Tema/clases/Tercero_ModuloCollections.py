from collections import namedtuple

Persona = namedtuple('Persona',['nombre','altura','peso'])

ariel = Persona('Ariel', 1.90,'79')


print(ariel.altura)
