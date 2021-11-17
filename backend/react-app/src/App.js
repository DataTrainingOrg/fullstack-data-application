import './App.css';
import {
  BrowserRouter as Router,
  useRoutes,
} from "react-router-dom";

import MyBooks from './webpages/mybooks';
import Favorites from './webpages/favorites';
import Home from './webpages/home';


const App = () => {
  let routes = useRoutes([
    { path: "/", element: <Home /> },
    { path: "/favorites", element: <Favorites /> },
    { path: "/mybooks", element: <MyBooks /> },
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