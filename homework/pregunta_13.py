"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

nombre_archivo0 = "files/input/tbl0.tsv"
nombre_archivo2 = "files/input/tbl2.tsv"


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    try:
        df0 = pd.read_csv(nombre_archivo0, sep='\t', usecols=['c0', 'c1'])
        df2 = pd.read_csv(nombre_archivo2, sep='\t', usecols=['c0', 'c5b'])
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Uno o ambos archivos no se encontraron. Verifica la ruta: {e}") 
    
    df_merged = pd.merge(
        df0, 
        df2, 
        on='c0', 
        how='inner'
    )

    suma_c5b_por_c1 = df_merged.groupby('c1')['c5b'].sum().sort_index()
    
    return suma_c5b_por_c1