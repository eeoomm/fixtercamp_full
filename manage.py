#!/usr/bin/env python
#Que informacion quieres 
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hola_mundo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
