
<br />
<div align="center">
<h3 align="center">PRUEBA TÉCNICA</h3>

  <p align="center">
    Prueba técnica para Data Engineer
    <br />
    <a href="https://github.com/ajaramillor/PruebaTecnica"><strong>Ver archivos »</strong></a>
    ·
    <a href="https://github.com/ajaramillor/PruebaTecnica/issues">Reportar bugs</a>
    ·
  </p>
</div>

[![LinkedIn][linkedin-shield]][linkedin-url]

**Índice**
- [Planteamiento del problema](#planteamiento-del-problema)
- [Objetivos](#objetivos)
- [Exclusiones](#exclusiones)
- [Solución propuesta](#solución-propuesta)
  - [Factores de riesgo](#factores-de-riesgo)
  - [Criterios de éxito](#criterios-de-éxito)
- [Proceso](#proceso)
  - [Limpieza y carga de los datos](#limpieza-y-carga-de-los-datos)
  - [Diseño DB](#diseño-db)
  - [Carga de datos](#carga-de-datos)
  - [ETL](#etl)
  - [Dashboard](#dashboard)
- [Pruebas unitarias](#pruebas-unitarias)
- [Escenarios futuros](#escenarios-futuros)
- [Referencias](#referencias)



# Planteamiento del problema

Como prueba técnica se pide el planteamiento y diseño de una solución de procesamiento de datos con el fin de verificar las capacidades técnicas y la capacidad de trabajar bajo presión.

# Objetivos

El objetivo de este proyecto es construir una base de datos que alimente un dashboard de visualización de datos para la toma de decisiones de una aerolínea. La información disponible para esta base de datos son los registros históricos de vuelos dentro del país. La base de datos debe ser capaz de manejar grandes cantidades de datos y ser escalable para permitir futuras expansiones del dashboard.

# Exclusiones

Este proyecto no abordará la construcción del dashboard en sí, sino que se centrará en la construcción de la base de datos que lo alimenta.

# Solución propuesta

El proceso constará de las siguientes etapas:

1. **Carga de datos históricos en CSV:** recopilar los registros históricos de vuelos dentro del país en formato CSV desde las fuentes de datos identificadas en la etapa de planificación.
2. **Limpieza de datos:** realizar un proceso de limpieza de datos para garantizar que los datos sean precisos y consistentes. Esto incluye la eliminación de datos duplicados, la corrección de errores tipográficos y la normalización de los datos.
3. **Creación de la base de datos:** diseñar y construir una arquitectura de base de datos escalable que pueda manejar grandes cantidades de datos y permitir futuras expansiones. Se utiliza un motor de base de datos relacional para garantizar la integridad de los datos y se implementa una estructura de tabla eficiente para optimizar el rendimiento.
4. **Creación del dashboard:** crear un dashboard de visualización de datos para la toma de decisiones de la aerolínea utilizando los datos almacenados en la base de datos. El dashboard se construye utilizando una herramienta de visualización de datos como Tableau o Power BI y se personaliza para satisfacer las necesidades específicas de la aerolínea.

![image](https://github.com/ajaramillor/PruebaTecnica/assets/98030147/4ef86fa0-5051-4f73-8039-777997e13537)

## Factores de riesgo

Los principales riesgos asociados con este proyecto incluyen:

- Fallos en la integración y transformación de datos.
- Problemas de rendimiento y escalabilidad de la base de datos.
- Problemas de calidad de datos que afectan la precisión y la consistencia del dashboard.

Para mitigar estos riesgos, se implementan pruebas de integración y transformación de datos exhaustivas, se configura la base de datos para optimizar el rendimiento y un proceso de verificación de calidad de datos.

## Criterios de éxito

El éxito de este proyecto se medirá por la capacidad de la base de datos para manejar grandes cantidades de datos de manera eficiente y escalable, así como por la precisión y la consistencia de los datos en la base de datos.

# Proceso

A continuación se incluye la descripción general de cada uno de los pasos y el link a su respectivo notebook. Se debe destacar que las funciones se dejan en el notebook por facilidad de lectura, se podrían llamar directamente desde el archivo [funciones](funciones.py) pero sería más difícil la lectura del documento.

## Limpieza y carga de los datos

Los datos se encuentran en el archivo comprimido [flights](flights.zip), contenido en el archivo comprimido flights.zip. Se hace de esta manera porque el archivo descomprimido supera el límite de Github. A continuación, se procede a la limpieza de datos en el Jupyter notebook [limpieza](Limpieza.ipynb).

## Diseño DB

Teniendo claro el propósito del proyecto que es alimentar un dashboard para la toma de decisiones se opta por una base de datos relacional con un esquema en estrella ya que tiene las siguientes ventajas:

- Rendimiento optimizado: El diseño en estrella permite un acceso rápido y eficiente a los datos. Al tener una tabla de hechos central y tablas de dimensiones conectadas a ella, las consultas pueden realizarse de manera rápida y directa, lo que agiliza el rendimiento del dashboard.
- Simplificación de consultas: Al separar los datos en hechos y dimensiones, el modelo de base de datos en estrella simplifica las consultas complejas. Las tablas de dimensiones contienen atributos descriptivos que se utilizan para filtrar, agrupar y clasificar los datos en el dashboard, lo que facilita la generación de consultas y la obtención de resultados rápidos.
- Facilidad de mantenimiento: El modelo en estrella es fácil de mantener y actualizar. Si se necesita agregar una nueva dimensión o modificar una existente, se pueden realizar cambios en las tablas de dimensiones sin afectar la tabla de hechos. Esto evita la necesidad de modificar todas las consultas y asegura que el dashboard siga funcionando sin interrupciones.
- Escalabilidad: El modelo en estrella es altamente escalable. A medida que se agregan más datos al sistema, se pueden agregar nuevas tablas de hechos y dimensiones sin afectar el rendimiento general. Esto permite que el dashboard crezca a medida que crecen las necesidades de la organización sin comprometer la velocidad de respuesta.

A continuación se presenta el diagrama de la base de datos:
![bd](https://github.com/ajaramillor/PruebaTecnica/assets/98030147/3b0ac13a-ad58-4a0e-b584-7286436d9b10)

## Carga de datos

El proceso de carga se realiza con otro Jupyter notebook [Transformacion_carga](Transformacion_carga.ipynb) que permite dividir el dataset limpio en las distintas tablas de la base de datos, posteriormente por medio de la API de GCP se suben los dataframes y se forman las dimensiones y la tabla de hechos (fact table) para el posterior análisis.

![image](https://github.com/ajaramillor/PruebaTecnica/assets/98030147/add2be04-a621-46d0-82bf-20dff5919ce9)

## ETL

Para el proceso ETL (Extracción, Transformación y Carga) se propone una una Cloud Function de Google que es una solución escalable y eficiente para la integración de datos. Este enfoque aprovecha la infraestructura y los servicios de Google Cloud Platform (GCP) además permite solo pagar por uso y optimizar recursos vs una solución local.

Es importante mencionar que la Cloud Function de Google es una función sin servidor que se ejecuta de manera automatizada en respuesta a eventos específicos, como cambios en los datos de origen o programados de acuerdo a una frecuencia determinada. Esto permite la ejecución periódica y programada del proceso ETL, asegurando la actualización constante de los datos y la generación de insights en tiempo real.

Además, la Cloud Function se beneficia de la escalabilidad y disponibilidad proporcionadas por GCP. Esto significa que puede manejar grandes volúmenes de datos y adaptarse a cambios en la demanda sin problemas, lo que garantiza un rendimiento óptimo del proceso ETL.

Para fines prácticos de la prueba y debido a que las Cloud Functions tienen un costo se presentará el proceso en un Jupyter notebook [ETL](ETL.ipynb) pero su código exportado a .py es identico al usado por la Cloud Function.

![image](https://github.com/ajaramillor/PruebaTecnica/assets/98030147/8adcd841-1d23-4d81-bf63-ceb3b706a358)


## Dashboard

El último paso de la solución propuesta es la creación del dashboard final, en este caso se utiliza el visualizador gratuito de GCP, Looker Studio. A continuación se muestra el preview y el link donde se puede acceder de manera libre al dashboard. 

![image](https://github.com/ajaramillor/PruebaTecnica/assets/98030147/6e748e6a-4d2e-4c98-9701-97ab7db0dce7)

[Link dashboard](https://lookerstudio.google.com/s/o0uhH7ydH4Q)

# Pruebas unitarias

Para verificar las funciones que se crean en el proceso se realizan pruebas unitarias con Pytest, en el repositorio se encuentra el archivo [test_funciones](funciones.py) para verificarlas. Las funciones que dependen de la API de Google no se probaron pues requiere un desarrollo diferente fuera del alcance de esta prueba como creacion de mocks de la API con Unittest.
![image](https://github.com/ajaramillor/PruebaTecnica/assets/98030147/849cbfe1-ab68-48b7-b724-506d5cfa6668)

# Escenarios futuros

La prueba técnica tiene las siguientes preguntas respecto a lo que puede suceder con esta solución en un futuro:

- **Si los datos se incrementaran en 100x:** en este escenario se propone cambiar la Cloud Function por un Dataproc o cualquier otro servicio cloud que permita el despliegue de Apache e implementar Apache Spark para el procesamiento paralelo de los datos; mejorar la Cloud Function donde corre el proceso por una con más RAM puede no ser suficiente ya que todo el código funciona con Pandas y su consumo es muy elevado.
- **Si las tuberías se ejecutaran diariamente en una ventana de tiempo especifica:** originalmente se propone correr la tubería o ETL cada día pues no influye mucho la información intra diaria en la toma de decisiones pero si se requiere más seguido no hay problema ya que la ETL no se relaciona con otras, si se requiere incorporar otras fuentes o ETL que dependan entre sí se recomienda migrar el proceso a Airflow o algún otro orquestador para facilitar el proceso.
- **Si la base de datos necesitara ser accedido por más de 100 usuarios funcionales:** como la solución actual ya está implementada en Bigquery que es autoescalable no hay mucho por mejorar en este aspecto, lo que si se debe configurar es el dashboard para que solo lea información directamente de las tablas y no haga querys en el proceso pues 100 usuarios entrando al tiempo pueden elevar los costos sin necesidad.}
- **Si se requiere hacer analítica en tiempo real, ¿Cuáles componentes cambiaria a su
arquitectura propuesta?:** la infraestructura actual permite realizar analítica en tiempo real, el cambio sería consultar la información directamente desde una API que tenga la misma información y no esperar a que se consolide un CSV cada día.

# Referencias

- [https://www.kaggle.com/datasets/mmetter/flights](https://www.kaggle.com/datasets/mmetter/flights)
- [https://chat.openai.com/](https://chat.openai.com/)
- [https://cloud.google.com/bigquery/docs/samples/](https://cloud.google.com/bigquery/docs/samples/)
<!-- LINKS EXTERNOS -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alejandro-jaramillo-rivas/
