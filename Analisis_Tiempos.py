# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:47:31 2024

@author: 20171078343
"""


import pandas as pd
import json
import sys
archivo = 'tiempos_user_vars_metrics.csv'

df_user_vars_metrics = pd.read_csv(archivo)


df_con_json = pd.DataFrame()


for index, row in df_user_vars_metrics.iterrows():
    try:

        json_data = json.loads(row['vars_value'])
        
        df_con_json = pd.concat([df_con_json, pd.DataFrame([row])])
    except json.JSONDecodeError:
        # Omitir la fila si no se puede cargar como JSON
        print("error")
        pass

df_con_json['columna_nueva'] = df_con_json['vars_value'].apply(json.loads)

for index, row in df_con_json.iterrows():
    tiempo_respuesta = row['columna_nueva']['response_time']
    print(tiempo_respuesta)
    
