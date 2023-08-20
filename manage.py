#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    # Configuración del entorno Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        # Intenta importar Django
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            # Intenta importar el módulo Django
            import django
        except ImportError:
            # Mostrar un mensaje de error detallado si no se encuentra Django
            raise ImportError(
                "Couldn't import Django. Make sure it's installed and "
                "available on your PYTHONPATH environment variable. Did you "
                "forget to activate a virtual environment?"
            )
        # Si se importó Django pero no se pudo importar el módulo, levanta la excepción
        raise

    # Agregar la ruta al directorio django_project_template al PYTHONPATH
    current_path = Path(__file__).parent.resolve()
    sys.path.append(str(current_path / "django_project_template"))

    # Ejecutar el comando de línea de comandos de Django
    execute_from_command_line(sys.argv)
