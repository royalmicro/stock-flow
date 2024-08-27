import importlib
import os
from flask import Flask
from injector import Binder, singleton

from configuration.services.utils import (
    convert_path_to_module,
    split_and_capitalize,
)


class Application:
    """
    A class to handle the loading and binding of application service modules.

    Attributes
    ----------
    application_file_names : list[str]
        A list of paths to application service files.
    application_modules : list[dict[str, any]]
        A list of imported application service modules.

    Methods
    -------
    bind_applications(binder: Binder)
        Binds application service classes to themselves using the provided binder.
    """

    application_file_names: list[str] = []
    application_modules: list[dict[str, any]] = []

    def __init__(self, app: Flask) -> None:
        self.root_path = app.config["ROOT_PATH"]
        self.__import_application_modules()

    def bind_applications(self, binder: Binder):
        for application in self.application_modules:
            application_key = next(iter(application))
            application_value = application[application_key]
            application_class = getattr(application_value, application_key)
            binder.bind(
                interface=application_class, to=application_class, scope=singleton
            )

    def __import_application_modules(self):
        repositories_services_path = f"{self.root_path}/application/services"

        for root, dirs, files in os.walk(repositories_services_path):
            if "__pycache__" in dirs:
                dirs.remove("__pycache__")  # don't visit __pycache__ directories
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    module_name = os.path.splitext(file)[0]
                    full_module_name = convert_path_to_module(os.path.join(root, file))

                    module = importlib.import_module(full_module_name)
                    module_name = split_and_capitalize(module_name)
                    self.application_modules.append({module_name: module})
