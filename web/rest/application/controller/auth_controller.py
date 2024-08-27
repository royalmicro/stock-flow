from flask_jwt_extended import create_access_token
from flask_restx import Resource, marshal_with
from injector import inject
from werkzeug.security import check_password_hash
from configuration.api.namespaces import auth_ns
from configuration.api.models import user_model, auth_model, login_model
from domain.utils.exceptions.domain_exception import DomainException
from infrastructure.persistence.user_repository import UserRepository


@auth_ns.route("/register")
class RgisterController(Resource):
    """
    Controller for handling user registration.

    This class defines the endpoint for user registration, allowing
    new users to create an account.
    """

    @inject
    def __init__(self, user_repository: UserRepository, *args, **kwargs):
        self.user_repository = user_repository
        super().__init__(*args, **kwargs)

    @auth_ns.expect(auth_model)
    @auth_ns.marshal_with(user_model, code=201)
    def post(self):
        user_data = auth_ns.payload
        user = self.user_repository.add(**user_data)
        return ({"id": user.get_id(), "username": user.get_username()}, 201)


@auth_ns.route("/login")
class LoginController(Resource):
    """
    Controller for handling user login.

    This class defines the endpoint for user login, allowing existing
    users to authenticate and receive an access token.
    """

    @inject
    def __init__(self, user_repository: UserRepository, *args, **kwargs):
        self.user_repository = user_repository
        super().__init__(*args, **kwargs)

    @marshal_with(login_model)
    @auth_ns.expect(auth_model)
    def post(self):
        try:
            user = self.user_repository.get_by_username(auth_ns.payload.get("username"))
            password = auth_ns.payload["password"]
        except DomainException as e:
            return {"error": str(e)}, 404

        if not check_password_hash(user.get_password_hash(), password):
            return {"error": "Incorrect password"}, 401

        return {
            "token": create_access_token(user.get_username()),
            "user": user.entity_to_dto(),
        }
