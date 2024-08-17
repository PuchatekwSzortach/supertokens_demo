import os

import flask
import flask_cors

import supertokens_python

import supertokens_python.framework.flask
import supertokens_python.recipe.multitenancy.syncio
import supertokens_python.recipe.session
import supertokens_python.recipe.session.framework.flask

import config


supertokens_python.init(
    supertokens_config=config.supertokens_config,
    app_info=config.app_info,
    framework=config.framework,
    recipe_list=config.recipe_list,
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


@app.route("/sessioninfo", methods=["GET"])  # type: ignore
@supertokens_python.recipe.session.framework.flask.verify_session()
def get_session_info():
    session_ = flask.g.supertokens
    return flask.jsonify(
        {
            "sessionHandle": session_.get_handle(),
            "userId": session_.get_user_id(),
            "accessTokenPayload": session_.get_access_token_payload(),
        }
    )


@app.route('/user-info', methods=['GET'])
@supertokens_python.recipe.session.framework.flask.verify_session()
def get_user_info():

    session: supertokens_python.recipe.session.SessionContainer = flask.g.supertokens

    return flask.jsonify({
        "data": "nothing here yet",
        "userId": session.get_user_id()
    })



@app.route("/tenants", methods=["GET"])  # type: ignore
def get_tenants():
    tenantReponse = supertokens_python.recipe.multitenancy.syncio.list_all_tenants()

    tenantsList = []

    for tenant in tenantReponse.tenants:
        tenantsList.append(tenant.to_json())

    return flask.jsonify({
        "status": "OK",
        "tenants": tenantsList,
    })


@app.route('/update-jwt', methods=['POST'])
@supertokens_python.recipe.session.framework.flask.verify_session()
def like_comment():
    session: supertokens_python.recipe.session.SessionContainer = flask.g.supertokens

    _ = session.get_user_id()


# This is required since if this is not there, then OPTIONS requests for
# the APIs exposed by the supertokens' Middleware will return a 404
@app.route("/", defaults={"u_path": ""})  # type: ignore
@app.route("/<path:u_path>")  # type: ignore
def catch_all(u_path: str):  # pylint: disable=unused-argument
    flask.abort(404)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
