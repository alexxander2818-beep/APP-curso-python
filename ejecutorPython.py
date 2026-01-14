import flask 
import bcrypt
from flask import request 
from rutas.cliente.routes_cliente import  mensage_login
import numpy as np
from rutas.servicios.comprar import comprar_arros, trabajar_mañana
from rutas.hola.practca2 import vaca,










a = np.array([3, 2, 1]) 
b = np.array([4, 5, 6])
suma_vectores = a + b
print(suma_vectores)# Salida: [7 7 7]
 

r = 20
p = 15
resta_numeros = r - p
print(resta_numeros)


c = np.array([[8, 17], [6, 7]])
x = np.array([[12, 4], [7, 8]])
suma_valores_cx = c + x
print(suma_valores_cx)  #resultado a igual a [20, 21], [13, 15]

d = np.array([[6, 3, 9, 5, 7], [5, 9, 14, 123, 56]])
f = np.array([[5, 12], [256, 3, 9]])
suma_valores_df = d + f
print(suma_valores_df) #resultado a igual a [11, 15, 9, 5, 7] [261, 12, 23, 123, 56]