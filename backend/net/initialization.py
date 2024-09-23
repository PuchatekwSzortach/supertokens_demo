"""
Module with app initialization logic
"""


import flask
import flask_cors

import supertokens_python

import supertokens_python.framework.flask

import net.routes


def get_configured_app(configuration) -> flask.Flask:
    """
    Get a configured Flask app.

    Returns:
        flask.Flask: configured Flask app
    """

    supertokens_python.init(
        supertokens_config=configuration.supertokens_config,
        app_info=configuration.app_info,
        framework=configuration.framework,
        recipe_list=configuration.recipe_list,
    )

    app = flask.Flask(__name__)

    # TODO: should middlware be after or before cors?
    supertokens_python.framework.flask.Middleware(app)
    flask_cors.CORS(
        app=app,
        supports_credentials=True,
        origins="http://localhost:10002",
        allow_headers=["Content-Type"] + supertokens_python.get_all_cors_headers(),
    )

    app.register_blueprint(net.routes.BLUEPRINT)

    return app
