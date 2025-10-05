"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

nombre_archivo = "files/input/tbl0.tsv"

def concatenar_ordenado(serie):
    valores_str_ordenados = serie.astype(int).sort_values().astype(str)
    return ":".join(valores_str_ordenados)

def pregunta_10():
    try:
        df0 = pd.read_csv(nombre_archivo, sep='\t')
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{nombre_archivo}' no se encontró. Verifica la ruta.") 
    
    resultado_serie = df0.groupby('c1')['c2'].agg(concatenar_ordenado).sort_index()
    
    resultado_df = resultado_serie.to_frame()
    
    resultado_df.index.name = '_c1'
    
    return resultado_df