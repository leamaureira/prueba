#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import re


# 

# ##### Sospecha
# - 1-Citodiagnóstico corriente, exfoliativa (Papanicolaou y similares) (por cada órgano)
# - 2-Visita domiciliaria de rescate
# - 3-Consulta o control médico integral en atención primaria
# - 4-Consulta o control por enfermera, matrona o nutricionista
# 

# In[36]:


prestaciones = [

"1-Citodiagnóstico corriente, exfoliativa (Papanicolaou y similares) (por cada órgano)"
    ]


# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",  
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[37]:


prestaciones=[
    "2-Visita domiciliaria de rescate"]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df1 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[38]:


prestaciones=[
    "3-Consulta o control médico integral en atención primaria"
]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué médico lo atendió",
    "¿Cuál otro médico?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df2 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[39]:


prestaciones=["4-Consulta o control por enfermera, matrona, o nutricionista"]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué especialista lo atendió",
    "¿Cuál otro especialista?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df3 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[42]:


# Agregar una columna con el número de la prestación
df['Numero Prestación'] = df['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df1['Numero Prestación'] = df1['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df2['Numero Prestación'] = df2['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df3['Numero Prestación'] = df3['Nombre Prestación'].str.extract(r'(\d+)').astype(int)



# Combinar los DataFrames
df_combined = pd.concat([df,df1,df2,df3], ignore_index=True)

# Ordenar el DataFrame por la columna 'Numero Prestación' y 'Orden Pregunta'
df_combined_sorted = df_combined.sort_values(by=['Numero Prestación', 'Orden Pregunta']).reset_index(drop=True)


# In[44]:


df = df_combined_sorted


# In[46]:


# Definir las variables de cada pregunta
variables = [
    "indica_",
    "fecha_indica_",
    "realiza_",
    "fecha_realiza_",
    "lugar_",
    "tipo_espe_",
    "otro_espe_",
    "lugar_exm_",
    "fecha_envio_",
    "fecha_devol_",
    "inform_resul_",
    "fecha_resul_",
    "fecha_prox_",
    "reagenda_",
    "n_reagenda_",
    "fecha_prim_reag_",
    "razon_prim_reag_",
    "fecha_sec_reag_",
    "razon_sec_reag_",
    "fecha_ter_reag_",
    "razon_ter_reag_",
    "fecha_cuar_reag_",
    "razon_cuar_reag_",
    "fecha_quin_reag_",
    "razon_quin_reag_",
    "tipo_med_",
    "otro_med_"

]

# Actualizar las variables por cada pregunta

df['Variable'] = df['Preguntas'].apply(lambda x: variables[[
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué especialista lo atendió",
    "¿Cuál otro especialista?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    "Indique qué médico lo atendió",
    "¿Cuál otro médico?"
    
].index(x)])


# In[48]:


prestaciones=[
    "1-Citodiagnóstico corriente, exfoliativa (Papanicolaou y similares) (por cada órgano)",
    "2-Visita domiciliaria de rescate",
    "3-Consulta o control médico integral en atención primaria",
    "4-Consulta o control por enfermera, matrona, o nutricionista"
    ]


# In[49]:


# Define una lista de números únicos por cada prestación
prestacion_numbers = list(range(1, len(prestaciones) + 1))

# Crea un diccionario para mapear prestaciones y asignar el número que corresponda
prestacion_to_number = {prestacion: number for prestacion, number in zip(prestaciones, prestacion_numbers)}

# Agrega la nueva columna "Numero prestación"
df['Numero prestacion'] = df['Nombre Prestación'].map(prestacion_to_number)

# Reordena la posición de las variables
df = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas', 'Variable']]


# In[52]:


# Crea una nueva columna "Nombre Variable Final" según el nombre de la variable, el número de prestación y el tipo de capacidad
df['Nombre Variable Final'] = df['Variable'] + 'cacu_' + df['Numero prestacion'].astype(str) + "_sosp"


# In[53]:


df


# ##### Comienza formato RedCap
# 
# - 1. Dejar solo las columnas que necesito: Nombre prestación, Pregunta y Nombre Variable Final
# - 2. Cambiar nombre al formato de redcap de las columnas que tengo
# - 3. Agregar columna "Section Header": título de cada prestación
# - 4. Agregar columna "Form Name" : nombre del formulario en redcap
# - 5. Agregar columna "Field Type" : Tipo de dato

# In[54]:


#Dejar solo las columnas que necesito
df_cacu = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas','Nombre Variable Final']]


# In[55]:


#Cambiar nombre de la variable

nombres_nuevos = {'Nombre Variable Final':'Variable / Field Name',
                 'Preguntas' : 'Field Label'}
df_cacu.rename(columns=nombres_nuevos, inplace=True)


# In[56]:


# Crear columna Section 
df_cacu['Section Header'] = ''

# Asignar S.H. según el nombre de la prestación 
df_cacu.loc[df_cacu.groupby('Nombre Prestación').cumcount() == 0, 'Section Header'] = df['Nombre Prestación']


# In[57]:


# Crear columna del nombre del formulario 

df_cacu['Form Name'] = "formulario_sospecha_cacu"
df_cacu["Field Note"] = ""


# In[58]:


# Crear la columna 'Field Type' con valores por defecto 'text'
df_cacu['Field Type'] = 'text'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("indica_","realiza_","lugar_","lugar_exm_",
                                                          "inform_resul_","reagenda_","razon_prim_reag_",
                                                          "razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_",
                                                          "razon_quin_reag_""tipo_med_","n_reagenda_","tipo_med_",
                                                          "tipo_espe_"


))
df_cacu.loc[condic, 'Field Type'] = 'dropdown'


# In[59]:


# Crear la columna 'Choices, Calculations, OR Slider Labels'
df_cacu['Choices, Calculations, OR Slider Labels'] = ''

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('indica_', 'realiza_', 'inform_resul_','reagenda_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Si | 2, No'


# In[60]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'


# In[20]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_exm_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Lab de la Red SSMSO  | 2,  Lab externo'


# In[61]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("razon_prim_reag_","razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_","razon_quin_reag_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se presentó | 2, Reagendamiento por temas administrativos (Ej: paro de funcionarios) | 3, Reagendamiento por rechazo del paciente | 4, Rechazo de interconsulta por Contralor | 5, Paciente no termina su tratamiento | 6, Paciente fallecido | 7, Paciente perdido (Ej: continuó su atención clínica en el extrasistema) | 8, Información no disponible'


# In[62]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("n_reagenda_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5'


# In[63]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_espe_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Enfermera | 2, Matrona | 3, Kinesióloga| 4, Nutricionista | 5, Otra (Especificar)'


# In[64]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_med_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Médico de familia | 4, Otro'


# In[65]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("fecha_"))
df_cacu.loc[condic, 'Text Validation Type OR Show Slider Number'] = 'date_dmy'


# In[66]:


# Define the function to apply the correct branching logic
def generate_branching_logic(row):
    variable_name = row['Variable / Field Name']
    try:
        num_prest = int(row['Numero prestacion'])
    except (ValueError, TypeError):
        return ""
    if variable_name == f"fecha_indica_cacu_{num_prest}_sosp":
        return f"[indica_cacu_{num_prest}_sosp]=1"
    
    elif variable_name == f"realiza_cacu_{num_prest}_sosp":
        return f"[indica_cacu_{num_prest}_sosp]=1"
    
    elif variable_name == f"fecha_realiza_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]=1"
    
    elif variable_name == f"lugar_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]=1"
    
    elif variable_name == f"lugar_exm_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1"
    
    elif variable_name == f"fecha_envio_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1"
    
    elif variable_name == f"fecha_devol_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1"
    
    elif variable_name == f"inform_resul_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1"
    
    elif variable_name == f"fecha_resul_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1 and [inform_resul_cacu_{num_prest}_sosp]=1"
    
    elif variable_name == f"fecha_prox_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1"
    
    elif variable_name == f"reagenda_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]=1 or [realiza_cacu_{num_prest}_sosp]=2"
    
    elif variable_name == f"n_reagenda_cacu_{num_prest}_sosp":
        return f"[reagenda_cacu_{num_prest}_sosp]=1"
    
    elif variable_name == f"fecha_prim_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=1"
    
    elif variable_name == f"razon_prim_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=1"
    
    elif variable_name == f"fecha_sec_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=2"
    
    elif variable_name == f"razon_sec_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=2"
    
    elif variable_name == f"fecha_ter_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=3"
    
    elif variable_name == f"razon_ter_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=3"
    
    elif variable_name == f"fecha_cuar_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=4"
    
    elif variable_name == f"razon_cuar_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=4"
    
    elif variable_name == f"fecha_quin_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=5"
    
    elif variable_name == f"razon_quin_reag_cacu_{num_prest}_sosp":
        return f"[n_reagenda_cacu_{num_prest}_sosp]>=5"
    
    elif variable_name == f"tipo_med_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1"

    elif variable_name == f"otro_med_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1 and [tipo_med_cacu_{num_prest}_sosp]=4"
    
    elif variable_name == f"tipo_espe_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1"
    
    elif variable_name == f"otro_espe_cacu_{num_prest}_sosp":
        return f"[realiza_cacu_{num_prest}_sosp]= 1 and [tipo_espe_cacu_{num_prest}_sosp]=5"
    
        return ""
    
    # Apply the function to create the new column
df_cacu['Branching Logic (Show field only if...)'] = df_cacu.apply(generate_branching_logic, axis=1)


# In[67]:


# Define the new columns with empty values
new_columns = {
    'Text Validation Min': '',
    'Text Validation Max': '',
    'Identifier?': '',
    'Required Field?': '',
    'Custom Alignment': '',
    'Question Number (surveys only)': '',
    'Matrix Group Name': '',
    'Matrix Ranking?': '',
    'Field Annotation': ''
}

# Add these new columns to the existing dataframe with default empty values
for column, value in new_columns.items():
    df_cacu[column] = value


# In[68]:


# Definir el orden de las variables en el df

orden_deseado = ['Variable / Field Name', 'Form Name', 'Section Header', 'Field Type',
       'Field Label', 'Choices, Calculations, OR Slider Labels', 'Field Note',
       'Text Validation Type OR Show Slider Number', 'Text Validation Min',
       'Text Validation Max', 'Identifier?',
       'Branching Logic (Show field only if...)', 'Required Field?',
       'Custom Alignment', 'Question Number (surveys only)',
       'Matrix Group Name', 'Matrix Ranking?', 'Field Annotation']

#Reordenar
df_cacu = df_cacu[orden_deseado]


# In[70]:


df_cacu.to_excel("Output/CaCu_sosp.xlsx")


# In[71]:


df_cacu.to_csv("Output/instrument.csv", index=False)


# ### Diagnóstico
# - 5-Citodiagnóstico corriente, exfoliativa (Papanicolau y similares)(por cada órgano)
# - 6-Colposcopía
# - 7-Estudio histopatológico con técnicas histoquimicas especiales
# - 8-Estudio histopatológico corriente de biopsia diferida (por cada órgano)
# - 9-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)
# - 10-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado
# - 11-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)
# - 12-Estudios moleculares específicos
# 

# In[ ]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import re


# ###### Exámenes

# In[ ]:


prestaciones = [
    "5-Citodiagnóstico corriente, exfoliativa (Papanicolaou y similares) (por cada órgano)"
    ]


# Agregar preguntas
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = ["6-Colposcopía"]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]

# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df1 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
    "7-Estudio histopatológico con técnicas histoquimicas especiales",
    "8-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
    "9-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
    "10-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
    "11-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)"
]
# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen"
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df2 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:



prestaciones = [
    "12-Estudios moleculares específicos"]

# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df3 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# ##### Confirmación CaCu

# - 13-Conización y/o amputación del cuello uterino, diagnóstica y/o terapéutica c/s biopsia"
# - 14-Estudio histopatológico con técnicas histoquimicas especiales
# - 15-Estudio histopatológico corriente de biopsia diferida
# - 16-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)
# - 17Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado
# - 18-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)'
# - 19-Estudios moleculares específicos
# - 20-Anticuerpos virales, determ H.I.V
# - 21-Consulta o control por enfermera, matrona, o nutricionista
# - 22-Consulta integral de especialidades en Medicina interna y Subespecialidades, Oftalmología, Neurología, Oncología
# 

# In[ ]:


prestaciones = ["13-Conización y/o amputación del cuello uterino, diagnóstica y/o terapéutica c/s biopsia"]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]

# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df4 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
    "14-Estudio histopatológico con técnicas histoquimicas especiales",
    "15-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
    "16-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
    "17-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
    "18-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)"
]
# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen"
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df5 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
    "19-Estudios moleculares específicos"]

# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df6 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
    "20-Anticuerpos virales, determ H.I.V"
    ]


# Agregar preguntas
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df7 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=["21-Consulta o control por enfermera, matrona, o nutricionista"]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué especialista lo atendió",
    "¿Cuál otro especialista?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df8 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "22-Consulta integral de especialidades en medicina interna y subespecialidades (hospital alta complejidad)"]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df9 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


