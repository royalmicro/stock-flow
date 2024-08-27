from flask_restx import fields
from configuration.extensions.api_extension import api

auth_model = api.model(
    "Auth",
    {
        "username": fields.String,
        "password": fields.String,
    },
)

user_model = api.model(
    "User",
    {
        "id": fields.Integer,
        "username": fields.String,
    },
)

login_model = api.model(
    "Login",
    {
        "token": fields.String,
        "user": fields.Nested(
            api.model(
                "User",
                {
                    "id": fields.Integer(required=True, description="User ID"),
                    "username": fields.String(required=True, description="Username"),
                },
            )
        ),
    },
)
