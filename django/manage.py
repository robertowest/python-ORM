#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "No se pudo importar Django. "
                "¿Está seguro de que está instalado y disponible en su variable de entorno PYTHONPATH? "
                "¿Olvidaste activar un entorno virtual?"
            )
        raise
    execute_from_command_line(sys.argv)
