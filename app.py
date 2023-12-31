from PIL import Image
import numpy as np

from main import leer_imagen, guardar_matriz, cargar_matriz, crear_imagen, leer_archivo, convertir_imagen_a_archivo, copiar_matriz, convertir_matriz_a_imagen

# CON numpy

def modificar_matriz(matriz):
    matriz_modificada = matriz.copy()
    matriz_modificada[:, :, 0] = 0
    matriz_modificada[:, :, 1] = 2
    # matriz_modificada[:, :, 2] = 255
    return matriz_modificada

# def modificar_matriz_reverse(matriz):
#     matriz_modificada = matriz.copy()
#     return matriz_modificada[::-1, ::-1, :]

def modificar_matriz_reverse(matriz):
    matriz_modificada = matriz.copy()
    for i in range(matriz_modificada.shape[0]):
        for j in range(matriz_modificada.shape[1]):
            matriz_modificada[i, j, :] = matriz[matriz.shape[0] - i - 1, matriz.shape[1] - j - 1, :]
    return matriz_modificada

# con MATRIZ

def convertir_escala_de_grises(m):
    matriz = copiar_matriz(m)
    for fila in matriz :
        for pixel in fila :
            pixel[2] = pixel[1] 
            pixel [0] = pixel[1]
    return matriz

def convertir_negativo(m):
    matriz = copiar_matriz(m)
    for fila in matriz :
        for pixel in fila :
            pixel[0]= 255-pixel[0]
            pixel[1]= 255-pixel[1]
            pixel[2]= 255-pixel[2]
    return matriz

def promedios_colores(listadecolres):
    suma= sum(listadecolres)
    #Se dividira en 3, ya que tenemos 3  trabajmos con  R, G , B
    Promediofinal= int(suma/3)
    # Se retorna Promediofinal ya una vez obtenido
    return Promediofinal

def convertir_blanco_negro(m):
    matriz= copiar_matriz(m)
    for fila in matriz:
        for pixel in fila:
            pp = promedios_colores(pixel)
            if  pp > 180:
                pixel[0]= 255
                pixel[1]= 255
                pixel[2]= 255
            elif pp <= 180:
                pixel[0]= 0
                pixel[1]= 0
                pixel[2]= 0
    return matriz



# Leer la imagen y convertirla en matriz RGB
# matriz_rgb = leer_imagen('img.jpg')

# # Guardar la matriz como archivo
# guardar_matriz(matriz_rgb, 'matriz_rgb.npy')

# # Cargar la matriz desde el archivo
# matriz_cargada = cargar_matriz('matriz_rgb.npy')

# # Manipular la matriz
# matriz_modificada = modificar_matriz_blanco_negro(matriz_cargada)

# # Crear una nueva imagen a partir de la matriz modificada
# imagen_modificada = crear_imagen(matriz_modificada)

# # Guardar la imagen modificada
# imagen_modificada.save('imagen_modificada.jpg')
# imagen_modificada.show() 

name_img = 'img.jpg'
array_img = 'array_img.txt'
salida_img = 'img_modificada.png'

convertir_imagen_a_archivo(name_img , array_img)
matriz_img = leer_archivo(array_img)

new_matriz = convertir_blanco_negro(matriz_img)

convertir_matriz_a_imagen(new_matriz, salida_img, True)

