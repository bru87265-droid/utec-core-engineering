#!/usr/bin/env python3
"""Defina una función que añade texto a un archivo."""


def append_write(filename="", text=""):
    """Añade una cadena al final de un archivo UTF-8."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
