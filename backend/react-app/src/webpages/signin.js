import React, { Component } from 'react';
import './App.css';

class Signin extends Component {
  render(){
    return (
      <form>
        <fieldset>

         <label for = "email">email</label><br/>
         <input type = "text" name = "email" placeholder = "email" /><br/>

         <label for = "PIN">mot de passe</label><br/>
         <input type = "text" name = "pin" placeholder = "pin" /><br/>

         <input type = "submit" value = "Submit" />

        </fieldset>
      </form>
    )
  }
}
export default Signin