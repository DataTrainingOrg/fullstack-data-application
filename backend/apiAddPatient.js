export default class apiAddPatient{

    static InsertPatient(body){
        return fetch(http://localhost:5000/signup,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify(body)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }

}