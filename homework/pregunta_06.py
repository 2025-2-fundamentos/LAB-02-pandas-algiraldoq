"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

nombre_archivo = "files/input/tbl1.tsv"

def pregunta_06():
    try:
        df1 = pd.read_csv(nombre_archivo, sep='\t')
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{nombre_archivo}' no se encontró. Verifica la ruta.") 
    
    valores_unicos = df1['c4'].unique()
    
    valores_mayusculas = pd.Series(valores_unicos).str.upper()
    
    resultado = valores_mayusculas.sort_values().tolist()
    
    return resultado