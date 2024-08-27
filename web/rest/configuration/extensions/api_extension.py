from flask_restx import Api

authorizations = {
    "Bearer": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "bearerFormat": "JWT",
        "description": "Add a JWT with **Bearer &lt;JWT&gt;**",
    }
}

api = Api(
    title="Profit Prophet",
    description="Profit Prophet api documentation",
    security="Bearer",
    doc="/swagger/",
    authorizations=authorizations,
)
