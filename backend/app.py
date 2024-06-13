from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session

import flask

from flask_cors import CORS
from supertokens_python.framework.flask import Middleware
from supertokens_python import get_all_cors_headers


init(
    app_info=InputAppInfo(
        app_name="supertokens_demo",
        api_domain="http://localhost:10003",
        website_domain="http://localhost:10002",
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    supertokens_config=SupertokensConfig(
        connection_uri="http://supertokens:3567",
        # api_key=<API_KEY(if configured)>
    ),
    framework='flask',
    recipe_list=[
        session.init(), # initializes session features
        emailpassword.init()
    ]
)

app = flask.Flask("supertokens_backend")
Middleware(app)


CORS(
    app=app,
    origins=[
        "http://localhost:10002"
    ],
    supports_credentials=True,
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)


# This is required since if this is not there, then OPTIONS requests for
# the APIs exposed by the supertokens' Middleware will return a 404
@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path: str):
    flask.abort(404)


@app.route("/home")
def home():
    return "Hello, home!"


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
