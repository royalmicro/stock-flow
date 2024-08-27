import importlib
import os
import fnmatch

from flask import Flask
from injector import Binder, singleton

from configuration.services.utils import (
    convert_path_to_module,
    split_and_capitalize,
)


class RepositoryService:
    """
    A class to handle the loading and binding of repository modules and interfaces.

    Attributes
    ----------
    interface_files_names : list[str]
        A list of paths to interface files.
    repository_modules : list[dict[str, any]]
        A list of imported repository modules.
    repository_interface_modules : list[dict[str, any]]
        A list of imported repository interface modules.

    Methods
    -------
    bind_repositories(binder: Binder)
        Binds repository classes to their corresponding interfaces using the provided binder.
    """

    interface_files_names: list[str] = []
    repository_modules: list[dict[str, any]] = []
    repository_interface_modules: list[dict[str, any]] = []

    def __init__(self, app: Flask) -> None:
        self.root_path = app.config["ROOT_PATH"]
        self.__import_repository_modules()
        self.__include_repository_interface_names()
        for file_path in self.interface_files_names:
            self.__import_repository_interface_modules(file_path)

    def bind_repositories(self, binder: Binder):
        for repository in self.repository_modules:
            repository_key = next(iter(repository))
            repository_value = repository[repository_key]

            for interface in self.repository_interface_modules:
                interface_key = next(iter(interface))
                interface_value = interface[interface_key]

                if repository_key in interface_key:
                    repository_class = getattr(repository_value, repository_key)
                    interface_class = getattr(interface_value, interface_key)
                    binder.bind(
                        interface=interface_class, to=repository_class, scope=singleton
                    )

    def __include_repository_interface_names(self):
        domain_services_path = f"{self.root_path}/domain/model"
        for root, _, files in os.walk(domain_services_path):
            for file in files:
                if fnmatch.fnmatch(file, "*_interface.py"):
                    self.interface_files_names.append(os.path.join(root, file))

    def __import_repository_interface_modules(self, filepath: str):
        module_name = os.path.splitext(os.path.basename(filepath))[0]
        module_name = split_and_capitalize(module_name)

        full_module_name = convert_path_to_module(filepath)
        module = importlib.import_module(full_module_name)
        self.repository_interface_modules.append({module_name: module})

    def __import_repository_modules(self):
        repositories_services_path = f"{self.root_path}/infrastructure/persistence"

        # Get a list of all files in the controllers directory
        for file in os.listdir(repositories_services_path):
            if file.endswith(".py") and file != "__init__.py":
                module_name = file[:-3]
                full_module_name = f"infrastructure.persistence.{module_name}"
                module_name = split_and_capitalize(module_name)
                module = importlib.import_module(full_module_name)
                self.repository_modules.append({module_name: module})
