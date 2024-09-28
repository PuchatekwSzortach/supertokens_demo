import EmailPassword from "supertokens-auth-react/recipe/emailpassword";
import Session from "supertokens-auth-react/recipe/session";

export const SuperTokensConfig = {
  appInfo: {
    appName: "SuperTokens Demo App",
    apiDomain: "http://localhost:10003",
    websiteDomain: "http://localhost:10002",
  },
  recipeList: [
    EmailPassword.init({
      useShadowDom: false,
    }),
    Session.init({
      tokenTransferMethod: "header"
    }),
  ],
};
