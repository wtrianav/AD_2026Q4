# AD_2026Q4 - Analítica de Datos

Repositorio colaborativo del curso **Analítica de Datos** (Ingeniería de Software y Datos). Contiene las clases reutilizables de Python, los flujos de trabajo en Jupyter Notebook y la generación automatizada de reportes `.txt` para las evidencias de aprendizaje (`EA1` y `EA2`).

## Estructura del Proyecto

```text
AD_2026Q4/
├── .github/workflows/
│   └── ejecucion-automatica.yml          # Ejecución automática de notebooks en GitHub Actions
├── src/clases_po/                        # Paquete de clases reutilizables (POO)
│   ├── __init__.py
│   ├── hf_loader.py                      # HFDatasetLoader: conexión a Hugging Face y exportación
│   └── reportes.py                       # Reportes: generación y guardado de resúmenes .txt
├── EA1/                                  # Evidencia de Aprendizaje 1: Carga y Transformación
│   ├── datos/
│   │   └── fast_food_restaurants.csv     # Dataset exportado desde Hugging Face
│   ├── reportes/
│   │   └── resumen_transformado.txt      # Resumen del DataFrame tras las 4 transformaciones
│   └── EA1_Carga_Transformacion.ipynb    # Notebook orquestador de la EA1
├── EA2/                                  # Evidencia de Aprendizaje 2: Manejo de CSV, JSON y TXT
│   ├── datos/
│   │   ├── original.csv                  # CSV descargado manualmente de Hugging Face
│   │   ├── modificado.csv                # Nuevo CSV generado con csv.writer
│   │   ├── original.json                 # JSON descargado manualmente de Hugging Face
│   │   └── modificado.json               # Nuevo JSON generado con json.dump
│   ├── manejador_csv.py                  # ManejadorCSV: lectura, modificación y guardado de CSV
│   ├── manejador_json.py                 # ManejadorJSON: lectura, modificación y guardado de JSON
│   ├── generador_resumen_txt.py          # GeneradorResumenTXT: consolidación del reporte final
│   ├── EA2_Manejo_Archivos.ipynb         # Notebook orquestador de la EA2
│   └── resumen.txt                       # Resumen de ejecución con URLs de origen y cambios
├── .gitignore
├── requirements.txt
└── README.md
```

## Requisitos Previos

* **Python 3.14.2** (configurado por defecto en el sistema: `python --version`).
* **Visual Studio Code** con las extensiones oficiales de **Python** y **Jupyter**.
* **Git** instalado para el control de versiones colaborativo.

---

## Instalación y Configuración del Entorno Local (VS Code)

Dado que **Python 3.14.2** ya es la versión predeterminada (`py --list` -> `-V:3.14 *`), ejecuta los siguientes comandos desde la terminal integrada de VS Code en la raíz del repositorio (`AD_2026Q4`):

### 1. Crear el entorno virtual

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual

