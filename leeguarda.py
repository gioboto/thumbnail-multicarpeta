#!/usr/bin/env python3

import os
from PIL import Image
import json

#ruta = "/home/usuario/Downloads/images.jpeg"

def obtiene_atributos_imagen(ruta):
    """Funciòn para leer los atributos de una imagen

    Args:
        ruta (string): ruta de las imagenes

    Returns:
        dictionary: atributos de iamgen dentro de un diccionario
    """    
    try:
        with Image.open(ruta) as img:
            ancho, alto = img.size
            modo = img.mode
            im = img.im
            format = img.format
            formatd = img.format_description
            #info = img.info
            #palette = img.palette
            
            #print({'nombre': os.path.basename(ruta), 'ancho': ancho, 'alto': alto, 'modo': modo, 'im' : im, 'format' : format, 'formatd': formatd, 'info': info, 'palette' : palette})
            #return{'ruta': ruta, 'nombre': os.path.basename(ruta), 'ancho': ancho, 'alto': alto, 'modo': modo, 'im' : im, 'format' : format, 'formatd': formatd, 'info': info, 'palette' : palette}
            return{'ruta': ruta, 'nombre': os.path.basename(ruta), 'ancho': ancho, 'alto': alto, 'modo': modo, 'im' : im, 'format' : format, 'formatd': formatd}
    except Exception as ex:
        return {'nombre': os.path.basename(ruta), 'error': str(ex)}
    

def guarda_json(datos, nombre_archivo):
    """Guarda de datos de imagen en un archvio json

    Args:
        datos (_type_): datos para el json
        nombre_archivo (_type_): Nombre de archivo json
    """    
    try:
        with open(nombre_archivo,'w') as archivo:
            json.dump(datos, archivo, indent=2)
        print(f"Datos guardados en {nombre_archivo}")
    except Exception as e:
        print(f"Error en guardar jcon: {e}")
"""
ELPATHO = "/home/usuario/python/thumbnail-multicarpeta/raiz/images.jpeg" 
ELPATHD = "/home/usuario/python/thumbnail-multicarpeta/destino/" 
NOMBRE_ARCHIVO = "MINIimages.jpeg"
"""

def cambiaimagen(elpathorigen, elpathdestino, nombre_archivo):
    """Cambia el tamaño de la imagen para generar las miniaturas

    Args:
        elpathorigen (string): path y nombre de la imagen de origen
        elpathdestino (string): path destino de la imagen
        nombre_archivo (string): nombre de la imagen destino para la miniatura

    Returns:
        _type_: _description_
    """    
    try:
        imagen = Image.open(elpathorigen)
        ELSIZE = (175, 128)
        imagen.thumbnail(ELSIZE)
        pathdnombre = elpathdestino + "/" + nombre_archivo
        print(pathdnombre)
        imagen.save(pathdnombre)
        #imagen.show()
    except Exception as ex:
        return print({'nombre': os.path.basename(elpathorigen), 'error': str(ex)})


#cb = cambiaimagen(ELPATHO, ELPATHD)