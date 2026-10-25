"""Tercera clase encargada de consolidar los resultados y generar el archivo resumen.txt."""
from __future__ import annotations
from pathlib import Path
from typing import Any


class GeneradorResumenTXT:
    """Recibe los resultados de las clases CSV y JSON y genera un reporte en .txt."""

    def __init__(self, ruta_salida: str | Path = "resumen.txt") -> None:
        self.ruta_salida = Path(ruta_salida)

    def generar_resumen(self, resultado_csv: dict[str, Any], resultado_json: dict[str, Any]) -> str:
        """Construye y guarda el archivo .txt con los datos reales de la ejecución."""
        lineas = [
            "RESUMEN DE EJECUCIÓN - EVIDENCIA DE APRENDIZAJE 2 (EA2)",
            "=" * 65,
            "",
            "1. PROCESAMIENTO DE ARCHIVO CSV",
            "-" * 35,
            f"URL de origen (Hugging Face): {resultado_csv['url_origen']}",
            f"Archivo original importado:   {resultado_csv['archivo_entrada']}",
            f"Nuevo archivo guardado en:    {resultado_csv['archivo_salida']}",
            f"Clase utilizada:              {resultado_csv['clase']}",
            f"Métodos invocados:            {', '.join(resultado_csv['metodos'])}",
            f"Total registros procesados:   {resultado_csv['total_registros']}",
            "Modificaciones aplicadas:",
            *[f"  * {mod}" for mod in resultado_csv["modificaciones"]],
            "",
            "2. PROCESAMIENTO DE ARCHIVO JSON",
            "-" * 35,
            f"URL de origen (Hugging Face): {resultado_json['url_origen']}",
            f"Archivo original importado:   {resultado_json['archivo_entrada']}",
            f"Nuevo archivo guardado en:    {resultado_json['archivo_salida']}",
            f"Clase utilizada:              {resultado_json['clase']}",
            f"Métodos invocados:            {', '.join(resultado_json['metodos'])}",
            f"Total registros procesados:   {resultado_json['total_registros']}",
            "Modificaciones aplicadas:",
            *[f"  * {mod}" for mod in resultado_json["modificaciones"]],
            "",
        ]

        texto_final = "\n".join(lineas)
        self.ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        with open(self.ruta_salida, mode="w", encoding="utf-8") as archivo:
            archivo.write(texto_final)

        return texto_final