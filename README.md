# Justificación de decisiones clave.
## Imputación de los datos.
**Caso columna "Age":**  
Sólo tiene el $3.49\%$ de los datos nulos, entonces como es un porcentaje pequeño podemos suponer que estos datos no son significativos al momento de entrenar un modelo. Así, podemos eliminar las filas cuya columna "Age" sea nula.

**Caso columnas "Height" y "Weight":**  
Cuando las columnas "Height" y "Weight" son valores nulos podemos suponer que es debido a la misma situación, por lo tanto debemos tratarlos de la misma forma. Como son datos de atletas en diferentes deportes de distintos paises y edades, entonces podemos usar el promedio en función de ("sport", "NOC","sex","age") puesto que el cuerpo de la persona varia en estas variables. Por ejemplo, una persona que hace maraton no tiene el mismo cuerpo que la persona que hace football. Las personas también varían por NOC (país), por ejemplo una persona de dinamarca tiende a ser alta, pero en Asia tienden a ser más pequeñas. Finalmente, los hombres tienden a pesar más y ser más altos que las mujeres. Para el caso de la edad, se definiran rangos de edad en donde se supone que no varían demasiado los pesos y alturas de las atletas. Los rango de edades se forman puesto que necesitamos pasar una variable discreta a categorica y porque si lo hacemos por edad los grupos serían demasiado pequeños.

En resumen, imputaremos con el promedio de la agrupación del tipo ("sport", "NOC","sex","Edad_rango"). Obviamente, no se imputaran todas las filas necesarias, si que proseguiremos agrupando por ("sport","sex","Edad_rango"), ("NOC","Sexo","Edad_rango") y finalmente por ("Sexo","Edad_rango").

**Caso columnas "Medalla":**  
Del item anterior, podemos ver que los posibles valores de la columna medalla son: 
- Bronze,
- Gold y
- Silver.  

Por lo tanto, podemos suponer que no se registran o se deja en blanco cuando la persona no obtiene alguna medalla. De este modo, llenaremos los valores null con la etiqueta "Ninguna".

## Validar si existen filas duplicadas o generadas por una combinación sensata de columnas y decidir si esas se eliminan o se preservan.

Si pensamos en normalizar la tabla, podemos entender que existen al menos tres entidades, [Atleta, Deporte, Evento]. Por lo tanto, podemos formar una primary key para cada una de estas entidades, concatenarlas y formaremos una primary key de la tabla. 

**Para Atletas.**  
Consideramos algunos ejemplos:
- Nombre y sexo como clave.  
Esto es insuficiente, puesto que existe un él atleta llamado "Yang Wei" y una atleta llamada de la misma forma.

- Nombre, Sexo y Edad como clave.  
Esto es insuficiente, puesto que existen dos atletas llamados "Balbir Singh" con estas atributos.

Por lo tanto, se postula la siguiente primary key para los atletas (Nombre, Sexo, Edad, Altura).

**Para Deporte**  
Sólo basta con la columna (Deporte).

**Para Evento**  
Sólo basta con las columnas (Año, Evento)

Luego, concatenamos estas claves, y nos fijamos que exite un atleta llamado "Adolf Mller", la cuál tiene un doble registro, uno con medalla y el otro no. De este modo, Mantendremos la primary formada, pero dejaremos los datos que tiene la medalla de mayor valor.

Notar que los eventos asociados al Deporte llamado "Art Competitions" es poco especifico, puesto que existen muchas categorias de eventos asociadas a este deporte y algunos son desconocidos. Aún así, aplicaremos la misma clave primaria.


# Instrucciones sobre cómo configurar el entorno
Versión de python: 3.12
Lista de librerias utilizadas se instala desde el archivo "requirements.txt"

## Resumen
Se creará un entorno capaz de ejecutar los códigos asociados al desafío. Para esto, se ejecutara el jupyter notebook con las tareas de la 1 al 6. Luego, se ejecuta la api de la tarea 7.


## Instructivo.
- Instalar python versión 3.12
- Abrir la terminal y dirigirse con el comando "cd" a un lugar donde desea instalar el entorno
- Ejecutar el comando "python3.12 -m venv NombreEnv",  con esto creará una carpeta llamada "NombreEnv"
- Usar "cd NombreEnv", y ejecutar "Scripts\activate", con esto cargará el entorno.
<img width="1272" height="197" alt="capture_250922_193340" src="https://github.com/user-attachments/assets/2ec75fd3-7c9d-4e18-b6bb-80d63cdd4e49" />

- Ir desde la terminal a la ubicación de "requirements.txt"
- Ejecutar "pip install -r requirements.txt" para instalar las librerias
- Ejecutr "pip install ipykernel"
- Ejecutar en la terminal "jupyter notebook"
- Abrir el archivo "desafio.ipynb"

Una vez corrido el código de "Ortega_Ignacio_desafio.ipynb", habremos generado los archivos:
- cleaned_olympic_data.csv
- olympic_kpi.json
en la carpeta "results".

Para abrir la API de la tarea 7, debemos cerrar todo y abrir otra terminal para cargar el entorno nuevamente y ejecutar la api. 
De esta forma,
- Abrimos una terminal,
- Nos dirigimos "dentro" de la carpeta "NombreEnv" usando el comando "cd",
- Ejecutarmos "Scripts\activate" para cargar el entorno,
Notar que podemos usar "ctrl+c" en la terminal en que ejecutamos "jupyter notebook" para cargar el entorno.

Seguimos ...
- Nos dirigimos a la ubicación del archivo "api.py" con el comando "cd",
- Ejecutamos el archivo "api.py" usando "python api.py"

Una vez ejecutado, debe hacer click+ctrl sobre la dirección que aparece en la terminal para abrir una página web.

<img width="1436" height="230" alt="capture_250922_190912" src="https://github.com/user-attachments/assets/0a544002-f343-495d-a80b-fc530c173232" />

Esta API tiene un página inicial con hipervínculos que dirige a las direcciones de la tarea 7. Usar otro filtro que sea "noc=CHI", podemos usar la página de ejemplo "http://127.0.0.1:5000/athlete_data_by_noc?noc=CHI" y cambiar "CHI" por el país deseado, por ejemplo "http://127.0.0.1:5000/athlete_data_by_noc?noc=USA".

# Ubicación de los archivos
Los archivos ("cleaned_olympic_data.csv", "olympic_kpi.json") están en la carpeta "./results".

# Desafíos dentro del desafío.
Pienso que como ingeniero matemático, el desafío más grande fue armar la API y pensar claves con la cuál se pudiera identificar a cierta persona, esto se ve más claramente cuando debemos validar los datos y concluimos que ciertos atletas están duplicados sin considerar la columna medalla.







- 
