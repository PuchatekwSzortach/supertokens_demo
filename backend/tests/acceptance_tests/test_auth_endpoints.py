"""
Tests for auth endpoints
"""


def test_registration(clean_supertokens_data, test_client):
    """
    Test user registration
    """

    _ = clean_supertokens_data

    # Register a user

    response = test_client.post(
        "/auth/signup",
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

    assert response.status_code == 200
    assert response.json["status"] == "OK"
