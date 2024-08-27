from flask import Flask

from configuration.extensions.db_extension import db
from configuration.extensions.migration_extension import Migration
from configuration.extensions.api_extension import api
from configuration.extensions.jwt_extension import jwt_manager
from configuration.extensions.marshmallow_extension import marshmallow

# Initialize extensions
migration = Migration()


def init(app: Flask):

    db.init_app(app)
    migration.init_migration(app, db)
    marshmallow.init_app(app)
    jwt_manager.init_app(app)

    from configuration.api.namespaces import profitProphet_ns
    from configuration.api.namespaces import auth_ns
    from configuration.api.models import auth_model

    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(profitProphet_ns, path="/")

    api.add_model("Auth", auth_model)

    api.init_app(app)
