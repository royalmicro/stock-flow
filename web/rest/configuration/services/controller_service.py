import importlib
import os
from flask import Flask


class Controller:
    """
    A class used to import all controller modules dynamically from a specified directory.

    Attributes
    ----------
    root_path : str
        The root path of the application where the controllers are located.
    """

    def __init__(self, app: Flask) -> None:
        self.root_path = app.config["ROOT_PATH"]
        self.__import_controllers()

    def __import_controllers(self):
        # Path to the controllers directory
        controllers_path = f"{self.root_path}/application/controller"

        # Get a list of all files in the controllers directory
        for file in os.listdir(controllers_path):
            if file.endswith(".py") and file != "__init__.py":
                # Module name is the file name without the .py extension
                module_name = file[:-3]
                # Full module name includes the package path
                full_module_name = f"application.controller.{module_name}"
                # Import the module dynamically
                importlib.import_module(full_module_name)
