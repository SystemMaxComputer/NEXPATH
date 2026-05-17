
   # **🧭# NEXPATH -- Rutas Óptimas y Seguras en Medellín**

## **🎯 Objetivo general**

Diseñar e implementar un sistema que permita calcular y visualizar rutas óptimas entre dos puntos de la ciudad de Medellín, considerando simultáneamente la **distancia** y el **riesgo de acoso**.  
El sistema debe ofrecer al usuario distintas **estrategias algorítmicas** y permitir la **configuración de preferencias** (prioridad por seguridad o rapidez), con el fin de comparar precisión, tiempo de cómputo y comportamiento de los algoritmos.

---

## **🧩 Contexto**

Se proporciona un [**dataset geográfico**](https://drive.google.com/file/d/11cOIpKB_OrAWPTm2IDFH-Tz_vDb4i-dx/view?usp=sharing) que describe la red vial de Medellín. Cada registro corresponde a un tramo de calle con los siguientes campos:

| Campo | Descripción |
| :---- | :---- |
| `name` | Nombre de la calle o segmento. |
| `origin` | Coordenadas geográficas del punto de inicio `(long, lat)`. |
| `destination` | Coordenadas geográficas del punto final `(long, lat)`. |
| `length` | Longitud del tramo (en metros). |
| `oneway` | Indica si la vía es unidireccional. |
| `harassmentRisk` | Valor entre 0 y 1 que indica el nivel de riesgo percibido. |
| `geometry` | Representación geométrica LINESTRING del tramo. |

A partir de estos datos, se debe construir un **grafo dirigido y ponderado**, donde cada arista tenga un costo definido por:

**C(e) \= α×length(e) \+ β×harassmentRisk(e)**

donde:

* `α` y `β` son pesos ajustables definidos por el usuario según su preferencia entre **rapidez** y **seguridad**.
