import React from 'react';
import './App.css';

import SuperTokens, { SuperTokensWrapper } from "supertokens-auth-react";
import EmailPassword from "supertokens-auth-react/recipe/emailpassword";
import Session from "supertokens-auth-react/recipe/session";

import {
  BrowserRouter,
  Routes,
} from "react-router-dom";

import { getSuperTokensRoutesForReactRouterDom } from "supertokens-auth-react/ui";
import { EmailPasswordPreBuiltUI } from 'supertokens-auth-react/recipe/emailpassword/prebuiltui';
import * as reactRouterDom from "react-router-dom";

SuperTokens.init({
  appInfo: {
      // learn more about this on https://supertokens.com/docs/thirdpartyemailpassword/appinfo
      appName: "supertokens_demo",
      apiDomain: "http://localhost:10003",
      websiteDomain: "http://localhost:10002",
      apiBasePath: "/auth",
      websiteBasePath: "/auth"
  },
  recipeList: [
      EmailPassword.init(),
      Session.init(),
  ]
});

class App extends React.Component {
  render() {
    return (
      <SuperTokensWrapper>
        <BrowserRouter>
          <Routes>
          {getSuperTokensRoutesForReactRouterDom(
            reactRouterDom, [EmailPasswordPreBuiltUI])}
          </Routes>
        </BrowserRouter>
      </SuperTokensWrapper>
    );
  }
}

export default App;