# Agregar una columna con el número de la prestación
df['Numero Prestación'] = df['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df1['Numero Prestación'] = df1['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df2['Numero Prestación'] = df2['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df3['Numero Prestación'] = df3['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df4['Numero Prestación'] = df4['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df5['Numero Prestación'] = df5['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df6['Numero Prestación'] = df6['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df7['Numero Prestación'] = df7['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df8['Numero Prestación'] = df8['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df9['Numero Prestación'] = df9['Nombre Prestación'].str.extract(r'(\d+)').astype(int)

# Combinar los DataFrames
df_combined = pd.concat([df,df1,df2,df3,df4,df5,df6,df7,df8,df9], ignore_index=True)

# Ordenar el DataFrame por la columna 'Numero Prestación' y 'Orden Pregunta'
df_combined_sorted = df_combined.sort_values(by=['Numero Prestación', 'Orden Pregunta']).reset_index(drop=True)


# In[ ]:


df = df_combined_sorted


# In[ ]:


prestaciones=[
  
"5-Citodiagnóstico corriente, exfoliativa (Papanicolaou y similares) (por cada órgano)",
"6-Colposcopía",
"7-Estudio histopatológico con técnicas histoquimicas especiales",
"8-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
"9-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"10-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
"11-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
"12-Estudios moleculares específicos",
"13-Conización y/o amputación del cuello uterino, diagnóstica y/o terapéutica c/s biopsia",
"14-Estudio histopatológico con técnicas histoquimicas especiales",
"15-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
"16-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"17-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
"18-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
"19-Estudios moleculares específicos",
"20-Anticuerpos virales, determ H.I.V",
"21-Consulta o control por enfermera, matrona, o nutricionista",
"22-Consulta integral de especialidades en medicina interna y subespecialidades (hospital alta complejidad)"
]


# In[ ]:


# Definir las variables de cada pregunta
variables = [
    "indica_",
    "fecha_indica_",
    "realiza_",
    "fecha_realiza_",
    "lugar_",
    "lugar_exm_",
    "lugar_inf_exm_",
    "fecha_envio_",
    "fecha_devol_",
    "inform_resul_",
    "inform_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_prox_",
    "fecha_prox_",
    "reagenda_",
    "n_reagenda_",
    "fecha_prim_reag_",
    "razon_prim_reag_",
    "fecha_sec_reag_",
    "razon_sec_reag_",
    "fecha_ter_reag_",
    "razon_ter_reag_",
    "fecha_cuar_reag_",
    "razon_cuar_reag_",
    "fecha_quin_reag_",
    "razon_quin_reag_",
    "tipo_med_",
    "otro_med_",
    "tipo_espe_med_",
    "otro_esp_med_",
    "tipo_espe_",
    "otro_espe_",
    "toma_biop_",
    "no_biop_",
    "otro_no_biop_",
    "tipo_biop_",
    "tipo_molec_",
    "otro_molec_",
    "otro_estudio"]


# Actualizar las variables por cada pregunta

df['Variable'] = df['Preguntas'].apply(lambda x: variables[[
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "¿Dónde se realizó el informe del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "¿Se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    "Indique qué médico lo atendió",
    "¿Cuál otro médico?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Indique qué especialista lo atendió",
    "¿Cuál otro especialista?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Qué tipo de estudio de biopsia se le indicó?",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio"].index(x)])



# In[ ]:


# Define una lista de números únicos por cada prestación
prestacion_numbers = list(range(5, len(prestaciones) + 22))

# Crea un diccionario para mapear prestaciones y asignar el número que corresponda
prestacion_to_number = {prestacion: number for prestacion, number in zip(prestaciones, prestacion_numbers)}

# Agrega la nueva columna "Numero prestación"
df['Numero prestacion'] = df['Nombre Prestación'].map(prestacion_to_number)

# Reordena la posición de las variables
df = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas', 'Variable']]


# In[ ]:


# Crea una nueva columna "Nombre Variable Final" según el nombre de la variable, el número de prestación y el tipo de capacidad
df['Nombre Variable Final'] = df['Variable'] + 'cacu_' + df['Numero prestacion'].astype(str) + "_diag"


# In[ ]:


df


# In[ ]:





# ##### Comienza formato RedCap
# 
# - 1. Dejar solo las columnas que necesito: Nombre prestación, Pregunta y Nombre Variable Final
# - 2. Cambiar nombre al formato de redcap de las columnas que tengo
# - 3. Agregar columna "Section Header": título de cada prestación
# - 4. Agregar columna "Form Name" : nombre del formulario en redcap
# - 5. Agregar columna "Field Type" : Tipo de dato

# In[ ]:


#Dejar solo las columnas que necesito
df_cacu = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas','Nombre Variable Final']]


# In[ ]:


#Cambiar nombre de la variable

nombres_nuevos = {'Nombre Variable Final':'Variable / Field Name',
                 'Preguntas' : 'Field Label'}
df_cacu.rename(columns=nombres_nuevos, inplace=True)


# In[ ]:


# Crear columna Section 
df_cacu['Section Header'] = ''

# Asignar S.H. según el nombre de la prestación 
df_cacu.loc[df_cacu.groupby('Nombre Prestación').cumcount() == 0, 'Section Header'] = df['Nombre Prestación']


# In[ ]:


# Crear columna con el nombre del formulario 

df_cacu['Form Name'] = "formulario_diagnostico_cacu"
df_cacu["Field Note"] = ""


# In[ ]:


# Crear la columna 'Field Type' con valores por defecto 'text'
df_cacu['Field Type'] = 'text'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("indica_","realiza_","lugar_","lugar_exm_",
                                                          "inform_resul_","reagenda_","razon_prim_reag_",
                                                          "razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_",
                                                          "razon_quin_reag_","tipo_med_","tipo_espe_med_","tipo_espe_",
                                                          "n_reagenda_","toma_biop_","no_biop","tipo_biop_","tipo_molec_",
                                                          "reagenda_biop_","lugar_inf_exm_"
                                                       

))

df_cacu.loc[condic, 'Field Type'] = 'dropdown'

# Crear la columna 'Choices, Calculations, OR Slider Labels'
df_cacu['Choices, Calculations, OR Slider Labels'] = ''

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('indica_','realiza_','inform_resul_','reagenda_','toma_biop_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Si | 2, No'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_exm_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Lab de la Red SSMSO  | 2,  Lab externo'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("razon_prim_reag_","razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_","razon_quin_reag_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se presentó | 2, Reagendamiento por temas administrativos (Ej: paro de funcionarios) | 3, Reagendamiento por rechazo del paciente | 4, Rechazo de interconsulta por Contralor | 5, Paciente no termina su tratamiento | 6, Paciente fallecido | 7, Paciente perdido (Ej: continuó su atención clínica en el extrasistema) | 8, Información no disponible'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("n_reagenda_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_med_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Médico de familia | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_espe_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Enfermera | 2, Matrona | 3, Kinesióloga| 4, Nutricionista | 5, Otra (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_biop_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Estudio histopatológico con técnicas histoquimicas especiales" | 2, Estudio histopatológico corriente de biopsia diferida(por cada órgano)" | 3, Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)" | 4, Estudio histopatológico con tinción corriente de biopsia diferida con estudio seriado (mínimo 10 muestras) de un órgano o parte de él (no incluye estudio con técnica habitual de otros órganos incluidos en la muestra) | 5, Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)'
                                 
# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("no_biop_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se encontró lesión | 2, Imposibilidad de tomar muestra | 3, Falta de insumos o RRHH | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("lugar_inf_exm_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_molec_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, P16 | 2, Estudios de receptores hormonales  | 3, PDL-1 | 4, Otro (Especificar)'



# Actualizar la columna ''Text Validation Type OR Show Slider Number' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("fecha_"))
df_cacu.loc[condic, 'Text Validation Type OR Show Slider Number'] = 'date_dmy'


# In[ ]:


# Define the function to apply the correct branching logic
def generate_branching_logic(row):
    variable_name = row['Variable / Field Name']
    try:
        num_prest = int(row['Numero prestacion'])
    except (ValueError, TypeError):
        return ""
    if variable_name == f"fecha_indica_cacu_{num_prest}_diag":
        return f"[indica_cacu_{num_prest}_diag]=1"
    
    elif variable_name == f"realiza_cacu_{num_prest}_diag":
        return f"[indica_cacu_{num_prest}_diag]=1"
    
    elif variable_name == f"fecha_realiza_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]=1"
    
    elif variable_name == f"lugar_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]=1"
    
    elif variable_name == f"lugar_exm_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"
    
    elif variable_name == f"fecha_envio_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"
    
    elif variable_name == f"fecha_devol_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"
    
    elif variable_name == f"inform_resul_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"
    
    elif variable_name == f"fecha_resul_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1 and [inform_resul_cacu_{num_prest}_diag]=1"
    
    elif variable_name == f"fecha_prox_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"
    
    elif variable_name == f"reagenda_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]=1 or [realiza_cacu_{num_prest}_diag]=2"
    
    elif variable_name == f"n_reagenda_cacu_{num_prest}_diag":
        return f"[reagenda_cacu_{num_prest}_diag]=1"
    
    elif variable_name == f"fecha_prim_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=1"
    
    elif variable_name == f"razon_prim_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=1"
    
    elif variable_name == f"fecha_sec_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=2"
    
    elif variable_name == f"razon_sec_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=2"
    
    elif variable_name == f"fecha_ter_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=3"
    
    elif variable_name == f"razon_ter_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=3"
    
    elif variable_name == f"fecha_cuar_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=4"
    
    elif variable_name == f"razon_cuar_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=4"
    
    elif variable_name == f"fecha_quin_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=5"
    
    elif variable_name == f"razon_quin_reag_cacu_{num_prest}_diag":
        return f"[n_reagenda_cacu_{num_prest}_diag]>=5"
    
    elif variable_name == f"tipo_espe_med_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"

    elif variable_name == f"otro_esp_med_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1 and [tipo_espe_med_cacu_{num_prest}_diag]=7"
    
    elif variable_name == f"tipo_med_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"

    elif variable_name == f"otro_med_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1 and [tipo_med_cacu_{num_prest}_diag]=4"
                                                          
    elif variable_name == f"tipo_espe_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"

    elif variable_name == f"otro_espe_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1 and [tipo_prof_cacu_{num_prest}_diag]=5"
    
    elif variable_name == f"lugar_inf_exm_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"
    
    elif variable_name == f"toma_biop_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"
    
    elif variable_name == f"no_biop_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1 and [toma_biop_cacu_{num_prest}_diag]=2"
    
    elif variable_name == f"otro_no_biop_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1 and [no_biop_cacu_{num_prest}_diag]=4"    
    
    elif variable_name == f"tipo_biop_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1 and [toma_biop_cacu_{num_prest}_diag]=1"
    
    elif variable_name == f"tipo_molec_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1"
    
    elif variable_name == f"otro_molec_cacu_{num_prest}_diag":
        return f"[realiza_cacu_{num_prest}_diag]= 1 and [tipo_molec_cacu_{num_prest}_diag]=4"

    
        return ""
    
    # Apply the function to create the new column
df_cacu['Branching Logic (Show field only if...)'] = df_cacu.apply(generate_branching_logic, axis=1)


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_7_diag", "realiza_cacu_8_diag", "realiza_cacu_9_diag",
    "realiza_cacu_10_diag","realiza_cacu_11_diag","realiza_cacu_12_diag"
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_6_diag]=1 and [toma_biop_cacu_6_diag]=1"


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_14_diag", "realiza_cacu_15_diag", "realiza_cacu_16_diag", 
    "realiza_cacu_17_diag", "realiza_cacu_18_diag", "realiza_cacu_19_diag",  
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_13_diag]=1 and [toma_biop_cacu_13_diag]=1"


# In[ ]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
nombres_completos = ["tipo_espe_med_cacu_22_diag"]


# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Cirujano General| 4, Internista | 5, Cirujano mama | 6, Ginecólogo Oncólogo | 7, Otro (Especificar)'


# In[ ]:


import pandas as pd

# Crear un diccionario con los valores de la nueva fila
nueva_fila = {
    'Variable / Field Name': 'resul_biop_cacu_diag',
    'Form Name': 'formulario_diagnostico',
    'Section Header': 'Confirmación CaCu',
    'Field Type': 'dropdown',
    'Field Label': '¿Cuál fue el resultado de la biopsia?',
    'Choices, Calculations, OR Slider Labels': '1, Cáncer de Cuello Uterino | 2, Neoplasia',
    'Field Note': '',
    'Text Validation Type OR Show Slider Number': '',
    'Text Validation Min': '',
    'Text Validation Max': '',
    'Identifier?': '',
    'Branching Logic (Show field only if...)': '[toma_biop_cacu_6_diag]=1 or [toma_biop_cacu_13_diag]=1',
    'Required Field?': '',
    'Custom Alignment': '',
    'Question Number (surveys only)': '',
    'Matrix Group Name': '',
    'Matrix Ranking?': '',
    'Field Annotation': ''
}

# Dividir el DataFrame en dos partes: antes y después del índice 120
df_parte_1 = df_cacu.iloc[:120, :]
df_parte_2 = df_cacu.iloc[120:, :]

# Convertir la nueva fila en un DataFrame
nueva_fila_df = pd.DataFrame([nueva_fila])

# Concatenar las partes con la nueva fila en medio
df_cacu = pd.concat([df_parte_1, nueva_fila_df, df_parte_2]).reset_index(drop=True)


# In[ ]:


# Define the new columns with empty values
new_columns = {
    'Text Validation Min': '',
    'Text Validation Max': '',
    'Identifier?': '',
    'Required Field?': '',
    'Custom Alignment': '',
    'Question Number (surveys only)': '',
    'Matrix Group Name': '',
    'Matrix Ranking?': '',
    'Field Annotation': ''
}

# Add these new columns to the existing dataframe with default empty values
for column, value in new_columns.items():
    df_cacu[column] = value

# Definir el orden de las variables en el df

orden_deseado = ['Variable / Field Name', 'Form Name', 'Section Header', 'Field Type',
       'Field Label', 'Choices, Calculations, OR Slider Labels', 'Field Note',
       'Text Validation Type OR Show Slider Number', 'Text Validation Min',
       'Text Validation Max', 'Identifier?',
       'Branching Logic (Show field only if...)', 'Required Field?',
       'Custom Alignment', 'Question Number (surveys only)',
       'Matrix Group Name', 'Matrix Ranking?', 'Field Annotation']

#Reordenar
df_cacu = df_cacu[orden_deseado]


# In[ ]:


df_cacu.to_excel("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/CaCu_diag.xlsx")

df_cacu.to_csv("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv", index=False)


# In[ ]:


import zipfile
import os

# Ruta del archivo que quieres comprimir
archivo_csv = "C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv"

# Ruta donde se guardará el archivo comprimido
ruta_salida_zip = r"C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/Cacu_diag.zip"

# Crear un archivo ZIP y agregar el archivo CSV
with zipfile.ZipFile(ruta_salida_zip, 'w') as archivo_zip:
    archivo_zip.write(archivo_csv, os.path.basename(archivo_csv))

print(f"Archivo comprimido guardado en: {ruta_salida_zip}")


# ### Etapificación
# ###### Cacu Invasor
# - '23-Orina completa',
# - '24-Urocultivo recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye ',recolector pediátrico)
# - '25-Glucosa',
# - '26-Creatinina',
# - '27-Protrombina tiempo de o consumo de (incluye INR Relación Internacional Normalizada)',
# - '28-Hemograma (incluye recuentos de leucocitos eritrocitos y plaquetas hemoglobina hematocrito fórmula leucocitaria ',características de los elementos figurados y velocidad de eritrosedimentación)
# - '29-Perfil renal (función renal incluye creatinina NUS urea)',
# - '30-Electrolitos plasmáticos incluye sodio potasio cloro)',
# - '31-Perfil hepático (función hepática incluye bilirrubina total y conjugada fosfatasas alcalinas totales GGT ',transaminasas GOT/AST y GPT/ALT)
# - '32-Albúmina (proteínas séricas incluye proteínas totales albúminas)',
# - '33-Deshidrogenasa láctica total (LDH)',
# - '34-Pruebas de coagulación (incluye tiempo de protrombina tiempo de o consumo de (incluye INR relación internacional ',normalizada) Tromboplastina tiempo parcial de (TTPA TTPK o similares)
# - '35-Prueba de compatibilidad por unidad de glóbulos rojos (proc. aut.)',
# - '36-Transfusión en adulto (atención ambulatoria atención cerrada siempre que la administración sea controlada por ',profesional especialista tecnólogo médico o médico responsable
# - '37-Set de exámenes por unidad de glóbulos rojos transfundida (incluye clasificación ABO y RHO VDRL HIV virus hepatitis ',Bantígeno de superficie anticuerpos de hepatitis C HTLV-I y II Chagas prueba de compatibilidad eritrocitaria)
# - '38-E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)',
# - '39-Radiografía de tórax frontal y lateral incluye fluoroscopía',
# - '40-Tomografía computarizada de pelvis (además incluye sacro coxis caderas huesos pélvicos articulaciones sacro iliacas). ',Bilateral
# - '41-Tomografía computarizada de abdomen (hígado vías y vesícula biliar páncreas bazo suprarrenales y riñones) (40 cortes ',8-10 mm)
# - '42-Tomografía computarizada de tórax. Incluye además: esternón clavículas articulación acromioclavicular escápula ',costillas articulación esternoclavicular. Incluye todo el tórax o cada segmento o articulación. Incluye bilateralidad
# - '43-Ano-recto sigmoidoscopia',
# - '44-Estudio histopatológico con técnicas histoquimicas especiales',
# - '45-Estudio histopatológico corriente de biopsia diferida',
# - '46-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)',
# - '47-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado',
# - '48-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye ',biopsia diferida)
# - '49-Estudios moleculares específicos',
# - '50-Cistoscopia y/o uretrocistoscopia y/o uretroscopia',
# - '51-Estudio histopatológico con técnicas histoquimicas especiales',
# - '52-Estudio histopatológico corriente de biopsia diferida',
# - '53-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)',
# - '54-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado',
# - '55-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye ',biopsia diferida)
# - '56-Estudios moleculares específicos',
# - '57-Consulta integral de especialidades en Medicina interna y Subespecialidades Oftalmología Neurología Oncología',
# - '58-Visita por médico interconsultor (o en junta médica c/u) a enfermo hospitalizado',
# 
# 

# In[ ]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import re


# In[ ]:


prestaciones = [
    '23-Orina completa',
    '24-Urocultivo recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)',
    '25-Glucosa',
    '26-Creatinina',
    '27-Protrombina tiempo de o consumo de (incluye INR Relación Internacional Normalizada)',
    '28-Hemograma (incluye recuentos de leucocitos eritrocitos y plaquetas hemoglobina hematocrito fórmula leucocitaria características de los elementos figurados y velocidad de eritrosedimentación)',
    '29-Perfil bioquímico básico',
    '30-Perfil renal (función renal incluye creatinina NUS urea)',
    '31-Electrolitos plasmáticos incluye sodio potasio cloro)',
    '32-Perfil hepático (función hepática incluye bilirrubina total y conjugada fosfatasas alcalinas totales GGT transaminasas GOT/AST y GPT/ALT)',
    '33-Albúmina (proteínas séricas incluye proteínas totales albúminas)',
    '34-Deshidrogenasa láctica total (LDH)',
    '35-Pruebas de coagulación (incluye tiempo de protrombina tiempo de o consumo de (incluye INR relación internacional normalizada) Tromboplastina tiempo parcial de (TTPA TTPK o similares)',
    '36-Prueba de compatibilidad por unidad de glóbulos rojos (proc. aut.)',
    '37-Transfusión en adulto (atención ambulatoria atención cerrada siempre que la administración sea controlada por profesional especialista tecnólogo médico o médico responsable',
    '39-E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)',
    '40-Radiografía de tórax frontal y lateral incluye fluoroscopía',
    '41-Tomografía computarizada de pelvis (además incluye sacro coxis caderas huesos pélvicos articulaciones sacro iliacas). Bilateral',
    '42-Tomografía computarizada de abdomen (hígado vías y vesícula biliar páncreas bazo suprarrenales y riñones) (40 cortes 8-10 mm)',
    '43-Tomografía computarizada de tórax. Incluye además: esternón clavículas articulación acromioclavicular escápula costillas articulación esternoclavicular. Incluye todo el tórax o cada segmento o articulación. Incluye bilateralidad'
]


    

# Agregar preguntas
preguntas = [ 
    "¿Se le indicó esta prestación?",q
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
    '38-Set de exámenes por unidad de glóbulos rojos transfundida (incluye clasificación ABO y RHO VDRL HIV virus hepatitis Bantígeno de superficie anticuerpos de hepatitis C HTLV-I y II Chagas prueba de compatibilidad eritrocitaria)'
    ]
# Agregar preguntas
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df1 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = ["44-Ano-recto sigmoidoscopia", "51-Cistoscopia y/o uretrocistoscopia y/o uretroscopia"]

#Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]

# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df2 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
'45-Estudio histopatológico con técnicas histoquimicas especiales',
'46-Estudio histopatológico corriente de biopsia diferida',
'47-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)',
'48-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado',
'49-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)',
'50-Estudios moleculares específicos',
'52-Estudio histopatológico con técnicas histoquimicas especiales',
'53-Estudio histopatológico corriente de biopsia diferida',
'54-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)',
'55-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado',
'56-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)',
'57-Estudios moleculares específicos'
]

# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df3 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "58-Consulta integral de especialidades en Medicina interna y Subespecialidades Oftalmología Neurología Oncología"
]
# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df4 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    '59-Visita por médico interconsultor (o en junta médica c/u) a enfermo hospitalizado'             
]
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Se le informó el resultado de la junta médica oncológica?",
    "Indique la fecha en que se le informó el resultado de la junta médica",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df5 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


# Agregar una columna con el número de la prestación
df['Numero Prestación'] = df['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df1['Numero Prestación'] = df1['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df2['Numero Prestación'] = df2['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df3['Numero Prestación'] = df3['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df4['Numero Prestación'] = df4['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df5['Numero Prestación'] = df5['Nombre Prestación'].str.extract(r'(\d+)').astype(int)

# Combinar los DataFrames
df_combined = pd.concat([df,df1,df2,df3,df4,df5], ignore_index=True)


# In[ ]:


# Ordenar el DataFrame por la columna 'Numero Prestación' y 'Orden Pregunta'
df_combined_sorted = df_combined.sort_values(by=['Numero Prestación', 'Orden Pregunta']).reset_index(drop=True)


# In[ ]:


df = df_combined_sorted


# In[ ]:


prestaciones=[
'23-Orina completa',
'24-Urocultivo recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)',
'25-Glucosa',
'26-Creatinina',
'27-Protrombina tiempo de o consumo de (incluye INR Relación Internacional Normalizada)',
'28-Hemograma (incluye recuentos de leucocitos eritrocitos y plaquetas hemoglobina hematocrito fórmula leucocitaria características de los elementos figurados y velocidad de eritrosedimentación)',
'29-Perfil bioquímico básico',
'30-Perfil renal (función renal incluye creatinina NUS urea)',
'31-Electrolitos plasmáticos incluye sodio potasio cloro)',
'32-Perfil hepático (función hepática incluye bilirrubina total y conjugada fosfatasas alcalinas totales GGT transaminasas GOT/AST y GPT/ALT)',
'33-Albúmina (proteínas séricas incluye proteínas totales albúminas)',
'34-Deshidrogenasa láctica total (LDH)',
'35-Pruebas de coagulación (incluye tiempo de protrombina tiempo de o consumo de (incluye INR relación internacional normalizada) Tromboplastina tiempo parcial de (TTPA TTPK o similares)',
'36-Prueba de compatibilidad por unidad de glóbulos rojos (proc. aut.)',
'37-Transfusión en adulto (atención ambulatoria atención cerrada siempre que la administración sea controlada por profesional especialista tecnólogo médico o médico responsable',
'38-Set de exámenes por unidad de glóbulos rojos transfundida (incluye clasificación ABO y RHO VDRL HIV virus hepatitis Bantígeno de superficie anticuerpos de hepatitis C HTLV-I y II Chagas prueba de compatibilidad eritrocitaria)',
'39-E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)',
'40-Radiografía de tórax frontal y lateral incluye fluoroscopía',
'41-Tomografía computarizada de pelvis (además incluye sacro coxis caderas huesos pélvicos articulaciones sacro iliacas). Bilateral',
'42-Tomografía computarizada de abdomen (hígado vías y vesícula biliar páncreas bazo suprarrenales y riñones) (40 cortes 8-10 mm)',
'43-Tomografía computarizada de tórax. Incluye además: esternón clavículas articulación acromioclavicular escápula costillas articulación esternoclavicular. Incluye todo el tórax o cada segmento o articulación. Incluye bilateralidad',
'44-Ano-recto sigmoidoscopia',
'45-Estudio histopatológico con técnicas histoquimicas especiales',
'46-Estudio histopatológico corriente de biopsia diferida',
'47-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)',
'48-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado',
'49-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)',
'50-Estudios moleculares específicos',
'51-Cistoscopia y/o uretrocistoscopia y/o uretroscopia',
'52-Estudio histopatológico con técnicas histoquimicas especiales',
'53-Estudio histopatológico corriente de biopsia diferida',
'54-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)',
'55-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado',
'56-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)',
'57-Estudios moleculares específicos',
'58-Consulta integral de especialidades en Medicina interna y Subespecialidades Oftalmología Neurología Oncología',
'59-Visita por médico interconsultor (o en junta médica c/u) a enfermo hospitalizado'

    
]


# In[ ]:


# Definir las variables de cada pregunta
variables = [
    "indica_",
    "fecha_indica_",
    "realiza_",
    "fecha_realiza_",
    "lugar_",
    "lugar_exm_",
    "lugar_inf_exm_",
    "fecha_envio_",
    "fecha_devol_",
    "inform_resul_",
    "inform_resul_",
    "inform_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_prox_",
    "fecha_prox_",
    "reagenda_",
    "n_reagenda_",
    "fecha_prim_reag_",
    "razon_prim_reag_",
    "fecha_sec_reag_",
    "razon_sec_reag_",
    "fecha_ter_reag_",
    "razon_ter_reag_",
    "fecha_cuar_reag_",
    "razon_cuar_reag_",
    "fecha_quin_reag_",
    "razon_quin_reag_",
    "tipo_med_",
    "otro_med_",
    "tipo_espe_med_",
    "otro_esp_med_",
    "tipo_prof_",
    "otro_prof_",
    "toma_biop_",
    "no_biop_",
    "otro_no_biop_",
    "tipo_biop_",
    "tipo_molec_",
    "otro_molec_"]


# Actualizar las variables por cada pregunta

df['Variable'] = df['Preguntas'].apply(lambda x: variables[[
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "¿Dónde se realizó el informe del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "¿Se le informó el resultado del procedimiento?",
    "¿Se le informó el resultado de la junta médica oncológica?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    'Indique la fecha en que se le informó el resultado de la junta médica',
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    "Indique qué médico lo atendió",
    "¿Cuál otro médico?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Indique qué profesional lo atendió",
    "¿Cuál otro profesional?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Qué tipo de estudio de biopsia se le indicó?",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio"].index(x)])


# In[ ]:


# Define una lista de números únicos por cada prestación
prestacion_numbers = list(range(23, len(prestaciones) + 58))

# Crea un diccionario para mapear prestaciones y asignar el número que corresponda
prestacion_to_number = {prestacion: number for prestacion, number in zip(prestaciones, prestacion_numbers)}

# Agrega la nueva columna "Numero prestación"
df['Numero prestacion'] = df['Nombre Prestación'].map(prestacion_to_number)

# Reordena la posición de las variables
df = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas', 'Variable']]


# In[ ]:


# Crea una nueva columna "Nombre Variable Final" según el nombre de la variable, el número de prestación y el tipo de capacidad
df['Nombre Variable Final'] = df['Variable'] + 'cacu_' + df['Numero prestacion'].astype(str) + "_etap"


# In[ ]:


df


# ##### Comienza formato RedCap
# 
# - 1. Dejar solo las columnas que necesito: Nombre prestación, Pregunta y Nombre Variable Final
# - 2. Cambiar nombre al formato de redcap de las columnas que tengo
# - 3. Agregar columna "Section Header": título de cada prestación
# - 4. Agregar columna "Form Name" : nombre del formulario en redcap
# - 5. Agregar columna "Field Type" : Tipo de dato

# In[ ]:


#Dejar solo las columnas que necesito
df_cacu_etap = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas','Nombre Variable Final']]

#Cambiar nombre de la variable

nombres_nuevos = {'Nombre Variable Final':'Variable / Field Name',
                 'Preguntas' : 'Field Label'}
df_cacu_etap.rename(columns=nombres_nuevos, inplace=True)

# Crear columna Section 
df_cacu_etap['Section Header'] = ''

# Asignar S.H. según el nombre de la prestación 
df_cacu_etap.loc[df_cacu_etap.groupby('Nombre Prestación').cumcount() == 0, 'Section Header'] = df['Nombre Prestación']


# In[ ]:


# Crear columna con el nombre del formulario 

df_cacu_etap['Form Name'] = "formulario_diagnostico_cacu"
df_cacu_etap["Field Note"] = ""


# In[ ]:


# Crear la columna 'Field Type' con valores por defecto 'text'
df_cacu_etap['Field Type'] = 'text'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("indica_","realiza_","lugar_","lugar_exm_",
                                                          "inform_resul_","reagenda_","razon_prim_reag_",
                                                          "razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_",
                                                          "razon_quin_reag_","tipo_med_","tipo_espe_med_","n_reagenda_",
                                                          "toma_biop_","no_biop","tipo_biop_","tipo_molec_",
                                                          "tipo_espe_med_","reagenda_biop_","lugar_inf_exm_","tipo_prof_"



))

df_cacu_etap.loc[condic, 'Field Type'] = 'dropdown'

# Crear la columna 'Choices, Calculations, OR Slider Labels'
df_cacu_etap['Choices, Calculations, OR Slider Labels'] = ''

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(('indica_','realiza_','inform_resul_','reagenda_','toma_biop_'))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Si | 2, No'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(('lugar_'))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(('lugar_exm_'))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Lab de la Red SSMSO  | 2,  Lab externo'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("razon_prim_reag_","razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_","razon_quin_reag_"))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se presentó | 2, Reagendamiento por temas administrativos (Ej: paro de funcionarios) | 3, Reagendamiento por rechazo del paciente | 4, Rechazo de interconsulta por Contralor | 5, Paciente no termina su tratamiento | 6, Paciente fallecido | 7, Paciente perdido (Ej: continuó su atención clínica en el extrasistema) | 8, Información no disponible'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("n_reagenda_"))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("tipo_med_"))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Médico de familia | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("tipo_prof_"))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Enfermera | 2, Matrona | 3, Kinesióloga| 4, Nutricionista | 5, Otra (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("tipo_biop_"))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Estudio histopatológico con técnicas histoquimicas especiales" | 2, Estudio histopatológico corriente de biopsia diferida(por cada órgano)" | 3, Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)" | 4, Estudio histopatológico con tinción corriente de biopsia diferida con estudio seriado (mínimo 10 muestras) de un órgano o parte de él (no incluye estudio con técnica habitual de otros órganos incluidos en la muestra) | 5, Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)'
                                 
# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("no_biop_"))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se encontró lesión | 2, Imposibilidad de tomar muestra | 3, Falta de insumos o RRHH | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("lugar_inf_exm_"))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("tipo_molec_"))
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, P16 | 2, Estudios de receptores hormonales  | 3, PDL-1 | 4, Otro (Especificar)'



# Actualizar la columna ''Text Validation Type OR Show Slider Number' con 'dropdown' si corresponde
condic = df_cacu_etap['Variable / Field Name'].str.startswith(("fecha_"))
df_cacu_etap.loc[condic, 'Text Validation Type OR Show Slider Number'] = 'date_dmy'


# In[ ]:



# Define the function to apply the correct branching logic
def generate_branching_logic(row):
    variable_name = row['Variable / Field Name']
    try:
        num_prest = int(row['Numero prestacion'])
    except (ValueError, TypeError):
        return ""
    
    if variable_name == f"indica_cacu_{num_prest}_etap":
        return f"[resul_biop_cacu_diag]=1"
    
    elif variable_name == f"fecha_indica_cacu_{num_prest}_etap":
        return f"[indica_cacu_{num_prest}_etap]=1"
    
    elif variable_name == f"realiza_cacu_{num_prest}_etap":
        return f"[indica_cacu_{num_prest}_etap]=1"
    
    elif variable_name == f"fecha_realiza_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]=1"
    
    elif variable_name == f"lugar_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]=1"
    
    elif variable_name == f"lugar_exm_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"
    
    elif variable_name == f"fecha_envio_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"
    
    elif variable_name == f"fecha_devol_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"
    
    elif variable_name == f"inform_resul_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"
    
    elif variable_name == f"fecha_resul_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1 and [inform_resul_cacu_{num_prest}_etap]=1"
    
    elif variable_name == f"fecha_prox_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"
    
    elif variable_name == f"reagenda_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]=1 or [realiza_cacu_{num_prest}_etap]=2"
    
    elif variable_name == f"n_reagenda_cacu_{num_prest}_etap":
        return f"[reagenda_cacu_{num_prest}_etap]=1"
    
    elif variable_name == f"fecha_prim_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=1"
    
    elif variable_name == f"razon_prim_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=1"
    
    elif variable_name == f"fecha_sec_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=2"
    
    elif variable_name == f"razon_sec_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=2"
    
    elif variable_name == f"fecha_ter_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=3"
    
    elif variable_name == f"razon_ter_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=3"
    
    elif variable_name == f"fecha_cuar_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=4"
    
    elif variable_name == f"razon_cuar_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=4"
    
    elif variable_name == f"fecha_quin_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=5"
    
    elif variable_name == f"razon_quin_reag_cacu_{num_prest}_etap":
        return f"[n_reagenda_cacu_{num_prest}_etap]>=5"
    
    elif variable_name == f"tipo_espe_med_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"

    elif variable_name == f"otro_esp_med_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1 and [tipo_espe_med_cacu_{num_prest}_etap]=7"
    
    elif variable_name == f"tipo_med_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"

    elif variable_name == f"otro_med_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1 and [tipo_med_cacu_{num_prest}_etap]=4"
                                                          
    elif variable_name == f"tipo_prof_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"

    elif variable_name == f"otro_prof_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1 and [tipo_prof_cacu_{num_prest}_etap]=5"
    
    elif variable_name == f"lugar_inf_exm_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"
    
    elif variable_name == f"toma_biop_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"
    
    elif variable_name == f"no_biop_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1 and [toma_biop_cacu_{num_prest}_etap]=2"
    
    elif variable_name == f"otro_no_biop_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1 and [no_biop_cacu_{num_prest}_etap]=4"    
    
    elif variable_name == f"tipo_biop_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1 and [toma_biop_cacu_{num_prest}_etap]=1"
    
    elif variable_name == f"tipo_molec_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1"
    
    elif variable_name == f"otro_molec_cacu_{num_prest}_etap":
        return f"[realiza_cacu_{num_prest}_etap]= 1 and [tipo_molec_cacu_{num_prest}_etap]=4"

    
        return ""
    
    # Apply the function to create the new column
df_cacu_etap['Branching Logic (Show field only if...)'] = df_cacu_etap.apply(generate_branching_logic, axis=1)


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_45_etap", "realiza_cacu_46_etap", "realiza_cacu_47_etap", 
    "realiza_cacu_48_etap", "realiza_cacu_49_etap", "realiza_cacu_50_etap"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu_etap['Variable / Field Name'].isin(nombres_completos)
df_cacu_etap.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_44_etap]=1 and [toma_biop_cacu_44_etap]=1"


# In[ ]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
nombres_completos = ["tipo_espe_med_cacu_58_etap"]


# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu_etap['Variable / Field Name'].isin(nombres_completos)
df_cacu_etap.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Cirujano General| 4, Internista | 5, Cirujano mama | 6, Ginecólogo Oncólogo | 7, Otro médico especialista (Especificar)'


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_52_etap", "realiza_cacu_53_etap", "realiza_cacu_54_etap", 
    "realiza_cacu_55_etap", "realiza_cacu_56_etap", "realiza_cacu_57_etap"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu_etap['Variable / Field Name'].isin(nombres_completos)
df_cacu_etap.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_51_etap]=1 and [toma_biop_cacu_51_etap]=5"


# In[ ]:


# Define the new columns with empty values
new_columns = {
    'Text Validation Min': '',
    'Text Validation Max': '',
    'Identifier?': '',
    'Required Field?': '',
    'Custom Alignment': '',
    'Question Number (surveys only)': '',
    'Matrix Group Name': '',
    'Matrix Ranking?': '',
    'Field Annotation': ''
}

# Add these new columns to the existing dataframe with default empty values
for column, value in new_columns.items():
    df_cacu_etap[column] = value

# Definir el orden de las variables en el df

orden_deseado = ['Variable / Field Name', 'Form Name', 'Section Header', 'Field Type',
       'Field Label', 'Choices, Calculations, OR Slider Labels', 'Field Note',
       'Text Validation Type OR Show Slider Number', 'Text Validation Min',
       'Text Validation Max', 'Identifier?',
       'Branching Logic (Show field only if...)', 'Required Field?',
       'Custom Alignment', 'Question Number (surveys only)',
       'Matrix Group Name', 'Matrix Ranking?', 'Field Annotation']

#Reordenar
df_cacu_ = df_cacu_etap[orden_deseado]


# In[ ]:


df_cacu_.to_excel("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/CaCu_etap.xlsx")

df_cacu_.to_csv("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv", index=False)


# In[ ]:


import zipfile
import os

# Ruta del archivo que quieres comprimir
archivo_csv = "C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv"

# Ruta donde se guardará el archivo comprimido
ruta_salida_zip = r"C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/Cacu_etap.zip"

# Crear un archivo ZIP y agregar el archivo CSV
with zipfile.ZipFile(ruta_salida_zip, 'w') as archivo_zip:
    archivo_zip.write(archivo_csv, os.path.basename(archivo_csv))

print(f"Archivo comprimido guardado en: {ruta_salida_zip}")


# In[ ]:


# Combinar los DataFrames
df_diag_etap = pd.concat([df_cacu, df_cacu_], ignore_index=True)


# In[ ]:


df_diag_etap.to_excel("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/Cacu_diag_etap.xlsx")

df_diag_etap.to_csv("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv", index=False)


# In[ ]:


import zipfile
import os

# Ruta del archivo que quieres comprimir
archivo_csv = "C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv"

# Ruta donde se guardará el archivo comprimido
ruta_salida_zip = r"C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/Cacu_diag_etap.zip"

# Crear un archivo ZIP y agregar el archivo CSV
with zipfile.ZipFile(ruta_salida_zip, 'w') as archivo_zip:
    archivo_zip.write(archivo_csv, os.path.basename(archivo_csv))

print(f"Archivo comprimido guardado en: {ruta_salida_zip}")


# ### Tratamiento

# ### TTO Quirúrgico CaCu Invasor
# 
# #### CaCu Pre-Invasor
# 
# ##### Cacu Nie I
# - Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología
# - Consulta o control por enfermera, matrona o nutricionista
# - Citodiagnóstico corriente, exfoliativa (Papanicolau y similares) (por cada órgano)
# - Colposcopía
# - Estudio histopatológico con técnicas histoquimicas especiales
# - Estudio histopatológico corriente de biopsia diferida
# - Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)
# - Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado
# - Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)
# - Estudios moleculares específicos
# 
# ##### CaCu NIE II, III o CIS
# ##### Hospitalización
# - Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más)
# - Día cama integral de observación o día cama integral ambulatorio diurno
# 
# ##### Exámenes
# - Grupos sanguíneos AB0 y Rho (incluye estudio de factor Du en Rh negativos)
# - Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)
# - Protrombina, tiempo de consumo (incluye INR, Relación Internacional Normalizada)
# - Creatinina
# - Glucosa en sangre
# - Orina completa
# - Urocultivo, recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)
# - E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)
# 
# ##### Cirugía
# - Electrodiatermo o criocoagulación de lesiones del cuello
# - Histerectomía total o ampliada por vía abdominal; útero y sus elementos de sostén
# - Conización y/o amputación del cuello, diagnostica y/o terapéutica c/s biopsia
# - Estudio histopatológico con técnicas histoquimicas especiales
# - Estudio histopatológico corriente de biopsia diferida
# - Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)
# - Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado
# - Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)
# - Estudios moleculares específicos
# - Histerectomía por vía vaginal
# 
# #### Tratamiento quirurgico CaCu Invasor
# 
# ##### Exámenes
# - Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)
# - Protrombina, tiempo de o consumo de (incluye INR, Relación Internacional Normalizada)
# - Creatinina
# - Electrolitos plasmáticos (sodio, potasio, cloro) c/u
# - Glucosa
# - Orina completa
# - Urocultivo, recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)
# - Set de Exámenes por unidad de Glóbulos Rojos transfundida (incluye clasificación ABO y Rho, VDRL, HIV, virus hepatitis B antígeno de superficie, anticuerpos de hepatitis C, HTLV - I y II, Chagas, prueba de compatibilidad eritrocitaria)
# - Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)
# 
# ##### Cirugía
# - Conización y/o amputación del cuello, diagnostica y/o terapéutica c/s biopsia
# - Estudio histopatológico con técnicas histoquimicas especiales
# - Estudio histopatológico corriente de biopsia diferida
# - Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)
# - Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado
# - Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)
# - Estudios moleculares específicos
# - Histerectomía radical con disección pelviana completa de territorios ganglionares, incluye ganglios lumboaórticos(operación de Wertheim o similares)
# - Linfadenectomía pelviana laparoscópica
# - Traquelectomía radical
# 
# ##### Post Operatorio
# - Día cama hospitalización integral medicina,
# - Día Cama UCI (1.109)
# - Día cama UTI (1.110)
# - Atención kinesiológica integral ambulatoria
# 
# #### Quimioterapia CaCu Invasor - Quimioterapia Recidivia CaCu Invasor
# - Visita por médico interconsultor (o en junta médica c/u) a enfermo hospitalizado'
# - Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología
# 
# ##### Hospitalización por quimioterapia
# - Educación de grupo por enfermera, matrona o nutricionista
# - Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más) Hospitales tipo 1
# - Día cama integral de observación o día cama integral ambulatorio diurno
# - Instalación de catéter Swan-Ganz o similar, en adultos o niños (proc. aut.)
# - Catéter con reservorio
# 
# ##### Examenes
# - Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)
# - Creatinina
# - Perfil Hepático (incluye: toma de muestra, tiempo de protrombina, bilirrubina total y conjugada, fosfatasas alcalinas totales, GGT, transaminasas GOT y GPT).
# - Tórax (frontal y lateral) (incluye fluoroscopía) (2 proy. panorámicas) (2 exp.)
# 
# ##### Radioterapia
# - Preparación de glóbulos rojos, plasma, plaquetas o crioprecipitados (incluye entrevista, selección del donante y la preparación del respectivo hemocomponente)
# - Set de Exámenes por unidad de Glóbulos Rojos transfundida (incluye clasificación ABO y Rho, VDRL, HIV, virus hepatitis B antígeno de superficie, anticuerpos de hepatitis C, HTLV - I y II, Chagas, prueba de compatibilidad eritrocitaria)
# - Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)
# - Radioterapia
# 
# ##### Braquiterapia
# - Día cama hospitalización integral intermedio adulto
# - E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)
# - Braquiterapia
# 
# #### Atención Integral para pacientes con cáncer
# - Educación de grupo por enfermera, matrona o nutricionista
# - Educación de grupo por asistente social
# - Consulta integral de especialidades Psiquiatría
# - Consulta o control por psicólogo clínico

# In[ ]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import re


# In[ ]:


prestaciones=[
    "112-Atención kinesiológica integral ambulatoria",
    "116-Educación de grupo por enfermera, matrona o nutricionista",
    "133-Educación de grupo por enfermera, matrona o nutricionista",
    "134-Educación de grupo por asistente social",
    "135-Consulta integral de especialidades Psiquiatría",
    "136-Consulta o control por psicólogo clínico"
    
]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"  
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "60-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología",
    "114-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología"
]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df1 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "61-Consulta o control por enfermera, matrona o nutricionista"
    
]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué profesional lo atendió",
    "¿Cuál otro profesional?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df2 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
    "62-Citodiagnóstico corriente, exfoliativa (Papanicolau y similares) (por cada órgano)"

    ]


# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df3 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
"72-Grupos sanguíneos AB0 y Rho (incluye estudio de factor Du en Rh negativos)",
"73-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
"74-Protrombina, tiempo de consumo (incluye INR, Relación Internacional Normalizada)",
"75-Creatinina",
"76-Glucosa en sangre",
"77-Orina completa",
"78-Urocultivo, recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)",
"79-E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)",
"90-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
"91-Protrombina, tiempo de o consumo de (incluye INR, Relación Internacional Normalizada)",
"92-Creatinina",
"93-Electrolitos plasmáticos (sodio, potasio, cloro) c/u",
"94-Glucosa",
"95-Orina completa",
"96-Urocultivo, recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)",
"98-Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)",
"122-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
"123-Creatinina",
"124-Perfil Hepático (incluye: toma de muestra, tiempo de protrombina, bilirrubina total y conjugada, fosfatasas alcalinas totales, GGT, transaminasas GOT y GPT).",
"125-Tórax (frontal y lateral) (incluye fluoroscopía) (2 proy. panorámicas) (2 exp.)",
"128-Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)",
"131-E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)"



]

    
    
# Agregar preguntas
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df4 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
    "97-Set de Exámenes por unidad de Glóbulos Rojos transfundida (incluye clasificación ABO y Rho, VDRL, HIV, virus hepatitis B antígeno de superficie, anticuerpos de hepatitis C, HTLV - I y II, Chagas, prueba de compatibilidad eritrocitaria)",
    "127-Set de Exámenes por unidad de Glóbulos Rojos transfundida (incluye clasificación ABO y Rho, VDRL, HIV, virus hepatitis B antígeno de superficie, anticuerpos de hepatitis C, HTLV - I y II, Chagas, prueba de compatibilidad eritrocitaria)"
]

