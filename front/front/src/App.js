import React from "react";
import { Switch, Route, Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

import AddPost from "../../front/src/components/add_post";
import Post from "../../front/src/components/post";
import PostsList from "../../front/src/components/posts_lists";

function App() {
  return (
    <div>
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <a href="/posts" className="navbar-brand">
          Data Full Stack App
        </a>
        <div className="navbar-nav mr-auto">
          <li className="nav-item">
            <Link to={"/posts"} className="nav-link">
              Posts
            </Link>
          </li>
          <li className="nav-item">
            <Link to={"/add"} className="nav-link">
              Add
            </Link>
          </li>
        </div>
      </nav>

      <div className="container mt-3">
        <Switch>
          <Route exact path={["/", "/posts"]} component={PostsList} />
          <Route exact path="/add" component={AddPost} />
          <Route path="/posts/:id" component={Post} />
        </Switch>
      </div>
    </div>
  );
}

export default App;