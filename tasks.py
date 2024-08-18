""""
Invoke commands to be run from the host
"""

import invoke


@invoke.task
def login_flow(_context):
    """
    Command calling server with a few basic authentication requests

    Args:
        _context (invoke.Context): context instance
    """

    import icecream
    import requests

    host = "http://localhost:10010"

    with requests.Session() as session:

        response = session.post(
            f"{host}/auth/signin",
            headers={
                "rid": "emailpassword"
            },
            json={
                "formFields": [
                    {"id": "email", "value": "test@example.com"},
                    {"id": "password", "value": "test1234"}
                ]
            }
        )

        access_token = response.headers['st-access-token']

        # Call protected endpoint
        response = session.get(
            f"{host}/user-info",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        icecream.ic(response.request.path_url)
        icecream.ic(response.status_code)
        icecream.ic(response.json())
