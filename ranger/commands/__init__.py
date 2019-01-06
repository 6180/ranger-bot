import os
import sys
import inspect

from importlib import import_module
from pprint import pprint

from command_registrar import CommandRegistrar as registrar


module_files = [filename.rsplit('.')[0] for filename in os.listdir('commands')
           if not filename.startswith('_')
           and (filename.endswith('.py') or os.path.isdir(f'{"commands:"}/{filename}'))]

for filename in module_files:
    __import__(f'commands.{filename}')

    clsmembers = inspect.getmembers(
        sys.modules[f'commands.{filename}'],
        inspect.isclass
    )

    for clsname, cls in clsmembers:
        cls._filename = filename
        registrar.register_command(cls)


print("Loaded command modules:")
pprint(registrar._commands.keys())
# XXX: get the list from the command registrar
