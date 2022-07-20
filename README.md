# Powermeter
Armar una API REST en Django con integración con Django Rest Framework que guarde Mediciones en
una base de datos relacional. Mediante un endpoint se envían las mediciones, y mediante tres
endpoints distintos se puede pedir el valor mínimo de las mediciones, el valor máximo y el promedio. El
endpoint /save va a recibir una lista de valores en la key “sensor_data” y hay que guardar cada valor por
separado. La lista puede tener uno o más valores y los valores pueden ser enteros o floats, positivos,
negativos o cero.
Los endpoints para obtener el máximo, mínimo o promedio son GET, no reciben nada y devuelven un
JSON cuya key es la operación y el valor es el resultado de la operación.
La forma en la que lo probamos es realizando múltiples POST mediante el siguiente comando:
curl -X POST http://localhost:8000/api/save/ -d '{"sensor_data": [1, -2, 3.2, 7]}' -H "Content-Type: application/json"

----------------------------------------------------------------------------------------------------

### Antes de empezar 📋

Se utilizo el entorno virtual Pyenv\
Para crear un determinado entorno debe **ejecutar los siguiente comandos** en la terminal:

>$`pyenv virtualenv "version_python" "nombre_entorno_virtual"                  #creación de entorno virtual`\
$`pyenv activate "nombre_entorno_virtual"                                       #activar entorno virtual` \

## Clonar proyecto:

Se puede clonar el proyecto por medio del siguiente comando

> $`git init`\
$`git clone git@github.com:cristianniglesias/Powermeter_Prueba.git`



### Instalación 🔧

Primero se deben instalar los requerimientos

Ejecutar en la terminal

>$`pip install -r requirements.txt`


## Correr proyecto Powermeter🚀

Se deben seguir los siguientes pasos

1. Ejecutar las migraciones
> $`python manage.py migrate`
2. Levantar proyecto
> $`python manage.py runserver`
3. Crear superusuario para acceder al administrador de django si fuera necesario
> $`python manage.py createsuperuser`

### Probando proyecto 🔩

### A continuacion se dejan diferentes comandos para realizar las pruebas

Ejecutar desde terminal

1. Cargar la base de datos
>$`curl -X POST http://localhost:8000/api/save/ -d '{"sensor_data": [1, -2, 3.2, 7]}' -H "Content-Type: application/json"`
2. Consultas 
>$`curl http://localhost:8000/api/get/max/` 
$`curl http://localhost:8000/api/get/min/`   
$`curl http://localhost:8000/api/get/avg/`  
3. Código en python

Se generó un archvio denominado "calcular.py" que realiza lo siguiente

    Teniendo como base: 
    repetidos = [1,2,3,"1","2","3",3,4,5]
    r = [1,"5",2,"3"]
    d_str = '{"valor":125.3,"codigo":123}'

    a. Genera una lista con los valores no repetidos de la lista ‘repetidos’.
    b. Genera una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
    c. Transforma ‘d_str’ en un diccionario.

Para correrlo:
>$`python manage.py calcular`


## Softwares principales utilizados 🛠️

* [Django Rest Framework](https://www.django-rest-framework.org/) - Framework
* [Python](https://www.python.org/) - lenguaje de programacón


## Opinion sobre el proyecto 📖

Utilizamos el decorador @api_view en la seccions views dentro de la clase correspondiente para devolver los diferentes gets requeridos permitiendo un analisis y una respuesta sencilla de la información.
Utilizamos aggregate en la consulta del max, min y promedio, ya que podemos procesar los datos directamente desde la base de datos, sino, deberiamos analizar y realizar diferentes calculos con python. Asi, reducimos, entre otras cosas, la cantidad de lineas de codigo. 
En los casos que la base de datos no cuente con información para poder realizar las métricas, se enviará un mensaje informativo.