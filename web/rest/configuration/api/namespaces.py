from configuration.extensions.api_extension import api, authorizations

auth_ns = api.namespace("auth", description="Stock Flow operations")
profitProphet_ns = api.namespace(
    "stockflow",
    description="Stock Flow operations",
    authorizations=authorizations,
)
