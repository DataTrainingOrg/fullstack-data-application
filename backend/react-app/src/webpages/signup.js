import React, { Component } from 'react'
import './App.css';

class Signup extends Component {
 
  render() {
    return (
      <form>
        <fieldset>

          <label for="name">Enter your name: </label>
          <input type="text" id="name" /><br/><br/>

          <label for="age">Enter your birthdate </label>
          <input type="date" id="age" min='1'/><br/><br/>

         <label for = "email">email</label><br/>
         <input type = "text" name = "email" placeholder = "email" /><br/>

         <label for = "city">city</label><br/>
         <input type = "text" name = "city" placeholder = "city" /><br/>

         <label for = "addr">addr</label><br/>
         <input name = "addr" placeholder = "addr"></input><br/>

         <label for = "PIN">numéro de sécu</label><br/>
         <input type = "text" name = "pin" placeholder = "pin" /><br/>

         <label for = "PIN">mot de passe</label><br/>
         <input type = "text" name = "pin" placeholder = "pin" /><br/>

         <input type = "submit" value = "Submit" />

        </fieldset>
      </form>
    )
  }
}
export default Signup