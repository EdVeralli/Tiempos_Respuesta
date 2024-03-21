# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:47:31 2024

@author: 20171078343
"""
import pandas as pd
import json
import sys


# Leer el archivo línea por línea y convertirlo en una lista de diccionarios
data = []
with open('tiempos_user_vars_metrics.json', 'r', encoding='latin1') as file:
    for line in file:
        data.append(eval(line))

# Convertir la lista de diccionarios en un DataFrame
df_user_vars_metrics = pd.DataFrame(data)


df_responsemsft = df_user_vars_metrics.loc[df_user_vars_metrics['name'] == 'responsemsft']

# corto hasta la palabra "answer"
df_responsemsft['response_time_substring'] = df_responsemsft['value'].apply(lambda x: x[:x.find('"answer"')-1] if x else None)

# corto hasta "response_time"
df_responsemsft['response_time_substring2'] = df_responsemsft['response_time_substring'].apply(lambda x: x[x.find('"response_time":'):].strip() if x else None)
# me quedo solo con el valor del tiempo
df_responsemsft['Tiempo_transcurrido'] = df_responsemsft['response_time_substring2'].apply(lambda x: x[x.find('":')+2:] if x else None)
# elimino las columnas auxiliares
df_responsemsft.drop(columns=['response_time_substring'], inplace=True)
df_responsemsft.drop(columns=['response_time_substring2'], inplace=True)



#muestro x StdOut los tiempos obtenido 
for index, row in df_responsemsft.iterrows():
    tiempo_respuesta = row['Tiempo_transcurrido']  ## ['response_time']
    print("\n",tiempo_respuesta)
    
#Grabo en un csv los tiempos, el session_id y el json roto de todo el Value
nombre_archivo = 'tiempo_transcurrido.csv'
df_responsemsft[['session_id','Tiempo_transcurrido','value']].to_csv(nombre_archivo,sep=';', index=False)


"""
De Aqui en adelante tengo los restos de codigo que use para tratar de leer el json "value" 
"""

# # Filtrar el DataFrame para las filas donde el valor de la columna "value" termina con una llave que cierra "}"
# filtered_df = df_user_vars_metrics[df_user_vars_metrics['value'].str.endswith('}')]

# # Verificar si hay filas que cumplan con la condición
# if not filtered_df.empty:
#     print("Se encontraron filas donde el valor de 'value' termina con una llave que cierra.")
# else:
#     print("No se encontraron filas donde el valor de 'value' termine con una llave que cierra.")



# Aplicar una función lambda para extraer el valor de "response_time" del JSON
# df_responsemsft['response_time'] = df_responsemsft['modified_value'].apply(lambda x: json.loads(x).get('response_time') if x.endswith('}') else None)


# for index, row in df_responsemsft.iterrows():
#     tiempo_respuesta = row['modified_value']['response_time']
#     print(tiempo_respuesta)
    

"""
import ast  # Módulo para convertir cadenas de texto en diccionarios

# Supongamos que 'columna_lista' es la columna que deseas convertir
df['columna_lista'] = df['columna_lista'].apply(ast.literal_eval)
"""


# df_user_vars_metrics['response_time_value'] = df_user_vars_metrics['value'].apply(lambda x: json.loads(x).get('response_time'))

# # Imprimir los valores de la columna 'response_time_value'
# print(df_user_vars_metrics['response_time_value'])


"""
df_user_vars_metrics = pd.read_csv(archivo)


df_con_json = pd.DataFrame()
"""



# df_user_vars_metrics['response_time_value'] = df_user_vars_metrics['value'].apply(lambda x: None if pd.isna(x) else json.loads(x).get('response_time', None))

# print(df_user_vars_metrics['response_time_value'])

# df_con_json = pd.DataFrame()
# for index, row in df_responsemsft.iterrows():
    
#     try:
#         # pepe = row['name']
#         # print(pepe+"####")
#         # if row['name'] != "userinputmsft":
#         #     print("entro")
#         #     pepe2 = row['value']
#         json_data = json.loads(row['modified_value'])
#         df_con_json = pd.concat([df_con_json, pd.DataFrame([row])])
#     except json.JSONDecodeError:
#         # Omitir la fila si no se puede cargar como JSON
#         print("error")
#         pass


# df_con_json['columna_nueva'] = df_con_json['vars_value'].apply(json.loads)

