"""
Routes definitions
"""

import flask

import supertokens_python

import supertokens_python.framework.flask
import supertokens_python.recipe.multitenancy.syncio
import supertokens_python.recipe.session
import supertokens_python.recipe.session.framework.flask


BLUEPRINT = flask.Blueprint("net", __name__)


@BLUEPRINT.route("/sessioninfo", methods=["GET"])  # type: ignore
@supertokens_python.recipe.session.framework.flask.verify_session()
def get_session_info():
    """
    Endpoint for getting session information
    """
    session_ = flask.g.supertokens
    return flask.jsonify(
        {
            "sessionHandle": session_.get_handle(),
            "userId": session_.get_user_id(),
            "accessTokenPayload": session_.get_access_token_payload(),
        }
    )


@BLUEPRINT.route('/user-info', methods=['GET'])
@supertokens_python.recipe.session.framework.flask.verify_session()
def get_user_info():
    """
    Endpoint for getting user info
    """

    session: supertokens_python.recipe.session.SessionContainer = flask.g.supertokens

    return flask.jsonify({
        "data": "nothing here yet",
        "userId": session.get_user_id()
    })


@BLUEPRINT.route("/tenants", methods=["GET"])  # type: ignore
def get_tenants():
    """
    Endpoint for getting all tenants
    """

    tenantReponse = supertokens_python.recipe.multitenancy.syncio.list_all_tenants()

    tenantsList = []

    for tenant in tenantReponse.tenants:
        tenantsList.append(tenant.to_json())

    return flask.jsonify({
        "status": "OK",
        "tenants": tenantsList,
    })


# This is required since if this is not there, then OPTIONS requests for
# the APIs exposed by the supertokens' Middleware will return a 404
@BLUEPRINT.route("/", defaults={"u_path": ""})  # type: ignore
@BLUEPRINT.route("/<path:u_path>")  # type: ignore
def catch_all(u_path: str):  # pylint: disable=unused-argument
    """
    Catch all route returning 404
    """
    flask.abort(404)
