""""
Configuration module for the Supertokens backend.
"""

from supertokens_python.recipe import emailpassword, session, dashboard
from supertokens_python import (
    InputAppInfo,
    SupertokensConfig,
)

# this is the location of the SuperTokens core.
supertokens_config = SupertokensConfig(
    connection_uri="http://supertokens:3567",
    api_key="some_key_I_made_up")

app_info = InputAppInfo(
    app_name="Supertokens",
    api_domain="http://localhost:10002",
    website_domain="http://localhost:10003",
)

framework = "flask"

# recipeList contains all the modules that you want to
# use from SuperTokens. See the full list here: https://supertokens.com/docs/guides
recipe_list = [
    session.init(),
    emailpassword.init(),
    dashboard.init(),
]
