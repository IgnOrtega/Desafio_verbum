Para poder visualizar mejor el reamde.md puede ir al siguiente enlace https://github.com/IgnOrtega/Desafio_verbum/blob/master/README.md

# Justificación de decisiones clave.
## Imputación de los datos.
**Caso columna "Age":**  
Sólo tiene el $3.49\%$ de los datos nulos, entonces como es un porcentaje pequeño podemos suponer que estos datos no son significativos al momento de entrenar un modelo. Así, podemos eliminar las filas cuya columna "Age" sea nula.

**Caso columnas "Height" y "Weight":**  
Cuando las columnas "Height" y "Weight" son valores nulos podemos suponer que es debido a la misma situación, puesto que tienen aproximadamente el mismo porcentaje de datos faltantes y uno podría suponer que cuando te pesan también te miden y viceversa.

**Caso columnas "Medalla":**  
Podemos suponer que no se registran o se deja en blanco la columna "medalla" cuando la persona no obtiene alguna medalla.

## Validar si existen filas duplicadas o generadas por una combinación sensata de columnas y decidir si esas se eliminan o se preservan.
Si pensamos en normalizar la tabla, podemos entender que existen al menos tres entidades, [Atleta, Deporte, Evento]. Por lo tanto, podemos formar una primary key para cada una de estas entidades, concatenarlas y formaremos una primary key de la tabla. 

# Instructivo
Versión de python: 3.12
Lista de librerias utilizadas se instala desde el archivo "requirements.txt"

## Resumen
Se creará un entorno capaz de ejecutar los códigos asociados al desafío. Para esto, se ejecutara el jupyter notebook con las tareas de la 1 al 6. Luego, se ejecuta la api de la tarea 7.


## Instructivo para configurar el entorno.
- Instalar python versión 3.12
- Abrir la terminal y dirigirse con el comando "cd" a un lugar donde desea instalar el entorno
- Ejecutar el comando "python3.12 -m venv NombreEnv",  con esto creará una carpeta llamada "NombreEnv"
- Usar "cd NombreEnv", y ejecutar "Scripts\activate", con esto cargará el entorno.
<img width="1272" height="197" alt="capture_250922_193340" src="https://github.com/user-attachments/assets/2ec75fd3-7c9d-4e18-b6bb-80d63cdd4e49" />

- Ir desde la terminal a la ubicación de "requirements.txt"
- Ejecutar "pip install -r requirements.txt" para instalar las librerias
- Ejecutar "pip install ipykernel"

## Instructivo para ejecutar el jupyter notebook
Sobre la terminal del punto anterior, ejecutamos:
- Ejecutar en la terminal "jupyter notebook"
- Abrir el archivo "Ortega_Ignacio_desafio.ipynb"

## Instructivo para ejecutar la API
Una vez ejecutado el código de "Ortega_Ignacio_desafio.ipynb", habremos generado los archivos:
- cleaned_olympic_data.csv
- olympic_kpi.json  
en la carpeta "results" que también será generada.

Para abrir la API de la tarea 7 debemos cargar el entorno creado. Así, tenemos dos alternativas para realizar esta tarea: 

**Alternativa 1**  
- Usar "ctrl+c" en la terminal en que ejecutamos "jupyter notebook" para cancelar el proceso.
Con esto, tendremos el entorno cargado puesto que ya estaba cargado.
<img width="1897" height="420" alt="cargar_entorno" src="https://github.com/user-attachments/assets/5f4f1ecb-c956-4250-b462-86130999ed81" />

**Alternativa 2**  
La idea es cerrar todo y abrir otra terminal para cargar el entorno nuevamente y ejecutar la api. 
De esta forma:
- Cerramos todo,
- Abrimos una terminal,
- Nos dirigimos "dentro" de la carpeta "NombreEnv" usando el comando "cd",
- Ejecutarmos "Scripts\activate" para cargar el entorno.  
Con esto tendremos el entorno cargado.
<img width="1272" height="197" alt="capture_250922_193340" src="https://github.com/user-attachments/assets/2ec75fd3-7c9d-4e18-b6bb-80d63cdd4e49" />

Seguimos ...
- Nos dirigimos a la ubicación del archivo "api.py" con el comando "cd",
- Ejecutamos el archivo "api.py" usando "python api.py"

Una vez ejecutado, debe hacer click+ctrl sobre la dirección que aparece en la terminal para abrir una página web.

<img width="1436" height="230" alt="capture_250922_190912" src="https://github.com/user-attachments/assets/0a544002-f343-495d-a80b-fc530c173232" />

Esta API tiene un página inicial con hipervínculos que dirige a las direcciones de la tarea 7. Usar otro filtro que sea "noc=CHI", podemos usar la página de ejemplo "http://127.0.0.1:5000/athlete_data_by_noc?noc=CHI" y cambiar "CHI" por el país deseado, por ejemplo "http://127.0.0.1:5000/athlete_data_by_noc?noc=USA".

# Ubicación de los archivos
Los archivos ("cleaned_olympic_data.csv", "olympic_kpi.json") están en la carpeta "./results". La carpeta "./results" es generada por el archivo "Ortega_Ignacio_desafio.ipynb".

# Desafíos dentro del desafío.
Pienso como ingeniero matemático que el desafío más grande fue armar la API y pensar claves con la cuál se pudiera identificar a cierta persona, esto se ve más claramente cuando debemos validar los datos y concluimos que ciertos atletas están duplicados sin considerar la columna medalla.







- 
