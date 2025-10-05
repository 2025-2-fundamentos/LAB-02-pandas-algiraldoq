"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

nombre_archivo = "files/input/tbl0.tsv" 

def pregunta_03():
    try:
        df0 = pd.read_csv(nombre_archivo, sep='\t')
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{nombre_archivo}' no se encontró. Verifica la ruta.") 
    
    conteo_registros = df0['c1'].value_counts().sort_index()
    
    return conteo_registros