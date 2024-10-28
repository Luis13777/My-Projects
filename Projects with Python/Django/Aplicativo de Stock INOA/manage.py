#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "P_INOA.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # from app_INOA.scheduler import iniciar_agendador  # Importar a função de agendamento
    # iniciar_agendador()  # Iniciar o agendador

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