# Agregar preguntas
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df5 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = ["63-Colposcopía",
                "80-Electrodiatermo o criocoagulación de lesiones del cuello",
                "81-Histerectomía total o ampliada por vía abdominal; útero y sus elementos de sostén",
                "82-Conización y/o amputación del cuello, diagnostica y/o terapéutica c/s biopsia",
                "89-Histerectomía por vía vaginal",
                "99-Conización y/o amputación del cuello, diagnostica y/o terapéutica c/s biopsia",
                "106-Histerectomía radical con disección pelviana completa de territorios ganglionares, incluye ganglios lumboaórticos(operación de Wertheim o similares)",
                "107-Linfadenectomía pelviana laparoscópica",
                "108-Traquelectomía radical"
               ]

#Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]

# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df6 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
"64-Estudio histopatológico con técnicas histoquimicas especiales",
"65-Estudio histopatológico corriente de biopsia diferida",
"66-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"67-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
"68-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
"83-Estudio histopatológico con técnicas histoquimicas especiales",
"84-Estudio histopatológico corriente de biopsia diferida",
"85-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"86-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
"87-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
"100-Estudio histopatológico con técnicas histoquimicas especiales",
"101-Estudio histopatológico corriente de biopsia diferida",
"102-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"103-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
"104-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)"

]

# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df7 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "69-Estudios moleculares específicos",
    "88-Estudios moleculares específicos",
    "105-Estudios moleculares específicos"
]

# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen"
    
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df8 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "70-Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más)",
    "71-Día cama integral de observación o día cama integral ambulatorio diurno",
    "109-Día cama hospitalización integral medicina",
    "110-Día Cama UCI",
    "111-Día cama UTI",
    "117-Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más) Hospitales tipo 1",
    "118-Día cama integral de observación o día cama integral ambulatorio diurno",
    "130-Día cama hospitalización integral intermedio adulto"
    
]
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique la fecha de alta hospitalaria",
    "Indique el o los diagnósticos de alta hospitalaria (ver GRD del episodio)",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df9 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "119-Instalación de catéter Swan-Ganz o similar, en adultos o niños (proc. aut.)",
    "120-Catéter con reservorio"]

preguntas = [
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué tipo de catéter fue indicado",
    "Indique qué tipo de catéter fue instalado",
    "¿El catéter quedó operativo?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"]
    
# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df10= pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "121-Curación simple ambulatoria"]

preguntas = [
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique la fecha en que se le realizó la prestación siguiente a este procedimiento",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"]
    
# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df11 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "115-Quimioterapia"
    ]

preguntas = [
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "¿Dónde se realizó esta prestación?",
    "¿Qué tipo de quimioterapia se le indicó?",
    "En cuanto a las drogas usadas en tratamiento ¿Qué drogas se le indicó?",
    "Otra droga",
    "Indique número de ciclos en plan de tratamiento",
    "Indique número de ciclos efectivamente realizadas",
    "Indique la fecha de inicio del tratamiento",
    "Indique la fecha de término del tratamiento",
    "Indique la fecha en que se le realizó la prestación siguiente a este procedimiento",
    "¿Hubo alguna interrupción en el tratamiento?",
    "¿Por qué se interrumpió el tratamiento?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"]
# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df12= pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "129-Radioterapia"]

preguntas = [
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Qué intención de radioterapia se le indicó?",
    "¿Qué tipo de radioterapia se le indicó?",
    "Indique número de ciclos en plan de tratamiento",
    "Indique número de ciclos efectivamente realizadas",
    "Indique la fecha de inicio del tratamiento",
    "Indique la fecha de término del tratamiento",
    "Indique la fecha en que se le realizó la prestación siguiente a este procedimiento",
    "¿Hubo alguna interrupción en el tratamiento?",
    "¿Por qué se interrumpió el tratamiento?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"]
# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df13 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "132-Braquiterapia"
    ]

preguntas = [
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "¿Dónde se realizó esta prestación?",
    "¿Qué tipo de braquiterapia se le indicó?",
    "Otro tipo de braquiterapia",
    "Indique número de ciclos en plan de tratamiento",
    "Indique número de ciclos efectivamente realizadas",
    "Indique la fecha de inicio del tratamiento",
    "Indique la fecha de término del tratamiento",
    "Indique la fecha en que se le realizó la prestación siguiente a este procedimiento",
    "¿Hubo alguna interrupción en el tratamiento?",
    "¿Por qué se interrumpió el tratamiento?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"]
# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df14 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "113-Visita por médico interconsultor (o en junta médica c/u) a enfermo hospitalizado"
             
]
# Agregar preguntas
preguntas = [
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Se le informó el resultado de la junta médica oncológica?",
    "Indique la fecha en que se le informó el resultado de la junta médica",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados de la prestación",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    ]
    
# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df15 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


# Agregar una columna con el número de la prestación
df['Numero Prestación'] = df['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df1['Numero Prestación'] = df1['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df2['Numero Prestación'] = df2['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df3['Numero Prestación'] = df3['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df4['Numero Prestación'] = df4['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df5['Numero Prestación'] = df5['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df6['Numero Prestación'] = df6['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df7['Numero Prestación'] = df7['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df8['Numero Prestación'] = df8['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df9['Numero Prestación'] = df9['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df10['Numero Prestación'] = df10['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df11['Numero Prestación'] = df11['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df12['Numero Prestación'] = df12['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df13['Numero Prestación'] = df13['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df14['Numero Prestación'] = df14['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df15['Numero Prestación'] = df15['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
# Combinar los DataFrames
df_combined = pd.concat([df,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15], ignore_index=True)


# In[ ]:


# Ordenar el DataFrame por la columna 'Numero Prestación' y 'Orden Pregunta'
df_combined_sorted = df_combined.sort_values(by=['Numero Prestación', 'Orden Pregunta']).reset_index(drop=True)

df = df_combined_sorted


# In[ ]:


prestaciones=[
"60-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología",
"61-Consulta o control por enfermera, matrona o nutricionista",
"62-Citodiagnóstico corriente, exfoliativa (Papanicolau y similares) (por cada órgano)",
"63-Colposcopía",
"64-Estudio histopatológico con técnicas histoquimicas especiales",
"65-Estudio histopatológico corriente de biopsia diferida",
"66-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"67-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
"68-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
"69-Estudios moleculares específicos",
"70-Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más)",
"71-Día cama integral de observación o día cama integral ambulatorio diurno",
"72-Grupos sanguíneos AB0 y Rho (incluye estudio de factor Du en Rh negativos)",
"73-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
"74-Protrombina, tiempo de consumo (incluye INR, Relación Internacional Normalizada)",
"75-Creatinina",
"76-Glucosa en sangre",
"77-Orina completa",
"78-Urocultivo, recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)",
"79-E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)",
"80-Electrodiatermo o criocoagulación de lesiones del cuello",
"81-Histerectomía total o ampliada por vía abdominal; útero y sus elementos de sostén",
"82-Conización y/o amputación del cuello, diagnostica y/o terapéutica c/s biopsia",
"83-Estudio histopatológico con técnicas histoquimicas especiales",
"84-Estudio histopatológico corriente de biopsia diferida",
"85-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"86-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
"87-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
"88-Estudios moleculares específicos",
"89-Histerectomía por vía vaginal",
"90-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
"91-Protrombina, tiempo de o consumo de (incluye INR, Relación Internacional Normalizada)",
"92-Creatinina",
"93-Electrolitos plasmáticos (sodio, potasio, cloro) c/u",
"94-Glucosa",
"95-Orina completa",
"96-Urocultivo, recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)",
"97-Set de Exámenes por unidad de Glóbulos Rojos transfundida (incluye clasificación ABO y Rho, VDRL, HIV, virus hepatitis B antígeno de superficie, anticuerpos de hepatitis C, HTLV - I y II, Chagas, prueba de compatibilidad eritrocitaria)",
"98-Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)",
"99-Conización y/o amputación del cuello, diagnostica y/o terapéutica c/s biopsia",
"100-Estudio histopatológico con técnicas histoquimicas especiales",
"101-Estudio histopatológico corriente de biopsia diferida",
"102-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"103-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
"104-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
"105-Estudios moleculares específicos",
"106-Histerectomía radical con disección pelviana completa de territorios ganglionares, incluye ganglios lumboaórticos(operación de Wertheim o similares)",
"107-Linfadenectomía pelviana laparoscópica",
"108-Traquelectomía radical",
"109-Día cama hospitalización integral medicina",
"110-Día Cama UCI",
"111-Día cama UTI",
"112-Atención kinesiológica integral ambulatoria",
"113-Visita por médico interconsultor (o en junta médica c/u) a enfermo hospitalizado",
"114-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología",
"115-Quimioterapia",
"116-Educación de grupo por enfermera, matrona o nutricionista",
"117-Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más) Hospitales tipo 1",
"118-Día cama integral de observación o día cama integral ambulatorio diurno",
"119-Instalación de catéter Swan-Ganz o similar, en adultos o niños (proc. aut.)",
"120-Catéter con reservorio",
"121-Curación simple ambulatoria",
"122-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
"123-Creatinina",
"124-Perfil Hepático (incluye: toma de muestra, tiempo de protrombina, bilirrubina total y conjugada, fosfatasas alcalinas totales, GGT, transaminasas GOT y GPT).",
"125-Tórax (frontal y lateral) (incluye fluoroscopía) (2 proy. panorámicas) (2 exp.)",
"126-Preparación de glóbulos rojos, plasma, plaquetas o crioprecipitados (incluye entrevista, selección del donante y la preparación del respectivo hemocomponente)",
"127-Set de Exámenes por unidad de Glóbulos Rojos transfundida (incluye clasificación ABO y Rho, VDRL, HIV, virus hepatitis B antígeno de superficie, anticuerpos de hepatitis C, HTLV - I y II, Chagas, prueba de compatibilidad eritrocitaria)",
"128-Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)",
"129-Radioterapia",
"130-Día cama hospitalización integral intermedio adulto",
"131-E.C.G. de reposo (incluye mínimo 12 derivaciones y 4 complejos por derivación)",
"132-Braquiterapia",
"133-Educación de grupo por enfermera, matrona o nutricionista",
"134-Educación de grupo por asistente social",
"135-Consulta integral de especialidades Psiquiatría",
"136-Consulta o control por psicólogo clínico",
  

]


# In[ ]:


# Definir las variables de cada pregunta
variables = [
    "indica_",
    "fecha_indica_",
    "realiza_",
    "fecha_realiza_",
    "lugar_",
    "lugar_exm_",
    "lugar_inf_exm_",
    "fecha_envio_",
    "fecha_devol_",
    "inform_resul_",
    "inform_resul_",
    "inform_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_prox_",
    "fecha_prox_",
    "fecha_prox_",
    "fecha_prox_",
    "reagenda_",
    "n_reagenda_",
    "fecha_prim_reag_",
    "razon_prim_reag_",
    "fecha_sec_reag_",
    "razon_sec_reag_",
    "fecha_ter_reag_",
    "razon_ter_reag_",
    "fecha_cuar_reag_",
    "razon_cuar_reag_",
    "fecha_quin_reag_",
    "razon_quin_reag_",
    "tipo_med_",
    "otro_med_",
    "tipo_espe_med_",
    "otro_esp_med_",
    "tipo_prof_",
    "otro_prof_",
    "toma_biop_",
    "no_biop_",
    "otro_no_biop_",
    "tipo_biop_",
    "tipo_molec_",
    "otro_molec_",
    "int_radio_",
    "tipo_radio_",
    "n_ciclos_trat_",
    "n_ciclos_efec_",
    "fecha_ini_",
    "fecha_ter_",
    "interrup_trat_",
    "pq_interrup_",
    "tipo_quimio_",
    "tipo_droga_",
    "otra_droga_",
    "fecha_alta_",
    "diag_",
    "tipo_braq_",
    "otro_braq_",
    "tipo_cateter_ind_",
    "tipo_ceteter_inst_",
    "cateter_op_"]


# Actualizar las variables por cada pregunta

df['Variable'] = df['Preguntas'].apply(lambda x: variables[[
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "¿Dónde se realizó el informe del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "¿Se le informó el resultado del procedimiento?",
    "¿Se le informó el resultado de la junta médica oncológica?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado de la junta médica",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Indique la fecha en que se le realizó la prestación siguiente a este procedimiento",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados de la prestación",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    "Indique qué médico lo atendió",
    "¿Cuál otro médico?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Indique qué profesional lo atendió",
    "¿Cuál otro profesional?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Qué tipo de estudio de biopsia se le indicó?",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio",
    "¿Qué intención de radioterapia se le indicó?",
    "¿Qué tipo de radioterapia se le indicó?",
    'Indique número de ciclos en plan de tratamiento',
    'Indique número de ciclos efectivamente realizadas',
    'Indique la fecha de inicio del tratamiento',
    "Indique la fecha de término del tratamiento",
    "¿Hubo alguna interrupción en el tratamiento?",
    "¿Por qué se interrumpió el tratamiento?",
    "¿Qué tipo de quimioterapia se le indicó?",
    "En cuanto a las drogas usadas en tratamiento ¿Qué drogas se le indicó?",
    "Otra droga",
    'Indique la fecha de alta hospitalaria',
    "Indique el o los diagnósticos de alta hospitalaria (ver GRD del episodio)",
    "¿Qué tipo de braquiterapia se le indicó?",
    "Otro tipo de braquiterapia",
    "Indique qué tipo de catéter fue indicado",
    "Indique qué tipo de catéter fue instalado",
    "¿El catéter quedó operativo?"].index(x)])


# In[ ]:


# Define una lista de números únicos por cada prestación
prestacion_numbers = list(range(60, len(prestaciones) + 176))

# Crea un diccionario para mapear prestaciones y asignar el número que corresponda
prestacion_to_number = {prestacion: number for prestacion, number in zip(prestaciones, prestacion_numbers)}

# Agrega la nueva columna "Numero prestación"
df['Numero prestacion'] = df['Nombre Prestación'].map(prestacion_to_number)

# Reordena la posición de las variables
df = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas', 'Variable']]


# In[ ]:


# Crea una nueva columna "Nombre Variable Final" según el nombre de la variable, el número de prestación y el tipo de capacidad
df['Nombre Variable Final'] = df['Variable'] + 'cacu_' + df['Numero prestacion'].astype(str) + "_trat"


# In[ ]:


df


# ##### Comienza formato RedCap
# 
# - 1. Dejar solo las columnas que necesito: Nombre prestación, Pregunta y Nombre Variable Final
# - 2. Cambiar nombre al formato de redcap de las columnas que tengo
# - 3. Agregar columna "Section Header": título de cada prestación
# - 4. Agregar columna "Form Name" : nombre del formulario en redcap
# - 5. Agregar columna "Field Type" : Tipo de dato

# In[ ]:


#Dejar solo las columnas que necesito
df_cacu = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas','Nombre Variable Final']]

#Cambiar nombre de la variable

nombres_nuevos = {'Nombre Variable Final':'Variable / Field Name',
                 'Preguntas' : 'Field Label'}
df_cacu.rename(columns=nombres_nuevos, inplace=True)


# In[ ]:


# Crear columna Section 
df_cacu['Section Header'] = ''

# Asignar S.H. según el nombre de la prestación 
df_cacu.loc[df_cacu.groupby('Nombre Prestación').cumcount() == 0, 'Section Header'] = df['Nombre Prestación']


# In[ ]:


# Crear columna con el nombre del formulario 

df_cacu['Form Name'] = "formulario_tratamiento_cacu"
df_cacu["Field Note"] = ""


# In[ ]:


# Crear la columna 'Field Type' con valores por defecto 'text'
df_cacu['Field Type'] = 'text'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("indica_","realiza_","lugar_","lugar_exm_",
                                                               "inform_resul_","reagenda_","razon_prim_reag_",
                                                               "razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_",
                                                               "razon_quin_reag_","tipo_med_","tipo_espe_med_","n_reagenda_",
                                                               "toma_biop_","no_biop","tipo_biop_","tipo_molec_",
                                                               "tipo_espe_med_","reagenda_biop_","lugar_inf_exm_",
                                                               "tipo_prof_","int_radio_","tipo_radio_","interrup_trat_",
                                                               "pq_interrup_","tipo_quimio_","tipo_droga_",
                                                               "linea_droga_","tipo_braq_"


))

df_cacu.loc[condic, 'Field Type'] = 'dropdown'

# Crear la columna 'Choices, Calculations, OR Slider Labels'
df_cacu['Choices, Calculations, OR Slider Labels'] = ''

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('indica_','realiza_','inform_resul_','reagenda_','toma_biop_','interrup_trat_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Si | 2, No'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_exm_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Lab de la Red SSMSO  | 2,  Lab externo'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("razon_prim_reag_","razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_","razon_quin_reag_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se presentó | 2, Reagendamiento por temas administrativos (Ej: paro de funcionarios) | 3, Reagendamiento por rechazo del paciente | 4, Rechazo de interconsulta por Contralor | 5, Paciente no termina su tratamiento | 6, Paciente fallecido | 7, Paciente perdido (Ej: continuó su atención clínica en el extrasistema) | 8, Información no disponible'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("n_reagenda_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_med_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Médico de familia | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_prof_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Enfermera | 2, Matrona | 3, Kinesióloga| 4, Nutricionista | 5, Otra (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_biop_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Estudio histopatológico con técnicas histoquimicas especiales" | 2, Estudio histopatológico corriente de biopsia diferida(por cada órgano)" | 3, Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)" | 4, Estudio histopatológico con tinción corriente de biopsia diferida con estudio seriado (mínimo 10 muestras) de un órgano o parte de él (no incluye estudio con técnica habitual de otros órganos incluidos en la muestra) | 5, Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)'
                                 
# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("no_biop_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se encontró lesión | 2, Imposibilidad de tomar muestra | 3, Falta de insumos o RRHH | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("lugar_inf_exm_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_molec_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, P16 | 2, Estudios de receptores hormonales  | 3, PDL-1 | 4, Otro (Especificar)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_espe_med_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Cirujano General| 4, Internista | 5, Cirujano mama | 6, Ginecólogo Oncólogo | 7, Otro médico especialista (Especificar)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("int_radio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Curativa | 2, Paliativo | 3, No se especifica'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_braq_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Alta tasa (Cobalto o Iridio)| 2, Baja tasa (Cesio) | 3, No se especifíca'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("pq_interrup_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Mala respuesta  | 2, Intercurrencia (hospitalización por otra causa)  | 3, Toxicidad (mala tolerancia al tratamiento)  | 4, Presenta complicaciones  | 5, Problemas administrativos  | 6, No asiste  | 7, Fallecimiento'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_quimio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Adyuvante | 2, Neoadyuvante | 3, Paliativa'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_droga_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Cisplatino | 2, Paclitaxel | 3, Otra droga (Especifique)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_radio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Radiocirugía cerebral o corporal (SRS o SBRT)  | 2, Radioterapia guiada por imágenes (IGRT)  | 3, Radioterapia de intensidad modulada (IMRT) | 4, Radioterapia conformacional 3D (3D CRT) | 5, No se especifica'

# Actualizar la columna ''Text Validation Type OR Show Slider Number' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("fecha_"))
df_cacu.loc[condic, 'Text Validation Type OR Show Slider Number'] = 'date_dmy'


# In[ ]:


# Define the function to apply the correct branching logic
def generate_branching_logic(row):
    variable_name = row['Variable / Field Name']
    try:
        num_prest = int(row['Numero prestacion'])
    except (ValueError, TypeError):
        return ""
    if variable_name == f"fecha_indica_cacu_{num_prest}_trat":
        return f"[indica_cacu_{num_prest}_trat]=1"
    
    elif variable_name == f"realiza_cacu_{num_prest}_trat":
        return f"[indica_cacu_{num_prest}_trat]=1"
    
    elif variable_name == f"fecha_realiza_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]=1"
    
    elif variable_name == f"lugar_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]=1"
    
    elif variable_name == f"lugar_exm_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"fecha_envio_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"fecha_devol_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"inform_resul_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"fecha_resul_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [inform_resul_cacu_{num_prest}_trat]=1"
    
    elif variable_name == f"fecha_prox_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"reagenda_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]=1 or [realiza_cacu_{num_prest}_trat]=2"
    
    elif variable_name == f"n_reagenda_cacu_{num_prest}_trat":
        return f"[reagenda_cacu_{num_prest}_trat]=1"
    
    elif variable_name == f"fecha_prim_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=1"
    
    elif variable_name == f"razon_prim_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=1"
    
    elif variable_name == f"fecha_sec_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=2"
    
    elif variable_name == f"razon_sec_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=2"
    
    elif variable_name == f"fecha_ter_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=3"
    
    elif variable_name == f"razon_ter_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=3"
    
    elif variable_name == f"fecha_cuar_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=4"
    
    elif variable_name == f"razon_cuar_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=4"
    
    elif variable_name == f"fecha_quin_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=5"
    
    elif variable_name == f"razon_quin_reag_cacu_{num_prest}_trat":
        return f"[n_reagenda_cacu_{num_prest}_trat]>=5"
    
    elif variable_name == f"tipo_espe_med_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"

    elif variable_name == f"otro_esp_med_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [tipo_espe_med_cacu_{num_prest}_trat]=7"
    
    elif variable_name == f"tipo_med_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"

    elif variable_name == f"otro_med_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [tipo_med_cacu_{num_prest}_trat]=4"
                                                          
    elif variable_name == f"tipo_prof_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"

    elif variable_name == f"otro_prof_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [tipo_prof_cacu_{num_prest}_trat]=5"
    
    elif variable_name == f"lugar_inf_exm_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"toma_biop_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"no_biop_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [toma_biop_cacu_{num_prest}_trat]=2"
    
    elif variable_name == f"otro_no_biop_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [no_biop_cacu_{num_prest}_trat]=4"    
    
    elif variable_name == f"tipo_biop_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [toma_biop_cacu_{num_prest}_trat]=1"
    
    elif variable_name == f"tipo_molec_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"otro_molec_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [tipo_molec_cacu_{num_prest}_trat]=4"
    
    elif variable_name == f"tipo_droga_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"otra_droga_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1 and [tipo_droga_cacu_{num_prest}_trat]=3"

    elif variable_name == f"fecha_ini_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"n_ciclos_trat_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"n_ciclos_efec_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"fecha_ter_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"interrup_trat_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"pq_interrup_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"tipo_quimio_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"tipo_braq_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"fecha_alta_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"int_radio_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"tipo_radio_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"

    elif variable_name == f"diag_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"cateter_op_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"tipo_cateter_ind_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"tipo_ceteter_inst_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"
    
    elif variable_name == f"otro_braq_cacu_{num_prest}_trat":
        return f"[realiza_cacu_{num_prest}_trat]= 1"

    
        return ""
    
    # Apply the function to create the new column
df_cacu['Branching Logic (Show field only if...)'] = df_cacu.apply(generate_branching_logic, axis=1)


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_64_trat", "realiza_cacu_65_trat", "realiza_cacu_66_trat", 
    "realiza_cacu_67_trat", "realiza_cacu_68_trat", "realiza_cacu_69_trat"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_65_trat]=1 and [toma_biop_cacu_65_trat]=1"


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_83_trat", "realiza_cacu_84_trat", "realiza_cacu_85_trat", 
    "realiza_cacu_86_trat", "realiza_cacu_87_trat", "realiza_cacu_88_trat"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_82_trat]=1 and [toma_biop_cacu_82_trat]=1"


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_100_trat", "realiza_cacu_101_trat", "realiza_cacu_102_trat", 
    "realiza_cacu_103_trat", "realiza_cacu_104_trat", "realiza_cacu_105_trat"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_99_trat]=1 and [toma_biop_cacu_99_trat]=1"


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "indica_cacu_60_trat", 
    "indica_cacu_61_trat", 
    "indica_cacu_62_trat", 
    "indica_cacu_63_trat"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[diagnstico_arm_2][tipo_lesion_cacu_diag]=1"


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "indica_cacu_70_trat", 
    "indica_cacu_71_trat", 
    "indica_cacu_72_trat", 
    "indica_cacu_73_trat",
    "indica_cacu_74_trat", 
    "indica_cacu_75_trat", 
    "indica_cacu_76_trat", 
    "indica_cacu_77_trat",
    "indica_cacu_78_trat", 
    "indica_cacu_79_trat", 
    "indica_cacu_80_trat", 
    "indica_cacu_81_trat",
    "indica_cacu_82_trat",
    "indica_cacu_89_trat"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[diagnstico_arm_2][tipo_lesion_cacu_diag]=1"


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "indica_cacu_90_trat",
    "indica_cacu_91_trat", 
    "indica_cacu_92_trat", 
    "indica_cacu_93_trat", 
    "indica_cacu_94_trat", 
    "indica_cacu_95_trat", 
    "indica_cacu_96_trat",
    "indica_cacu_97_trat", 
    "indica_cacu_98_trat", 
    "indica_cacu_99_trat",
    "indica_cacu_100_trat",
    "indica_cacu_101_trat",
    "indica_cacu_102_trat",
    "indica_cacu_103_trat",
    "indica_cacu_104_trat",
    "indica_cacu_105_trat",
    "indica_cacu_106_trat",
    "indica_cacu_107_trat",
    "indica_cacu_108_trat",
    "indica_cacu_109_trat",
    "indica_cacu_110_trat",
    "indica_cacu_111_trat",
    "indica_cacu_112_trat",
    "indica_cacu_113_trat", 
    "indica_cacu_114_trat", 
    "indica_cacu_115_trat", 
    "indica_cacu_116_trat",
    "indica_cacu_117_trat", 
    "indica_cacu_118_trat", 
    "indica_cacu_119_trat", 
    "indica_cacu_120_trat",
    "indica_cacu_121_trat", 
    "indica_cacu_122_trat", 
    "indica_cacu_123_trat", 
    "indica_cacu_124_trat",
    "indica_cacu_125_trat",
    "indica_cacu_126_trat", 
    "indica_cacu_127_trat", 
    "indica_cacu_128_trat",
    "indica_cacu_129_trat",
    "indica_cacu_130_trat",
    "indica_cacu_131_trat", 
    "indica_cacu_132_trat"
    
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[diagnstico_arm_2][tipo_lesion_cacu_diag]=2"


# In[ ]:


# Define the new columns with empty values
new_columns = {
    'Text Validation Min': '',
    'Text Validation Max': '',
    'Identifier?': '',
    'Required Field?': '',
    'Custom Alignment': '',
    'Question Number (surveys only)': '',
    'Matrix Group Name': '',
    'Matrix Ranking?': '',
    'Field Annotation': ''
}

# Add these new columns to the existing dataframe with default empty values
for column, value in new_columns.items():
    df_cacu[column] = value

# Definir el orden de las variables en el df

orden_deseado = ['Variable / Field Name', 'Form Name', 'Section Header', 'Field Type',
       'Field Label', 'Choices, Calculations, OR Slider Labels', 'Field Note',
       'Text Validation Type OR Show Slider Number', 'Text Validation Min',
       'Text Validation Max', 'Identifier?',
       'Branching Logic (Show field only if...)', 'Required Field?',
       'Custom Alignment', 'Question Number (surveys only)',
       'Matrix Group Name', 'Matrix Ranking?', 'Field Annotation']

#Reordenar
df_cacu = df_cacu[orden_deseado]


# In[ ]:


df_cacu.to_excel("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/CaCu_trat.xlsx")

df_cacu.to_csv("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv", index=False)


# In[ ]:


import zipfile
import os

# Ruta del archivo que quieres comprimir
archivo_csv = "C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv"

# Ruta donde se guardará el archivo comprimido
ruta_salida_zip = r"C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/Cacu_trat.zip"

# Crear un archivo ZIP y agregar el archivo CSV
with zipfile.ZipFile(ruta_salida_zip, 'w') as archivo_zip:
    archivo_zip.write(archivo_csv, os.path.basename(archivo_csv))

print(f"Archivo comprimido guardado en: {ruta_salida_zip}")


# In[ ]:





# ### Seguimiento
# 
# ### Cacu Invasor
# - "148-Visita por médico interconsultor a enfermo hospitalizado (o en junta médica c/u)",
# - "149-Consulta integral de epecialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología",
# - "150-Consulta o control por enfermera,matrona o nutricionista",
# - "151-Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más)",
# - "152-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
# - "153-Urocultivo, recuento de colonias y antibiograma (cualquier técnica)(incluye toma de orina aséptica)(no incluye recolector pediátrico)",
# - "154-Tórax (fronta y lateral)(incluye fluoroscopía)(2  proy. panorámicas)(2 exp.)",
# - "155-Abdomen (hígado, vías y vesícula biliar, páncreas, bazo, suprarrenales y riñones) (40 cortes 8-10 mm)",
# - "156-Pelvis (28 cortes, 8-10 mm)",
# - "157-Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)",
# - "158-Citodiagnóstico corriente, exfoliativa(Papanicolau y similares)(por cada órgano)",
# - "159-Colposcopía",
# - "160-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
# - "161-Estudio histopatológico con técnicas histoquimicas especiales",
# - "162-Estudio histopatológico corriente de biopsia diferida",
# - "163-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
# - "164-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
# - "165-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas(por cada órgano)(no incluye biopsia diferida)",
# - "166-Estudios moleculares específicos",
# 
# 
# ### Cacu Pre-Invasor
# 
# - "137-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología",
# - "138-Consulta o control por enfermera, matrona o nutricionista",
# - "139-Citodiagnóstico corriente, exfoliativa (Papanicolau y similares) (por cada órgano)",
# - "140-Colposcopía",
# - "141-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
# - "142-Estudio histopatológico con técnicas histoquimicas especiales",
# - "143-Estudio histopatológico corriente de biopsia diferida",
# - "144-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
# - "145-Estudio histopatológico con con tinción corriente de biopsia diferida con estudio seriado",
# - "146-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
# - "147-Estudios moleculares específicos"
# 

# In[ ]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import re


# In[ ]:


prestaciones=[
    "147-Visita por médico interconsultor (o en junta médica c/u) a enfermo hospitalizado"
             
]
# Agregar preguntas
preguntas = [
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Se le informó el resultado de la junta médica oncológica?",
    "Indique la fecha en que se le informó el resultado de la junta médica",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados de la prestación",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    ]
    
# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "137-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología",
    "148-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología"
]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df1 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "138-Consulta o control por enfermera, matrona o nutricionista",
    "149-Consulta o control por enfermera, matrona o nutricionista"
    
]

# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué profesional lo atendió",
    "¿Cuál otro profesional?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df2 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "150-Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más)" 
]
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique la fecha de alta hospitalaria",
    "Indique el o los diagnósticos de alta hospitalaria (ver GRD del episodio)",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df3 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
"151-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
"152-Urocultivo, recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)",
"153-Tórax (frontal y lateral) (incluye fluoroscopía) (2 proy. panorámicas) (2 exp.)",
"154-Abdomen (hígado, vías y vesícula biliar, páncreas, bazo, suprarrenales y riñones) (40 cortes 8-10 mm)",
"155-Pelvis",
"156-Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)"

]

    
    
# Agregar preguntas
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df4 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = [
    "139-Citodiagnóstico corriente, exfoliativa (Papanicolau y similares) (por cada órgano)",
    "157-Citodiagnóstico corriente, exfoliativa (Papanicolau y similares) (por cada órgano)"

    ]


# Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df5 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones = ["140-Colposcopía",
                "158-Colposcopía"
               ]

