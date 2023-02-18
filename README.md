# Ejercicio03-T1A1
## Etapa 01. Descripción del problema
Se requiere un programa para determinar cuál es el número más pequeño, cuál es el número más grande y cuál es el número intermedio de los tres ingresados.
## Etapa 02. Definición de la solución
 Entrada
  float val
  bool swapped 
  list my_list
  
  
- Proceso
  Solicitar al usuario que introduzca los tres números
  Se comparan el primer y segundo elemento y se determina cuál es el mayor (se ordena)
  Se comparan el segundo y el tercer elemento y se determina cuál es el mayor (se ordena)
  De esta manera se obtiene una lista ordenada (se muestran las posiciones de la lista)
 
- Salida
~~~  
  +---------------+----------------+---------------+----------------+
  | Primer Número | Segundo Número | Tercer Número | Ordenamiento |
  +---------------+----------------+---------------+----------------+
  |       10      |       15       |       1       |    15-10-1   |
  +---------------+----------------+---------------+----------------+
  |       50      |     - 10       |        8      |  50-8-(-10)  |
  +---------------+----------------+---------------+----------------+
  
   ~~~
## Etapa 03. Diseño la solución
![Diagrama](https://github.com/richardmartus/Ejercicio03Python/blob/main/.idea/Diagrama%20de%20Clases3.png)
## Etapa 04. Desarrollo de la solución
Código disponible en el archivo [main](main.py)
## Etapa 05. Depuración y Pruebas
![Diagrama](https://github.com/richardmartus/Ejercicio03Python/blob/main/.idea/prueba1Ej03.png)
![Diagrama](https://github.com/richardmartus/Ejercicio03Python/blob/main/.idea/prueba2Ej03.png)


