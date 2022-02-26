# GBI6_ExamenPython
## Datos personales
Nombre: Dilan Jhoel Porras Quinaucho<br> 
Fecha: 25 de febrero del 2022<br> 
Correo: dilan.porras@est.ikiam.edu.ec<br> 
Sexto semestre<br> 
## Características del computador
      Time of this report: 2/25/2022, 21:19:56
             Machine name: DILANJHOEL
               Machine Id: {9A12274C-C370-4254-BE42-33A85FC14E71}
         Operating System: Windows 10 Home 64-bit (10.0, Build 19043) (19041.vb_release.191206-1406)
                 Language: Spanish (Regional Setting: Spanish)
      System Manufacturer: HP
             System Model: HP Notebook
                     BIOS: InsydeH2O Version 05.10.52F.09 (type: BIOS)
                Processor: AMD A10-9600P RADEON R5, 10 COMPUTE CORES 4C+6G (4 CPUs), ~2.4GHz
                   Memory: 8192MB RAM
      Available OS Memory: 7648MB RAM
                Page File: 6866MB used, 7316MB available
              Windows Dir: C:\WINDOWS
          DirectX Version: DirectX 12
      DX Setup Parameters: Not found
         User DPI Setting: 96 DPI (100 percent)
       System DPI Setting: 96 DPI (100 percent)
          DWM DPI Scaling: Disabled
                 Miracast: Available, with HDCP
Microsoft Graphics Hybrid: Not Supported
 DirectX Database Version: 1.0.8
           DxDiag Version: 10.00.19041.0928 64bit Unicode
## Versión de Python/Anaconda y de cada uno de los módulos/paquetes utilizados
### Versión de python 3.8.8
### Módulos: 
miningscience → contiene 2 funciones: download_pubmed para descargar información sobre publicaciones y artículos relacionados con la **palabra clave** que se usa para buscar y mining_pubs para usar tres tipos de variables: **DP** sobre el año de publicación del artículo por PMID, **AU** sobre el número de autores por PMID, **AD** sobre el conteo de autores por país, para mostrar un dataframe como resultado.
csv → es un formato utilizado para importar y exportar los datos de hojas de cálculo y bases de datos usado en python. 
Numpy → permite trabajar matrices multidimensionales. La implementación de matrices no está en Python. Principalmente se usa en proyectos de aprendizaje automático. 
Pandas → sirve para análisis de datos, filtrar los datos de forma más eficaz y ofrece diferentes tipos de estructuras de datos que son útiles para trabajar. También proporciona manejo de archivos con diferentes formatos de archivo.
Matplotlib → es una biblioteca de trazado de gráficos 2D, se visualiza datos, se genera imágenes de las figuras en diferentes formatos y se traza diferentes tipos de diagramas como gráficos de barras, gráficos de error, histogramas, diagramas de dispersión, etc.
re → permite buscar dentro y cambiar texto usando patrones formales.
os →  permite el acceso portable a funciones específicas del sistema operativo.
scipy → es una biblioteca de código abierto de herramientas y algoritmos matemáticos de Travis Oliphant.
Bio (Biopython) → permite leer y modificar la mayoría de formatos habituales para cada una de sus áreas de actividad, y su licencia es compatible con la mayoría de licencias de código abierto, de manera que puede ser utilizado para crear una gran variedad de proyectos informáticos.
## Explicación de la data utilizada
Ecuador_genomics.txt → información sobre artículos con participación de científicos o autores ecuatorianos que estudian un conjunto completo de ADN (con todos sus genes) de una persona u otro organismo, sus características y aplicaciones, por ejemplo: el artículo de revisión con PMID: 35121084 y participación del autor cuencano Chango Diego, proporciona normas de referencia para la electrocardiografía que pueden ser utilizadas por los médicos, que deben ser conscientes de los efectos de la residencia a gran altitud en la salud cardiovascular y de cómo éstos pueden cambiar en función de la edad, el origen étnico y otros factores.
countries_coordinates.txt → latitudes y longitudes con los respectivos nombres de cada país en todo el mundo, dando un total de 244 datos.
mapamundi.png → gráfico del mapa mundi del planeta.
miningscience.py → módulo usado en python, antes descrito.
### Pregunta 6
alignment.txt → alineamiento sobre genes de la testosterona en diferentes especies de mamíferos (10 secuencia en GenBank).