#Agregar preguntas
preguntas = [ 
    
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
]

# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df6 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
"141-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
"142-Estudio histopatológico con técnicas histoquimicas especiales",
"143-Estudio histopatológico corriente de biopsia diferida con estudio seriado",
"144-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"145-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano)(no incluye biopsia diferida)",
"159-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
"160-Estudio histopatológico con técnicas histoquimicas especiales",
"161-Estudio histopatológico corriente de biopsia diferida con estudio seriado",
"162-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
"163-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)"
   

]

# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen"
    
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df7 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


prestaciones=[
    "146-Estudios moleculares específicos",
    "164-Estudios moleculares específicos"
    
]

# Agregar preguntas
preguntas = [ 
#    "¿Se le indicó esta prestación?",
#    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Dónde se realizó el informe del exámen?",
    "¿Se le informó el resultado del exámen?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen"
    
    
    
]



# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df8 = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


# Agregar una columna con el número de la prestación
df['Numero Prestación'] = df['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df1['Numero Prestación'] = df1['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df2['Numero Prestación'] = df2['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df3['Numero Prestación'] = df3['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df4['Numero Prestación'] = df4['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df5['Numero Prestación'] = df5['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df6['Numero Prestación'] = df6['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df7['Numero Prestación'] = df7['Nombre Prestación'].str.extract(r'(\d+)').astype(int)
df8['Numero Prestación'] = df8['Nombre Prestación'].str.extract(r'(\d+)').astype(int)


# Combinar los DataFrames
df_combined = pd.concat([df,df1,df2,df3,df4,df5,df6,df7,df8], ignore_index=True)


# In[ ]:


# Ordenar el DataFrame por la columna 'Numero Prestación' y 'Orden Pregunta'
df_combined_sorted = df_combined.sort_values(by=['Numero Prestación', 'Orden Pregunta']).reset_index(drop=True)

df = df_combined_sorted


# In[ ]:


prestaciones=[
    "137-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología",
    "138-Consulta o control por enfermera, matrona o nutricionista",
    "139-Citodiagnóstico corriente, exfoliativa (Papanicolau y similares) (por cada órgano)",
    "140-Colposcopía",
    "141-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
    "142-Estudio histopatológico con técnicas histoquimicas especiales",
    "143-Estudio histopatológico corriente de biopsia diferida con estudio seriado",
    "144-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
    "145-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano)(no incluye biopsia diferida)",
    "146-Estudios moleculares específicos",
    "147-Visita por médico interconsultor (o en junta médica c/u) a enfermo hospitalizado",
    "148-Consulta integral de especialidades en Medicina Interna y Subespecialidades, Oftalmología, Neurología, Oncología",
    "149-Consulta o control por enfermera, matrona o nutricionista",
    "150-Día cama hospitalización integral medicina, cirugía, pediatría, obstetricia-ginecología y especialidades (sala 3 camas o más)",
    "151-Hemograma (incluye recuentos de leucocitos y eritrocitos, hemoglobina, hematocrito, fórmula leucocitaria, características de los elementos figurados y velocidad de eritrosedimentación)",
    "152-Urocultivo, recuento de colonias y antibiograma (cualquier técnica) (incluye toma de orina aséptica) (no incluye recolector pediátrico)",
    "153-Tórax (frontal y lateral) (incluye fluoroscopía) (2 proy. panorámicas) (2 exp.)",
    "154-Abdomen (hígado, vías y vesícula biliar, páncreas, bazo, suprarrenales y riñones) (40 cortes 8-10 mm)",
    "155-Pelvis",
    "156-Transfusión en adulto (atención ambulatoria, atención cerrada siempre que la administración sea controlada por profesional especialista, tecnólogo médico o médico responsable)",
    "157-Citodiagnóstico corriente, exfoliativa (Papanicolau y similares) (por cada órgano)",
    "158-Colposcopía",
    "159-Estudio histopatológico corriente de biopsia diferida (por cada órgano)",
    "160-Estudio histopatológico con técnicas histoquimicas especiales",
    "161-Estudio histopatológico corriente de biopsia diferida con estudio seriado",
    "162-Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)",
    "163-Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)",
    "164-Estudios moleculares específicos"
]


# In[ ]:


# Definir las variables de cada pregunta
variables = [
    "indica_",
    "fecha_indica_",
    "realiza_",
    "fecha_realiza_",
    "lugar_",
    "lugar_exm_",
    "lugar_inf_exm_",
    "fecha_envio_",
    "fecha_devol_",
    "inform_resul_",
    "inform_resul_",
    "inform_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_prox_",
    "fecha_prox_",
    "fecha_prox_",
    "fecha_prox_",
    "reagenda_",
    "n_reagenda_",
    "fecha_prim_reag_",
    "razon_prim_reag_",
    "fecha_sec_reag_",
    "razon_sec_reag_",
    "fecha_ter_reag_",
    "razon_ter_reag_",
    "fecha_cuar_reag_",
    "razon_cuar_reag_",
    "fecha_quin_reag_",
    "razon_quin_reag_",
    "tipo_med_",
    "otro_med_",
    "tipo_espe_med_",
    "otro_esp_med_",
    "tipo_prof_",
    "otro_prof_",
    "toma_biop_",
    "no_biop_",
    "otro_no_biop_",
    "tipo_biop_",
    "tipo_molec_",
    "otro_molec_",
    "int_radio_",
    "tipo_radio_",
    "n_ciclos_trat_",
    "n_ciclos_efec_",
    "fecha_ini_",
    "fecha_ter_",
    "interrup_trat_",
    "pq_interrup_",
    "tipo_quimio_",
    "tipo_droga_",
    "otra_droga_",
    "fecha_alta_",
    "diag_",
    "tipo_braq_",
    "otro_braq_",
    "tipo_cateter_ind_",
    "tipo_ceteter_inst_",
    "cateter_op_"]


# Actualizar las variables por cada pregunta

df['Variable'] = df['Preguntas'].apply(lambda x: variables[[
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "¿Dónde se realizó el informe del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "¿Se le informó el resultado del procedimiento?",
    "¿Se le informó el resultado de la junta médica oncológica?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado de la junta médica",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Indique la fecha en que se le realizó la prestación siguiente a este procedimiento",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados de la prestación",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    "Indique qué médico lo atendió",
    "¿Cuál otro médico?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Indique qué profesional lo atendió",
    "¿Cuál otro profesional?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Qué tipo de estudio de biopsia se le indicó?",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio",
    "¿Qué intención de radioterapia se le indicó?",
    "¿Qué tipo de radioterapia se le indicó?",
    'Indique número de ciclos en plan de tratamiento',
    'Indique número de ciclos efectivamente realizadas',
    'Indique la fecha de inicio del tratamiento',
    "Indique la fecha de término del tratamiento",
    "¿Hubo alguna interrupción en el tratamiento?",
    "¿Por qué se interrumpió el tratamiento?",
    "¿Qué tipo de quimioterapia se le indicó?",
    "En cuanto a las drogas usadas en tratamiento ¿Qué drogas se le indicó?",
    "Otra droga",
    'Indique la fecha de alta hospitalaria',
    "Indique el o los diagnósticos de alta hospitalaria (ver GRD del episodio)",
    "¿Qué tipo de braquiterapia se le indicó?",
    "Otro tipo de braquiterapia",
    "Indique qué tipo de catéter fue indicado",
    "Indique qué tipo de catéter fue instalado",
    "¿El catéter quedó operativo?"].index(x)])


# In[ ]:


# Define una lista de números únicos por cada prestación
prestacion_numbers = list(range(137, len(prestaciones) + 164))

# Crea un diccionario para mapear prestaciones y asignar el número que corresponda
prestacion_to_number = {prestacion: number for prestacion, number in zip(prestaciones, prestacion_numbers)}

# Agrega la nueva columna "Numero prestación"
df['Numero prestacion'] = df['Nombre Prestación'].map(prestacion_to_number)

# Reordena la posición de las variables
df = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas', 'Variable']]


# In[ ]:


# Crea una nueva columna "Nombre Variable Final" según el nombre de la variable, el número de prestación y el tipo de capacidad
df['Nombre Variable Final'] = df['Variable'] + 'cacu_' + df['Numero prestacion'].astype(str) + "_seg"


# In[ ]:


df


# ##### Comienza formato RedCap
# 
# - 1. Dejar solo las columnas que necesito: Nombre prestación, Pregunta y Nombre Variable Final
# - 2. Cambiar nombre al formato de redcap de las columnas que tengo
# - 3. Agregar columna "Section Header": título de cada prestación
# - 4. Agregar columna "Form Name" : nombre del formulario en redcap
# - 5. Agregar columna "Field Type" : Tipo de dato
# 

# In[ ]:


#Dejar solo las columnas que necesito
df_cacu = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas','Nombre Variable Final']]

#Cambiar nombre de la variable

nombres_nuevos = {'Nombre Variable Final':'Variable / Field Name',
                 'Preguntas' : 'Field Label'}
df_cacu.rename(columns=nombres_nuevos, inplace=True)


# In[ ]:


# Crear columna Section 
df_cacu['Section Header'] = ''

# Asignar S.H. según el nombre de la prestación 
df_cacu.loc[df_cacu.groupby('Nombre Prestación').cumcount() == 0, 'Section Header'] = df['Nombre Prestación']


# In[ ]:


# Crear columna con el nombre del formulario 

df_cacu['Form Name'] = "formulario_seguimiento_cacu"
df_cacu["Field Note"] = ""

# Crear la columna 'Field Type' con valores por defecto 'text'
df_cacu['Field Type'] = 'text'


# In[ ]:


# Crear la columna 'Field Type' con valores por defecto 'text'
df_cacu['Field Type'] = 'text'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("indica_","realiza_","lugar_","lugar_exm_",
                                                               "inform_resul_","reagenda_","razon_prim_reag_",
                                                               "razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_",
                                                               "razon_quin_reag_","tipo_med_","tipo_espe_med_","n_reagenda_",
                                                               "toma_biop_","no_biop","tipo_biop_","tipo_molec_",
                                                               "tipo_espe_med_","reagenda_biop_","lugar_inf_exm_",
                                                               "tipo_prof_","int_radio_","tipo_radio_","interrup_trat_",
                                                               "pq_interrup_","tipo_quimio_","tipo_droga_",
                                                               "linea_droga_","tipo_braq_"


))

df_cacu.loc[condic, 'Field Type'] = 'dropdown'

# Crear la columna 'Choices, Calculations, OR Slider Labels'
df_cacu['Choices, Calculations, OR Slider Labels'] = ''

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('indica_','realiza_','inform_resul_','reagenda_','toma_biop_','interrup_trat_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Si | 2, No'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_exm_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Lab de la Red SSMSO  | 2,  Lab externo'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("razon_prim_reag_","razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_","razon_quin_reag_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se presentó | 2, Reagendamiento por temas administrativos (Ej: paro de funcionarios) | 3, Reagendamiento por rechazo del paciente | 4, Rechazo de interconsulta por Contralor | 5, Paciente no termina su tratamiento | 6, Paciente fallecido | 7, Paciente perdido (Ej: continuó su atención clínica en el extrasistema) | 8, Información no disponible'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("n_reagenda_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_med_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Médico de familia | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_prof_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Enfermera | 2, Matrona | 3, Kinesióloga| 4, Nutricionista | 5, Otra (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_biop_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Estudio histopatológico con técnicas histoquimicas especiales" | 2, Estudio histopatológico corriente de biopsia diferida(por cada órgano)" | 3, Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)" | 4, Estudio histopatológico con tinción corriente de biopsia diferida con estudio seriado (mínimo 10 muestras) de un órgano o parte de él (no incluye estudio con técnica habitual de otros órganos incluidos en la muestra) | 5, Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)'
                                 
# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("no_biop_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se encontró lesión | 2, Imposibilidad de tomar muestra | 3, Falta de insumos o RRHH | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("lugar_inf_exm_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_molec_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, P16 | 2, Estudios de receptores hormonales  | 3, PDL-1 | 4, Otro (Especificar)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_espe_med_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Cirujano General| 4, Internista | 5, Cirujano mama | 6, Ginecólogo Oncólogo | 7, Otro médico especialista (Especificar)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("int_radio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Curativa | 2, Paliativo | 3, No se especifica'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_braq_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Alta tasa (Cobalto o Iridio)| 2, Baja tasa (Cesio) | 3, No se especifíca'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("pq_interrup_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Mala respuesta  | 2, Intercurrencia (hospitalización por otra causa)  | 3, Toxicidad (mala tolerancia al tratamiento)  | 4, Presenta complicaciones  | 5, Problemas administrativos  | 6, No asiste  | 7, Fallecimiento'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_quimio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Adyuvante | 2, Neoadyuvante | 3, Paliativa'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_droga_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Cisplatino | 2, Paclitaxel | 3, Otra droga (Especifique)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_radio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Radiocirugía cerebral o corporal (SRS o SBRT)  | 2, Radioterapia guiada por imágenes (IGRT)  | 3, Radioterapia de intensidad modulada (IMRT) | 4, Radioterapia conformacional 3D (3D CRT) | 5, No se especifica'

# Actualizar la columna ''Text Validation Type OR Show Slider Number' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("fecha_"))
df_cacu.loc[condic, 'Text Validation Type OR Show Slider Number'] = 'date_dmy'


# In[ ]:


# Define the function to apply the correct branching logic
def generate_branching_logic(row):
    variable_name = row['Variable / Field Name']
    try:
        num_prest = int(row['Numero prestacion'])
    except (ValueError, TypeError):
        return ""
    if variable_name == f"fecha_indica_cacu_{num_prest}_seg":
        return f"[indica_cacu_{num_prest}_seg]=1"
    
    elif variable_name == f"realiza_cacu_{num_prest}_seg":
        return f"[indica_cacu_{num_prest}_seg]=1"
    
    elif variable_name == f"fecha_realiza_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]=1"
    
    elif variable_name == f"lugar_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]=1"
    
    elif variable_name == f"lugar_exm_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"fecha_envio_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"fecha_devol_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"inform_resul_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"fecha_resul_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [inform_resul_cacu_{num_prest}_seg]=1"
    
    elif variable_name == f"fecha_prox_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"reagenda_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]=1 or [realiza_cacu_{num_prest}_seg]=2"
    
    elif variable_name == f"n_reagenda_cacu_{num_prest}_seg":
        return f"[reagenda_cacu_{num_prest}_seg]=1"
    
    elif variable_name == f"fecha_prim_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=1"
    
    elif variable_name == f"razon_prim_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=1"
    
    elif variable_name == f"fecha_sec_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=2"
    
    elif variable_name == f"razon_sec_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=2"
    
    elif variable_name == f"fecha_ter_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=3"
    
    elif variable_name == f"razon_ter_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=3"
    
    elif variable_name == f"fecha_cuar_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=4"
    
    elif variable_name == f"razon_cuar_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=4"
    
    elif variable_name == f"fecha_quin_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=5"
    
    elif variable_name == f"razon_quin_reag_cacu_{num_prest}_seg":
        return f"[n_reagenda_cacu_{num_prest}_seg]>=5"
    
    elif variable_name == f"tipo_espe_med_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"

    elif variable_name == f"otro_esp_med_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [tipo_espe_med_cacu_{num_prest}_seg]=7"
    
    elif variable_name == f"tipo_med_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"

    elif variable_name == f"otro_med_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [tipo_med_cacu_{num_prest}_seg]=4"
                                                          
    elif variable_name == f"tipo_prof_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"

    elif variable_name == f"otro_prof_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [tipo_prof_cacu_{num_prest}_seg]=5"
    
    elif variable_name == f"lugar_inf_exm_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"toma_biop_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"no_biop_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [toma_biop_cacu_{num_prest}_seg]=2"
    
    elif variable_name == f"otro_no_biop_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [no_biop_cacu_{num_prest}_seg]=4"    
    
    elif variable_name == f"tipo_biop_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [toma_biop_cacu_{num_prest}_seg]=1"
    
    elif variable_name == f"tipo_molec_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"otro_molec_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [tipo_molec_cacu_{num_prest}_seg]=4"
    
    elif variable_name == f"tipo_droga_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"otra_droga_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1 and [tipo_droga_cacu_{num_prest}_seg]=3"

    elif variable_name == f"fecha_ini_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"n_ciclos_seg_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"n_ciclos_efec_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"fecha_ter_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"interrup_trat_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"pq_interrup_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"tipo_quimio_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"tipo_braq_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"fecha_alta_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"int_radio_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"tipo_radio_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"

    elif variable_name == f"diag_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"cateter_op_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"tipo_cateter_ind_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"tipo_ceteter_inst_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"
    
    elif variable_name == f"otro_braq_cacu_{num_prest}_seg":
        return f"[realiza_cacu_{num_prest}_seg]= 1"

    
        return ""
    
    # Apply the function to create the new column
df_cacu['Branching Logic (Show field only if...)'] = df_cacu.apply(generate_branching_logic, axis=1)


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_141_seg", "realiza_cacu_142_seg", "realiza_cacu_143_seg", 
    "realiza_cacu_144_seg", "realiza_cacu_145_seg", "realiza_cacu_146_seg"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_140_seg]=1 and [toma_biop_cacu_140_seg]=1"


# Lista de nombres completos para verificar
nombres_completos = [
    
    "realiza_cacu_159_seg", "realiza_cacu_160_seg", "realiza_cacu_161_seg", 
    "realiza_cacu_162_seg", "realiza_cacu_163_seg", "realiza_cacu_164_seg"
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[realiza_cacu_158_seg]=1 and [toma_biop_cacu_158_seg]=1"


# In[ ]:


# Lista de nombres completos para verificar
nombres_completos = [
    
    "indica_cacu_137_seg", 
    "indica_cacu_138_seg", 
    "indica_cacu_139_seg",
    "indica_cacu_140_seg",
    
    
]

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[diagnstico_arm_2][resul_biop_cacu_diag]=2"


# Lista de nombres completos para verificar
nombres_completos = [
    
    "indica_cacu_147_seg",
    "indica_cacu_148_seg",
    "indica_cacu_149_seg",
    "indica_cacu_150_seg",
    "indica_cacu_151_seg",
    "indica_cacu_152_seg",
    "indica_cacu_153_seg",
    "indica_cacu_154_seg",
    "indica_cacu_155_seg",
    "indica_cacu_156_seg",
    "indica_cacu_157_seg",
    "indica_cacu_158_seg",
    "indica_cacu_159_seg",
    "indica_cacu_160_seg",
    "indica_cacu_161_seg",
    "indica_cacu_162_seg",
    "indica_cacu_163_seg",
    "indica_cacu_164_seg"
    
]


# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].isin(nombres_completos)
df_cacu.loc[condic,'Branching Logic (Show field only if...)'] = "[diagnstico_arm_2][resul_biop_cacu_diag]=1"


# In[ ]:


df_cacu


# In[ ]:


# Define the new columns with empty values
new_columns = {
    'Text Validation Min': '',
    'Text Validation Max': '',
    'Identifier?': '',
    'Required Field?': '',
    'Custom Alignment': '',
    'Question Number (surveys only)': '',
    'Matrix Group Name': '',
    'Matrix Ranking?': '',
    'Field Annotation': ''
}

# Add these new columns to the existing dataframe with default empty values
for column, value in new_columns.items():
    df_cacu[column] = value

# Definir el orden de las variables en el df

orden_deseado = ['Variable / Field Name', 'Form Name', 'Section Header', 'Field Type',
       'Field Label', 'Choices, Calculations, OR Slider Labels', 'Field Note',
       'Text Validation Type OR Show Slider Number', 'Text Validation Min',
       'Text Validation Max', 'Identifier?',
       'Branching Logic (Show field only if...)', 'Required Field?',
       'Custom Alignment', 'Question Number (surveys only)',
       'Matrix Group Name', 'Matrix Ranking?', 'Field Annotation']

#Reordenar
df_cacu = df_cacu[orden_deseado]



# In[ ]:


df_cacu.to_excel("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/CaCu_seg.xlsx")

df_cacu.to_csv("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv", index=False)

import zipfile
import os

# Ruta del archivo que quieres comprimir
archivo_csv = "C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv"

# Ruta donde se guardará el archivo comprimido
ruta_salida_zip = r"C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/Cacu_seg.zip"

# Crear un archivo ZIP y agregar el archivo CSV
with zipfile.ZipFile(ruta_salida_zip, 'w') as archivo_zip:
    archivo_zip.write(archivo_csv, os.path.basename(archivo_csv))

print(f"Archivo comprimido guardado en: {ruta_salida_zip}")


# ### Rehabilitación

# - 165-Capacitación y apoyo para cuidadores y familias
# - 166-Consejería educacional, entrenamiento y soporte
# - 167-Consejería vocacional, entrenamiento y soporte
# - 168-Educación, asesoramiento y apoyo para un estilo de vida saludable y la autogestión de la condición de salud
# - 169-Ejercicios de fortalecimiento muscular
# - 170-Ejercicios de piso pélvico
# - 171-Ejercicios de rango de movimiento
# - 172-Ejercicios de relajación
# - 173-Entrenamiento actividades de la vida diaria
# - 174-Entrenamiento cognitivo
# - 175-Entrenamiento del equilibrio
# - 176-Entrenamiento físico
# - 177-Entrenamiento movilidad
# - 178-Estimulación nerviosa eléctrica transcutánea (TENS)
# - 179-Intervenciones centradas en la participación
# - 180-Modificación de ambiente del hogar
# - 181-Provisión y capacitación en el uso de herramientas de apoyo para la movilidad
# - 182-Provisión y capacitación en el uso de productos de asistencia para el autocuidado
# - 183-Técnicas de tejidos blandos
# - 184-Terapia descongestiva completa
# - 185-Terapia psicológica
# - 186-Termoterapia
# 

# In[ ]:


prestaciones = [
    "165-Capacitación y apoyo para cuidadores y familias",
    "166-Consejería educacional, entrenamiento y soporte",
    "167-Consejería vocacional, entrenamiento y soporte",
    "168-Educación, asesoramiento y apoyo para un estilo de vida saludable y la autogestión de la condición de salud",
    "169-Ejercicios de fortalecimiento muscular",
    "170-Ejercicios de piso pélvico",
    "171-Ejercicios de rango de movimiento",
    "172-Ejercicios de relajación",
    "173-Entrenamiento actividades de la vida diaria",
    "174-Entrenamiento cognitivo",
    "175-Entrenamiento del equilibrio",
    "176-Entrenamiento físico",
    "177-Entrenamiento movilidad",
    "178-Estimulación nerviosa eléctrica transcutánea (TENS)",
    "179-Intervenciones centradas en la participación",
    "180-Modificación de ambiente del hogar",
    "181-Provisión y capacitación en el uso de herramientas de apoyo para la movilidad",
    "182-Provisión y capacitación en el uso de productos de asistencia para el autocuidado",
    "183-Técnicas de tejidos blandos",
    "184-Terapia descongestiva completa",
    "185-Terapia psicológica",
    "186-Termoterapia"]
   

# Agregar preguntas
preguntas = [ 
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "Indique qué profesional lo atendió",
    "¿Cuál otro profesión?",
    "Indique la fecha de inicio de la terapia",
    "Indique la fecha de término de la terapia",
    "Indique el número de sesiones en plan de tratamiento",
    "Indique el número de sesiones efectivamente realizadas",
    "¿Hubo alguna interrupción en el tratamiento?",
    "¿Por qué se interrumpió el tratamiento?",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?"
    
    
    
    
]


# Crear DF
rows_1 = []
for prestacion in prestaciones:
    for idx, pregunta in enumerate(preguntas):
        rows_1.append([prestacion, pregunta, idx])

df = pd.DataFrame(rows_1, columns=["Nombre Prestación", "Preguntas", "Orden Pregunta"])


# In[ ]:


# Definir las variables de cada pregunta
variables = [
    "indica_",
    "fecha_indica_",
    "realiza_",
    "fecha_realiza_",
    "lugar_",
    "lugar_exm_",
    "lugar_inf_exm_",
    "fecha_envio_",
    "fecha_devol_",
    "inform_resul_",
    "inform_resul_",
    "inform_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_resul_",
    "fecha_prox_",
    "fecha_prox_",
    "fecha_prox_",
    "fecha_prox_",
    "reagenda_",
    "n_reagenda_",
    "fecha_prim_reag_",
    "razon_prim_reag_",
    "fecha_sec_reag_",
    "razon_sec_reag_",
    "fecha_ter_reag_",
    "razon_ter_reag_",
    "fecha_cuar_reag_",
    "razon_cuar_reag_",
    "fecha_quin_reag_",
    "razon_quin_reag_",
    "tipo_med_",
    "otro_med_",
    "tipo_espe_med_",
    "otro_esp_med_",
    "tipo_prof_",
    "otro_prof_",
    "toma_biop_",
    "no_biop_",
    "otro_no_biop_",
    "tipo_biop_",
    "tipo_molec_",
    "otro_molec_",
    "int_radio_",
    "tipo_radio_",
    "n_ciclos_trat_",
    "n_ciclos_efec_",
    "n_ciclos_trat_",
    "n_ciclos_efec_",
    "fecha_ini_",
    "fecha_ini_",
    "fecha_ter_",
    "fecha_ter_",
    "interrup_trat_",
    "pq_interrup_",
    "tipo_quimio_",
    "tipo_droga_",
    "otra_droga_",
    "fecha_alta_",
    "diag_",
    "tipo_braq_",
    "otro_braq_",
    "tipo_cateter_ind_",
    "tipo_ceteter_inst_",
    "cateter_op_"]


# Actualizar las variables por cada pregunta

df['Variable'] = df['Preguntas'].apply(lambda x: variables[[
    "¿Se le indicó esta prestación?",
    "Indique la fecha en que se le indicó esta prestación",
    "¿Se realizó esta prestación?",
    "Indique la fecha en que se le realizó esta prestación",
    "¿Dónde se realizó esta prestación?",
    "¿Dónde se realizó la lectura del exámen?",
    "¿Dónde se realizó el informe del exámen?",
    "Indique la fecha de envío del exámen para lectura",
    "Indique la fecha de devolución del resultado del exámen",
    "¿Se le informó el resultado del exámen?",
    "¿Se le informó el resultado del procedimiento?",
    "¿Se le informó el resultado de la junta médica oncológica?",
    "Indique la fecha en que se le informó el resultado del exámen",
    "Indique la fecha en que se le informó el resultado del procedimiento?",
    "Indique la fecha en que se le informó el resultado de la junta médica",
    "Indique la fecha en que se le realizó la consulta de control siguiente al informe de resultados del examen",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados del procedimiento",
    "Indique la fecha en que se le realizó la prestación siguiente a este procedimiento",
    "Indique la fecha en que se le realizó la prestación siguiente al informe de resultados de la prestación",
    "Revisar en sistema si existen reagendamientos. ¿Se reagendó esta prestación?",
    "¿Cuántas veces se reagendó esta prestación?",
    "Fecha de primer reagendamiento",
    "¿Por qué se reagendó esta prestación?",
    "Fecha de segundo reagendamiento",
    "¿Por qué se reagendó por segunda vez esta prestación?",
    "Fecha de tercer reagendamiento",
    "¿Por qué se reagendó por tercera vez esta prestación?",
    "Fecha de cuarto reagendamiento",
    "¿Por qué se reagendó por cuarta vez esta prestación?",
    "Fecha de quinto reagendamiento",
    "¿Por qué se reagendó por quinta vez esta prestación?",
    "Indique qué médico lo atendió",
    "¿Cuál otro médico?",
    "Indique qué médico especialista lo atendió",
    "¿Cuál otro médico especialista?",
    "Indique qué profesional lo atendió",
    "¿Cuál otro profesión?",
    "¿Se realizó una toma de muestra para biopsia?",
    "¿Por qué no se realizó la toma de muestra?",
    "Otro motivo",
    "¿Qué tipo de estudio de biopsia se le indicó?",
    "¿Qué tipo de estudios moleculares específicos?",
    "Otro estudio",
    "¿Qué intención de radioterapia se le indicó?",
    "¿Qué tipo de radioterapia se le indicó?",
    'Indique número de ciclos en plan de tratamiento',
    'Indique número de ciclos efectivamente realizadas',
    "Indique el número de sesiones en plan de tratamiento",
    "Indique el número de sesiones efectivamente realizadas",
    'Indique la fecha de inicio de la terapia',
    'Indique la fecha de inicio del tratamiento',
    "Indique la fecha de término del tratamiento",
    "Indique la fecha de término de la terapia",
    "¿Hubo alguna interrupción en el tratamiento?",
    "¿Por qué se interrumpió el tratamiento?",
    "¿Qué tipo de quimioterapia se le indicó?",
    "En cuanto a las drogas usadas en tratamiento ¿Qué drogas se le indicó?",
    "Otra droga",
    'Indique la fecha de alta hospitalaria',
    "Indique el o los diagnósticos de alta hospitalaria (ver GRD del episodio)",
    "¿Qué tipo de braquiterapia se le indicó?",
    "Otro tipo de braquiterapia",
    "Indique qué tipo de catéter fue indicado",
    "Indique qué tipo de catéter fue instalado",
    "¿El catéter quedó operativo?"].index(x)])


# In[ ]:


# Define una lista de números únicos por cada prestación
prestacion_numbers = list(range(165, len(prestaciones) + 186))

# Crea un diccionario para mapear prestaciones y asignar el número que corresponda
prestacion_to_number = {prestacion: number for prestacion, number in zip(prestaciones, prestacion_numbers)}


# In[ ]:


# Agrega la nueva columna "Numero prestación"
df['Numero prestacion'] = df['Nombre Prestación'].map(prestacion_to_number)

# Reordena la posición de las variables
df = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas', 'Variable']]


# In[ ]:


# Crea una nueva columna "Nombre Variable Final" según el nombre de la variable, el número de prestación y el tipo de capacidad
df['Nombre Variable Final'] = df['Variable'] + 'cacu_' + df['Numero prestacion'].astype(str) + "_rehab"


# In[ ]:


df


# ##### Comienza formato RedCap
# 
# - 1. Dejar solo las columnas que necesito: Nombre prestación, Pregunta y Nombre Variable Final
# - 2. Cambiar nombre al formato de redcap de las columnas que tengo
# - 3. Agregar columna "Section Header": título de cada prestación
# - 4. Agregar columna "Form Name" : nombre del formulario en redcap
# - 5. Agregar columna "Field Type" : Tipo de dato
# 

# In[ ]:


#Dejar solo las columnas que necesito
df_cacu = df[['Numero prestacion', 'Nombre Prestación', 'Preguntas','Nombre Variable Final']]


# In[ ]:


#Cambiar nombre de la variable

nombres_nuevos = {'Nombre Variable Final':'Variable / Field Name',
                 'Preguntas' : 'Field Label'}
df_cacu.rename(columns=nombres_nuevos, inplace=True)


# In[ ]:


# Crear columna Section 
df_cacu['Section Header'] = ''

# Asignar S.H. según el nombre de la prestación 
df_cacu.loc[df_cacu.groupby('Nombre Prestación').cumcount() == 0, 'Section Header'] = df['Nombre Prestación']


# In[ ]:


# Crear columna con el nombre del formulario 

df_cacu['Form Name'] = "formulario_rehabilitacion_cacu"
df_cacu["Field Note"] = ""

# Crear la columna 'Field Type' con valores por defecto 'text'
df_cacu['Field Type'] = 'text'


# In[ ]:


# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("indica_","realiza_","lugar_","lugar_exm_",
                                                               "inform_resul_","reagenda_","razon_prim_reag_",
                                                               "razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_",
                                                               "razon_quin_reag_","tipo_med_","tipo_espe_med_","n_reagenda_",
                                                               "toma_biop_","no_biop","tipo_biop_","tipo_molec_",
                                                               "tipo_espe_med_","reagenda_biop_","lugar_inf_exm_",
                                                               "tipo_prof_","int_radio_","tipo_radio_","interrup_trat_",
                                                               "pq_interrup_","tipo_quimio_","tipo_droga_",
                                                               "linea_droga_","tipo_braq_"


))

df_cacu.loc[condic, 'Field Type'] = 'dropdown'

# Crear la columna 'Choices, Calculations, OR Slider Labels'
df_cacu['Choices, Calculations, OR Slider Labels'] = ''

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('indica_','realiza_','inform_resul_','reagenda_','toma_biop_','interrup_trat_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Si | 2, No'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(('lugar_exm_'))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Lab de la Red SSMSO  | 2,  Lab externo'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("razon_prim_reag_","razon_sec_reag_","razon_ter_reag_","razon_cuar_reag_","razon_quin_reag_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se presentó | 2, Reagendamiento por temas administrativos (Ej: paro de funcionarios) | 3, Reagendamiento por rechazo del paciente | 4, Rechazo de interconsulta por Contralor | 5, Paciente no termina su tratamiento | 6, Paciente fallecido | 7, Paciente perdido (Ej: continuó su atención clínica en el extrasistema) | 8, Información no disponible'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("n_reagenda_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_med_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Médico de familia | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_prof_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Enfermera | 2, Matrona | 3, Kinesióloga| 4, Nutricionista | 5, Otra (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_biop_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Estudio histopatológico con técnicas histoquimicas especiales" | 2, Estudio histopatológico corriente de biopsia diferida(por cada órgano)" | 3, Estudio histopatológico con técnicas de inmunohistoquímica o inmunofluorescencia (por cada órgano)" | 4, Estudio histopatológico con tinción corriente de biopsia diferida con estudio seriado (mínimo 10 muestras) de un órgano o parte de él (no incluye estudio con técnica habitual de otros órganos incluidos en la muestra) | 5, Estudio histopatológico de biopsia contemporánea (rápida) a intervenciones quirúrgicas (por cada órgano) (no incluye biopsia diferida)'
                                 
# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("no_biop_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, No se encontró lesión | 2, Imposibilidad de tomar muestra | 3, Falta de insumos o RRHH | 4, Otro (Especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("lugar_inf_exm_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, En la Red SSMSO | 2,  En el extrasistema (Modalidad Libre Elección) | 3, En segundo prestador'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_molec_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, P16 | 2, Estudios de receptores hormonales  | 3, PDL-1 | 4, Otro (Especificar)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_espe_med_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Médico general | 2, Ginecólogo | 3, Cirujano General| 4, Internista | 5, Cirujano mama | 6, Ginecólogo Oncólogo | 7, Otro médico especialista (Especificar)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("int_radio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Curativa | 2, Paliativo | 3, No se especifica'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_braq_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Alta tasa (Cobalto o Iridio)| 2, Baja tasa (Cesio) | 3, No se especifíca, | 4, Otro (especificar)'

# Actualizar la columna 'Field Type' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("pq_interrup_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Mala respuesta  | 2, Intercurrencia (hospitalización por otra causa)  | 3, Toxicidad (mala tolerancia al tratamiento)  | 4, Presenta complicaciones  | 5, Problemas administrativos  | 6, No asiste  | 7, Fallecimiento'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_quimio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Adyuvante | 2, Neoadyuvante | 3, Paliativa'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_droga_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Cisplatino | 2, Paclitaxel | 3, Otra droga (Especifique)'

# Actualizar la columna 'Choices, Calculations, OR Slider Labels' para las filas que cumplen con la condición
condic = df_cacu['Variable / Field Name'].str.startswith(("tipo_radio_"))
df_cacu.loc[condic, 'Choices, Calculations, OR Slider Labels'] = '1, Radiocirugía cerebral o corporal (SRS o SBRT)  | 2, Radioterapia guiada por imágenes (IGRT)  | 3, Radioterapia de intensidad modulada (IMRT) | 4, Radioterapia conformacional 3D (3D CRT) | 5, No se especifica'

# Actualizar la columna ''Text Validation Type OR Show Slider Number' con 'dropdown' si corresponde
condic = df_cacu['Variable / Field Name'].str.startswith(("fecha_"))
df_cacu.loc[condic, 'Text Validation Type OR Show Slider Number'] = 'date_dmy'


# In[ ]:


# Define the function to apply the correct branching logic
def generate_branching_logic(row):
    variable_name = row['Variable / Field Name']
    try:
        num_prest = int(row['Numero prestacion'])
    except (ValueError, TypeError):
        return ""
    if variable_name == f"fecha_indica_cacu_{num_prest}_rehab":
        return f"[indica_cacu_{num_prest}_rehab]=1"
    
    elif variable_name == f"realiza_cacu_{num_prest}_rehab":
        return f"[indica_cacu_{num_prest}_rehab]=1"
    
    elif variable_name == f"fecha_realiza_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]=1"
    
    elif variable_name == f"lugar_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]=1"
    
    elif variable_name == f"lugar_exm_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"fecha_envio_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"fecha_devol_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"inform_resul_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"fecha_resul_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [inform_resul_cacu_{num_prest}_rehab]=1"
    
    elif variable_name == f"fecha_prox_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"reagenda_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]=1 or [realiza_cacu_{num_prest}_rehab]=2"
    
    elif variable_name == f"n_reagenda_cacu_{num_prest}_rehab":
        return f"[reagenda_cacu_{num_prest}_rehab]=1"
    
    elif variable_name == f"fecha_prim_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=1"
    
    elif variable_name == f"razon_prim_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=1"
    
    elif variable_name == f"fecha_sec_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=2"
    
    elif variable_name == f"razon_sec_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=2"
    
    elif variable_name == f"fecha_ter_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=3"
    
    elif variable_name == f"razon_ter_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=3"
    
    elif variable_name == f"fecha_cuar_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=4"
    
    elif variable_name == f"razon_cuar_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=4"
    
    elif variable_name == f"fecha_quin_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=5"
    
    elif variable_name == f"razon_quin_reag_cacu_{num_prest}_rehab":
        return f"[n_reagenda_cacu_{num_prest}_rehab]>=5"
    
    elif variable_name == f"tipo_espe_med_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"

    elif variable_name == f"otro_esp_med_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [tipo_espe_med_cacu_{num_prest}_rehab]=7"
    
    elif variable_name == f"tipo_med_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"

    elif variable_name == f"otro_med_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [tipo_med_cacu_{num_prest}_rehab]=4"
                                                          
    elif variable_name == f"tipo_prof_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"

    elif variable_name == f"otro_prof_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [tipo_prof_cacu_{num_prest}_rehab]=5"
    
    elif variable_name == f"lugar_inf_exm_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"toma_biop_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"no_biop_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [toma_biop_cacu_{num_prest}_rehab]=2"
    
    elif variable_name == f"otro_no_biop_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [no_biop_cacu_{num_prest}_rehab]=4"    
    
    elif variable_name == f"tipo_biop_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [toma_biop_cacu_{num_prest}_rehab]=1"
    
    elif variable_name == f"tipo_molec_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"otro_molec_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [tipo_molec_cacu_{num_prest}_rehab]=4"
    
    elif variable_name == f"tipo_droga_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"otra_droga_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1 and [tipo_droga_cacu_{num_prest}_rehab]=3"

    elif variable_name == f"fecha_ini_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"n_ciclos_trat_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"n_ciclos_efec_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"fecha_ter_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"interrup_trat_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"pq_interrup_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]=1 and [interrup_trat_cacu_{num_prest}_rehab]=1"
    
    elif variable_name == f"tipo_quimio_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"tipo_braq_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"fecha_alta_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"int_radio_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"tipo_radio_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"

    elif variable_name == f"diag_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"cateter_op_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"tipo_cateter_ind_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"tipo_ceteter_inst_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"
    
    elif variable_name == f"otro_braq_cacu_{num_prest}_rehab":
        return f"[realiza_cacu_{num_prest}_rehab]= 1"

    
        return ""
    
    # Apply the function to create the new column
df_cacu['Branching Logic (Show field only if...)'] = df_cacu.apply(generate_branching_logic, axis=1)


# In[ ]:


# Define the new columns with empty values
new_columns = {
    'Text Validation Min': '',
    'Text Validation Max': '',
    'Identifier?': '',
    'Required Field?': '',
    'Custom Alignment': '',
    'Question Number (surveys only)': '',
    'Matrix Group Name': '',
    'Matrix Ranking?': '',
    'Field Annotation': ''
}

# Add these new columns to the existing dataframe with default empty values
for column, value in new_columns.items():
    df_cacu[column] = value

# Definir el orden de las variables en el df

orden_deseado = ['Variable / Field Name', 'Form Name', 'Section Header', 'Field Type',
       'Field Label', 'Choices, Calculations, OR Slider Labels', 'Field Note',
       'Text Validation Type OR Show Slider Number', 'Text Validation Min',
       'Text Validation Max', 'Identifier?',
       'Branching Logic (Show field only if...)', 'Required Field?',
       'Custom Alignment', 'Question Number (surveys only)',
       'Matrix Group Name', 'Matrix Ranking?', 'Field Annotation']

#Reordenar
df_cacu = df_cacu[orden_deseado]


# In[ ]:


df_cacu.to_excel("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/CaCu_rehab.xlsx")

df_cacu.to_csv("C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv", index=False)


# In[ ]:


import zipfile
import os

# Ruta del archivo que quieres comprimir
archivo_csv = "C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/instrument.csv"

# Ruta donde se guardará el archivo comprimido
ruta_salida_zip = r"C:/Users/catal/OneDrive - udd.cl/Escritorio/CECAN/Cacu_rehab.zip"

# Crear un archivo ZIP y agregar el archivo CSV
with zipfile.ZipFile(ruta_salida_zip, 'w') as archivo_zip:
    archivo_zip.write(archivo_csv, os.path.basename(archivo_csv))

print(f"Archivo comprimido guardado en: {ruta_salida_zip}")


# In[ ]:





# In[ ]:




