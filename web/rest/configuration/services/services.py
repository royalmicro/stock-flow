from injector import Binder
from flask import Flask
from configuration.services.application_service import Application
from configuration.services.controller_service import Controller
from configuration.services.repository_service import RepositoryService


class Services:
    """
    A class used to initialize and manage application services.

    Attributes
    ----------
    repository : RepositoryService
        The repository service used to handle data repositories.
    controller : Controller
        The controller service used to handle application controllers.
    application : Application
        The application service used to manage application-specific logic.

    Methods
    -------
    inject_services(binder: Binder):
        Injects the services into the given Binder instance for dependency injection.
    """

    root_path: str

    def __init__(self, app: Flask) -> None:
        self.repository = RepositoryService(app)
        self.controller = Controller(app)
        self.application = Application(app)

    def inject_services(self, binder: Binder):
        self.repository.bind_repositories(binder)
        self.application.bind_applications(binder)
