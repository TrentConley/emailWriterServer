#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

key = ''
# Open the keys.txt file in read-only mode
with open("../keys.txt", "r") as f:
    # Read the contents of the file and store it in the key variable
    key = f.read()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
