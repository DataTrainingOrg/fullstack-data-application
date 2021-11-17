import './App.css';
import {
  BrowserRouter as Router,
  useRoutes,
} from "react-router-dom";

import PrincipalPage from './webpages/pageprincipale';
import Signup from './webpages/signup';
import Signin from './webpages/signin';
import Home from './webpages/home';


const App = () => {
  let routes = useRoutes([
    { path: "/", element: <PrincipalPage /> },
    { path: "/signup", element: <Signup /> },
    { path: "/signin", element: <Signin /> },
    { path: "/home", element: <Home /> },
  ]);
  return routes;
};

const AppWrapper = () => {
  return (
    <Router>
      <App />
    </Router>
  );
};

export default AppWrapper;