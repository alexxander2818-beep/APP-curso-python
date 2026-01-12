#Conceptos Básicos Palabra x Palabra

from
 
"""#Q es: Es como decir "de dónde" vas a traer algo. Es pa decirle a Python "oye, tráeme esta cosa DE este lugar"

#Ejemplo cotidiano:"""

from app import create_app

"""#Es como decir: "de la carpeta 'app', tráeme la función 'create_app'"

#Sería como decir: "de la tienda tráeme pan" → from tienda import pan"""

import

"""#Q es: Es "traer" o "importar". Es como traer una caja de herramientas q alguien más ya hizo pa q tu no tengas q hacerlas d nuevo.
#Ejemplos:"""

import flask  """tráeme TODO lo de flask"""
from flask import Flask  """# de flask, solo tráeme Flask"""
"""#Es como:

#import = tráeme toda la caja de herramientas
#from X import Y = de esa caja, solo tráeme el martillo"""

def

"""Q es: Significa "definir" o "define". Es pa crear tus propias funciones (como recetas q puedes usar después)."""


def saludar():
    print("hola parcero")
```

"Es como escribir una receta:"
```
def hacer_arepas():
    - agarra maíz
    - muélelo
    - haz bolitas
    - cocínalas

"Después solo dices hacer_arepas() y Python hace todo eso"