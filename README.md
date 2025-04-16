# PTB-CLI (Procesamiento de transacciones bancarias - CLI)

## Introducción
Este programa permite el calculo de balance final, transaccion de mayor monto y Conteo de transacciones

## Requisitos basicos
- \> Python3.10 

## Instrucciones de ejecución

1. Verificar la version de Python instalada, mediante el comando `python --version` , de no tener instalado python o tener una menor version, instalar una version mas reciente a traves del siguiente enlace
   - https://www.python.org/downloads/

2. Copiar el repositorio mediante le siguiente comando en terminal

   - `git clone https://github.com/sadsandman/interbank-academy-25.git `

3. entrar en la carpeta del programa 
`cd interbank-academy-25`
4. Usar el script de instalacion segun el sistema operativo
   > Linux
   - convertir el script en ejecutable:
   
      `chmod +x setup.sh`
   - ejecutar el script `setup.sh`
   - Verificar con el comando de prueba 
   `.venv\Scripts\python ptb_cli\main.py report --file archivo.csv full-report`


   > Windows
   - ejecutar el script `setup.bat`
   -  Verificar con el comando de prueba 
   `.venv\Scripts\python ptb_cli\main.py report --file archivo.csv full-report`

   ***De requerir la instalacion manual, los comandos de instalacion estan dentro del los archivos setup respectivos**

## Enfoque y Solucion
Intente tomar un enfoque que permitiera la escalabilidad, intentando dejar abierta las siguientes posibilidades

- Implementacion de ejecutable con poetry
- Implementacion de nuevos comandos CLI
- Implementacion de mas tipos de analisis de datos, o nuevas funcionalidades

Tales consideraciones me indicaron a Typer para la generacion de la aplicacion, puesto que su escalabilidad y facilidad de manejo superan a argparse 

Como tal, se genero la siguiente linea de funcionamiento, explicado desde su comando de ejecucion:

`python main.py report --file .\test\data.csv full-report`

### Punto de inicio
main externo ./main.py, punto de acceso que llama a la app principal(main dentro de ptb_cli). el cual busca el comando que requiere ejecutar

en el caso de report, este contiene 3 puntos principales:
1. inicializacion de la variable global obtenida mediante la lectura del archivo csv
2. LLamado de funciones para el analisis de datos ligados a calculo de balance final, transaccion de mayor monto y Conteo de transacciones
3. Display de datos en consola

la razon del primer punto es que esto permite el uso de --help sin el uso de --file, lo cual hace mas intuitivo su uso, como ejemplo se puede ejecutar 

`python main.py report --help`

La razon de hacer una variable global es permitir su acceso a todas las funciones posteriores que se deseen implementar en el programa, dejando su inicializacion solamente a una funcion en el inicio de la ejecucion general

Para cada nueva funcion se puede permitir la creacion de diferentes archivos y funciones, teniendo en el programa las carpetas de utils oara diferente manejo de variables (como input/output(io) o analisis de datos(dataAnalisis.py)) , como la carptea commands, que permite agregar mas funcionalidades a futuro facilmente (expor-to-pdf , mas tipos de analisis, etc)

## Estructura de proyecto

<pre> 
ptb-cli/
├── ptb_cli/                    # Paquete principal del CLI
│   ├── main.py                 # Punto de entrada del CLI
│   ├── commands/               # Comandos
│   │   └── report.py           # Reporte general
│   └── utils/                  # Funciones auxiliares
│       ├── io.py               # Entrada de datos
│       └── dataAnalisis.py     # Analisis de datos
├── test/                       # Pruebas automáticas
│   └── data.csv                # Archivo csv de demo
│
├── .venv/                      # Entorno virtual (añadido a .gitignore)
├── .gitignore
├── README.md
├── requirements.txt            # Requisitos
├── setup.sh                    # Instalador para Linux
└── setup.bat                   # Instalador para Windows
 </pre>