"""Clase para importar, modificar y guardar archivos CSV usando la librería nativa csv."""
from __future__ import annotations
import csv
from pathlib import Path


class ManejadorCSV:
    """Gestiona la lectura, modificación y escritura de archivos CSV."""

    def __init__(self, ruta_entrada: str | Path) -> None:
        self.ruta_entrada = Path(ruta_entrada)
        self.encabezados: list[str] = []
        self.datos: list[list[str]] = []
        self.modificaciones: list[str] = []

    def importar_csv(self) -> list[list[str]]:
        """Importa los datos del archivo CSV usando csv.reader."""
        with open(self.ruta_entrada, mode="r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)
            self.datos = [fila for fila in lector]
        return self.datos

    def actualizar_celda(self, fila_idx: int, nombre_columna: str, nuevo_valor: str) -> None:
        """Actualiza el valor de una celda específica por fila y nombre de columna."""
        col_idx = self.encabezados.index(nombre_columna)
        valor_anterior = self.datos[fila_idx][col_idx]
        self.datos[fila_idx][col_idx] = str(nuevo_valor)
        self.modificaciones.append(
            f"Actualización en fila {fila_idx}, columna '{nombre_columna}': '{valor_anterior}' -> '{nuevo_valor}'"
        )

    def agregar_fila(self, nueva_fila: list[str]) -> None:
        """Agrega un nuevo registro al final del CSV."""
        if len(nueva_fila) != len(self.encabezados):
            raise ValueError("La fila nueva debe tener la misma cantidad de columnas que los encabezados.")
        self.datos.append([str(item) for item in nueva_fila])
        self.modificaciones.append(f"Registro agregado en CSV: {nueva_fila[0]} ({nueva_fila[1]})")

    def guardar_csv(self, ruta_salida: str | Path) -> Path:
        """Guarda los datos modificados en un nuevo archivo CSV con encabezados usando csv.writer."""
        salida = Path(ruta_salida)
        salida.parent.mkdir(parents=True, exist_ok=True)
        with open(salida, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.datos)
        return salida