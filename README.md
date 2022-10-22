# apigee_edge_analytics_extractor
Permite extraer analiticas de una organizacion y sus ambientes. Esto por mes, segmentado por API Proxy.


### Estructura del respositorio y archivos:
```
.
└── apigee_edge_analytics_extractor/
    ├── analytics.csv - el archivo donde queda el resultado de las analiticas.
    ├── apigee_details.json - aqui se configuran los detalles de la organizacion en donde se debe gatillar el proceso de extraccion.
    ├── extract_analytics.py - el script que orquesta el proceso de extraccion.
    ├── functions.py - funciones invocadas para el proceso de extraccion.
    └── README.md - documentacion.
```

---
### Pre-requisitos:

* Python3
* Python Modules: requests


---
### Configuracion de Dependencias:

A continuacion se muestra la informacion requerida para el proceso de extraccion. Se deben reemplazar los valores del archivo json por los valores de la organizacion y ambiente del cual se quiere hacer la extraccion.


**apigee_details.json:**

```json
{
    "org": "organization-name",
    "environments": [
        "environment1",
        "environment2",
        "environment3"
    ],
    "user": "your-email-address",
    "pass": "password",
    "time_range": "07/01/2022 00:00~07/31/2022 23:59"
}
```

Este Json debe modificarse y guardarse teniendo como referencia el siguiente detalle:

| **Atributo** |                                             **Descripcion**                                             |
|:------------:|:-------------------------------------------------------------------------------------------------------:|
| org          | El nombre/identificador de la organizacion de apigee.                                                   |
| environments | Este es un arreglo de strings. Agrega el nombre de los ambientes de los cuales quieres extraer la data. |
| user         | El usuario que utilizas para acceder a Apigee.                                                          |
| pass         | La clave que utilizas para acceder a Apigee.                                                            |
| time_range   | El intervalo de tiempo del cual se desea extraer la informacion ej: 07/01/2022 00:00~07/31/2022 23:59   |

**Nota:** El usuario y contraseña no se utilizan en el proceso de extraccion. El script genera un access token con el cual se gatillan las llamadas a Apigee Edge Management APIs.

---
### Ejecutar la Extraccion:

Para ejecutar la extraccion lo unico que debemos hacer es ejecutar el siguiente comando:

```shell
python3 extract_analytics.py
```


---
### Revision de Output:

El output que debiera generarse como resultado del proceso de extraccion se debe ver reflejado en el archivo:

```shell
analytics.csv
```

Con este podran revisarse las analiticas segmentadas con el siguiente formato:

| **organization** | **environment** |    **apiproxy**    | **transactions** |           **time_range**          |
|:----------------:|:---------------:|:------------------:|:----------------:|:---------------------------------:|
| example-org      | dev             | customers-apiproxy | 10.000           | 07/01/2022 00:00~07/31/2022 23:59 |
| example-org      | test            | customers-apiproxy | 1.000.000        | 07/01/2022 00:00~07/31/2022 23:59 |
| example-org      | prod            | customers-apiproxy | 10.000.000       | 07/01/2022 00:00~07/31/2022 23:59 |
| example-org      | dev             | payments-apiproxy  | 100.000          | 07/01/2022 00:00~07/31/2022 23:59 |
| example-org      | test            | payments-apiproxy  | 10.000.000       | 07/01/2022 00:00~07/31/2022 23:59 |
| example-org      | prod            | payments-apiproxy  | 100.000.000      | 07/01/2022 00:00~07/31/2022 23:59 |
