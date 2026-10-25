"""Clase para importar, modificar y guardar archivos JSON usando la librería nativa json."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any


class ManejadorJSON:
    """Gestiona la lectura, modificación y escritura de archivos JSON."""

    def __init__(self, ruta_entrada: str | Path) -> None:
        self.ruta_entrada = Path(ruta_entrada)
        self.datos: list[dict[str, Any]] = []
        self.modificaciones: list[str] = []

    def importar_json(self) -> list[dict[str, Any]]:
        """Importa un archivo JSON local usando json.load."""
        with open(self.ruta_entrada, mode="r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
            self.datos = contenido if isinstance(contenido, list) else [contenido]
        return self.datos

    def actualizar_registro(self, indice: int, clave: str, nuevo_valor: Any) -> None:
        """Actualiza el valor de una clave en un registro específico."""
        valor_anterior = self.datos[indice].get(clave)
        self.datos[indice][clave] = nuevo_valor
        self.modificaciones.append(
            f"Actualización en registro [{indice}], clave '{clave}': '{valor_anterior}' -> '{nuevo_valor}'"
        )

    def agregar_registro(self, nuevo_diccionario: dict[str, Any]) -> None:
        """Agrega un nuevo objeto/diccionario a la lista del JSON."""
        self.datos.append(nuevo_diccionario)
        self.modificaciones.append(f"Nuevo objeto agregado al JSON con claves: {list(nuevo_diccionario.keys())}")

    def guardar_json(self, ruta_salida: str | Path) -> Path:
        """Guarda la estructura modificada en un nuevo archivo JSON usando json.dump."""
        salida = Path(ruta_salida)
        salida.parent.mkdir(parents=True, exist_ok=True)
        with open(salida, mode="w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, indent=4, ensure_ascii=False)
        return salida