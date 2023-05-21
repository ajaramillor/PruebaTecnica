
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
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

## Factores de riesgo

Los principales riesgos asociados con este proyecto incluyen:

- Fallos en la integración y transformación de datos.
- Problemas de rendimiento y escalabilidad de la base de datos.
- Problemas de calidad de datos que afectan la precisión y la consistencia del dashboard.

Para mitigar estos riesgos, se implementan pruebas de integración y transformación de datos exhaustivas, se configura la base de datos para optimizar el rendimiento y un proceso de verificación de calidad de datos.

## Criterios de éxito

El éxito de este proyecto se medirá por la capacidad de la base de datos para manejar grandes cantidades de datos de manera eficiente y escalable, así como por la precisión y la consistencia de los datos en la base de datos.

# Proceso

A continuación se incluye la descripción general de cada uno de los pasos y el link a su respectivo notebook.

## Limpieza y carga de los datos

Los datos se encuentran en el archivo comprimido [flights.zip](datasets), contenido en el archivo comprimido flights.zip. Se hace de esta manera porque el archivo descomprimido supera el límite de Github. A continuación, se procede a la limpieza de datos en el Jupyter notebook [limpieza](limpieza.ipynb).

## Diseño DB

Teniendo claro el propósito del proyecto que es alimentar un dashboard para la toma de decisiones se opta por una base de datos relacional con un esquema en estrella ya que tiene las siguientes ventajas:

- Rendimiento optimizado: El diseño en estrella permite un acceso rápido y eficiente a los datos. Al tener una tabla de hechos central y tablas de dimensiones conectadas a ella, las consultas pueden realizarse de manera rápida y directa, lo que agiliza el rendimiento del dashboard.
- Simplificación de consultas: Al separar los datos en hechos y dimensiones, el modelo de base de datos en estrella simplifica las consultas complejas. Las tablas de dimensiones contienen atributos descriptivos que se utilizan para filtrar, agrupar y clasificar los datos en el dashboard, lo que facilita la generación de consultas y la obtención de resultados rápidos.
- Facilidad de mantenimiento: El modelo en estrella es fácil de mantener y actualizar. Si se necesita agregar una nueva dimensión o modificar una existente, se pueden realizar cambios en las tablas de dimensiones sin afectar la tabla de hechos. Esto evita la necesidad de modificar todas las consultas y asegura que el dashboard siga funcionando sin interrupciones.
- Escalabilidad: El modelo en estrella es altamente escalable. A medida que se agregan más datos al sistema, se pueden agregar nuevas tablas de hechos y dimensiones sin afectar el rendimiento general. Esto permite que el dashboard crezca a medida que crecen las necesidades de la organización sin comprometer la velocidad de respuesta.

A continuación se presenta el diagrama de la base de datos:

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/ajaramillor/PruebaTecnica/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/ajaramillor/PruebaTecnica/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/ajaramillor/PruebaTecnica/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/ajaramillor/PruebaTecnica/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/ajaramillor/PruebaTecnica/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alejandro-jaramillo-rivas/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