* **En Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
* **En Windows (CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```
* **En Git Bash / Linux / GitHub Codespaces:**
  ```bash
  source .venv/bin/activate
  ```

Cuando el entorno se activa correctamente, el inicio de la línea en la terminal mostrará `(.venv)`.

### 3. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Ejecución de las Evidencias de Aprendizaje

### Evidencia 1 (`EA1`): Carga desde Hugging Face y Transformación con pandas
1. Abre el archivo `EA1/EA1_Carga_Transformacion.ipynb` en Visual Studio Code.
2. Selecciona el kernel **`.venv (Python 3.14.2)`** en la esquina superior derecha.
3. Ejecuta todas las celdas en orden (**Run All**):
   * Importa `HFDatasetLoader` y `Reportes` desde `src/clases_po`.
   * Descarga el dataset `JasonZhouTI/Fast_Food_Restaurants` desde Hugging Face y lo convierte en un `pandas.DataFrame`.
   * Aplica **4 transformaciones distintas** al DataFrame (limpieza de nulos, renombrado de columnas, filtrado condicional y selección/ordenamiento).
   * Genera y guarda el resumen estadístico y estructural en `EA1/reportes/resumen_transformado.txt`.

### Evidencia 2 (`EA2`): Manejo de Archivos CSV, JSON y TXT mediante Clases
1. Abre el archivo `EA2/EA2_Manejo_Archivos.ipynb` en Visual Studio Code.
2. Verifica que los archivos descargados manualmente de Hugging Face se encuentren en `EA2/datos/original.csv` y `EA2/datos/original.json`.
3. Ejecuta todas las celdas en orden (**Run All**):
   * Registra en variables las URL específicas de origen de Hugging Face para ambos formatos.
   * Importa y modifica los datos locales usando `ManejadorCSV` (`csv.reader` / `csv.writer`) y `ManejadorJSON` (`json.load` / `json.dump`), mostrando el antes y el después.
   * Guarda los archivos modificados en `EA2/datos/modificado.csv` y `EA2/datos/modificado.json` conservando los originales.
   * Invoca `GeneradorResumenTXT` para generar mediante código el archivo `EA2/resumen.txt` con las URLs de origen, clases/métodos usados, conteo de registros y detalle de las modificaciones.

---

## Autenticación en Hugging Face (Opcional para Datasets Privados)

Para descargar datasets públicos como `JasonZhouTI/Fast_Food_Restaurants` no se necesita un token. Si se utiliza un dataset privado o con condiciones de uso:

1. Inicia sesión en [Hugging Face](https://huggingface.co/) y abre [Settings > Access Tokens](https://huggingface.co/settings/tokens).
2. Selecciona **Create new token**, asigna un nombre (por ejemplo `AD_2026Q4`) con permiso **Read** y copia el token (`hf_...`).
3. Con el entorno virtual `.venv` activado, ejecuta en la terminal:
   ```bash
   hf auth login
   ```
   *(O `huggingface-cli login` en versiones anteriores de la CLI).*
4. Comprueba la sesión con:
   ```bash
   hf auth whoami
   ```

> **Seguridad:** Nunca escribas tokens directamente dentro de los archivos `.py` o `.ipynb` ni los subas a GitHub.

---

## Uso Manual de las Clases del Paquete `clases_po`

`HFDatasetLoader` recibe el identificador del dataset en Hugging Face, descarga la división indicada (`split`) y devuelve un `pandas.DataFrame`. Si se indica `filename`, también exporta el archivo en formato `csv`, `json`, `parquet` o `xlsx`.

```python
from clases_po import HFDatasetLoader, Reportes

loader = HFDatasetLoader(
    dataset_name="JasonZhouTI/Fast_Food_Restaurants",
    split="train",
    filename="EA1/datos/fast_food_restaurants.csv",
)
df = loader.load()

reportes = Reportes()
reportes.imprimir_reporte(df)
reportes.guardar_reporte(df, "EA1/reportes/resumen_transformado.txt")
```

Para ejecutar una prueba rápida desde la terminal en la raíz del proyecto:

* **En PowerShell (Windows):**
  ```powershell
  $env:PYTHONPATH="src"; python -c "from clases_po import HFDatasetLoader; df = HFDatasetLoader('JasonZhouTI/Fast_Food_Restaurants', max_rows=5).load(); print(df.head())"
  ```
* **En Bash (Linux / Codespaces / Git Bash):**
  ```bash
  PYTHONPATH=src python -c "from clases_po import HFDatasetLoader; df = HFDatasetLoader('JasonZhouTI/Fast_Food_Restaurants', max_rows=5).load(); print(df.head())"
  ```

También se puede indicar explícitamente el formato de exportación:

```python
loader = HFDatasetLoader(
    dataset_name="JasonZhouTI/Fast_Food_Restaurants",
    filename="EA1/datos/fast_food",
    file_type="parquet",
)
```