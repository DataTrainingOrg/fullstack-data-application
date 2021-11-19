import React, { useContext, useEffect, useState } from "react";

import Register from "./components/Register";
import Login from "./components/Login";
import Header from "./components/Header";
import Table from "./components/Table";
import { UserContext } from "./context/UserContext";
import PrincipalPage from "./components/pageprincipale" 

const App = () => {
  const [message, setMessage] = useState("");
  const [token] = useContext(UserContext);

  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("/hospForm", requestOptions);
    const data = await response.json();

    if (!response.ok) {
      console.log("Quelque chose s'est mal passé");
    } else {
      setMessage(data.message);
    }
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <>
      <Header title={message} />
        <div className="column"></div>
        
          {!token ? (
            <div>< PrincipalPage />
            <div className="columns">
              <Register /> <Login />
            </div>
          </div>
          ) : (
            <Table />
          )}
        
        <div className="column"></div>

    </>
  );
};

export default App;
