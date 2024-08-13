Log in path: POST /auth/signin
Defined somewhere in backend
Returns 200 on failure though


During sign up check on email is done:
GET /auth/emailpassword/email/exists?email=boss@kuba.com HTTP/1.1"
Returns 200 if email doesn't exist


Signing up / registering seems to call endpoints on supertokens instance:
- POST /public/recipe/signup in supertokens
- POST /public/recipe/session in supertokens
- POST /auth/signup in backend


Log out/sign out calls:
- POST /recipe/session/remove in supertokens
- POST /auth/signout in backend

Log in calls:
- POST /public/recipe/signin in supertokens
- POST /auth/signin in backend

Ok, what do I do next?
Try to:
- check if new version of supertokens docker image was released and if so, update
- go through documentation on supertokens to try to understand each endpoint, its inputs and outputs
- do the same with backend, try to find implementation of endpoints being called in it
- go through frontend to find code that calls endpoints above
- try to build a script that would be able to sign in and retrieve information about a user


These seem to be apis of Core Driver Interface.
The backend should be calling these.
POST /public/recipe/signup
POST /public/recipe/session
POST /recipe/session/remove
