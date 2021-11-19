import React, { useEffect, useState } from "react";

const HospForm = ({ active, handleModal, token, id, setErrorMessage }) => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [maidenName, setMaidenName] = useState("");

  //const [birthdayDate, setBirthdayDate] = useState("");
  const [birthdayDay, setBirthdayDay] = useState("");
  const [birthdayMonth, setBirthdayMonth] = useState("");
  const [birthdayYear, setBirthdayYear] = useState("");

  const [email, setEmail] = useState("");

  const [numberAddress, setNumberAddress] = useState("")
  const [nameAddress, setNameAddress] = useState("")
  const [postalCode, setPostalCode] = useState("")
  const [cityAddress, setCityAddress] = useState("")
  const [countryAddress, setCountryAddress] = useState("")
  
  const [secuNumber, setSecuNumber] = useState("")

  const [hospitalName, setHospitalName] = useState("")
  const [causeHosp, setCauseHosp] = useState("")


  useEffect(() => {
    const getPatientForm = async () => {
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token,
        },
      };
      const response = await fetch(`/hospForm/form/${id}`, requestOptions);

      if (!response.ok) {
        setErrorMessage("Questionnaire non disponible !");
      } else {
        const data = await response.json();
        setFirstName(data.first_name);
        setLastName(data.last_name);
        setMaidenName(data.maiden_name);

        //setBirthdayDate(data.birthday_date);
        setBirthdayDay(data.birthdayDay);
        setBirthdayMonth(data.birthdayMonth);
        setBirthdayYear(data.birthdayYear);
        
        setEmail(data.email);

        setNumberAddress(data.numberAddress);
        setNameAddress(data.nameAddress);
        setPostalCode(data.postalCode);
        setCityAddress(data.cityAddress);
        setCountryAddress(data.countryAddress);

        setSecuNumber(data.secuNumber);

        setHospitalName(data.hospitalName);
        setCauseHosp(data.causeHosp);
      }
    };

    if (id) {
      getPatientForm();
    }
  }, [id, token]);

  const cleanFormData = () => {
    setFirstName("");
    setLastName("");
    setMaidenName("");

    //setBirthdayDate("");
    setBirthdayDay("");
    setBirthdayMonth("");
    setBirthdayYear("");


    setEmail("");

    setNumberAddress("");
    setNameAddress("");
    setPostalCode("");
    setCityAddress("");
    setCountryAddress("");

    setSecuNumber("");

    setHospitalName("");
    setCauseHosp("");
    
  };

  const handleCreateLead = async (e) => {
    e.preventDefault();
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
      body: JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        maiden_name: maidenName,

        //birthday_date: birthdayDate,
        birthdayDay: birthdayDay,
        birthdayMonth: birthdayMonth,
        birthdayYear: birthdayYear,

        email: email,

        numberAddress: numberAddress,
        nameAddress: nameAddress,
        postalCode: postalCode,
        cityAddress: cityAddress,
        countryAddress: countryAddress,

        secuNumber: secuNumber,

        hospitalName: hospitalName,
        causeHosp: causeHosp,
      }),
    };
    const response = await fetch("/hospForm/form", requestOptions);
    if (!response.ok) {
      setErrorMessage("Une erreur a été détectée lors de la création du formulaire");
    } else {
      cleanFormData();
      handleModal();
    }
  };

  const handleUpdateLead = async (e) => {
    e.preventDefault();
    const requestOptions = {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
      body: JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        maiden_name: maidenName,

        //birthday_date: birthdayDate,
        birthdayDay: birthdayDay,
        birthdayMonth: birthdayMonth,
        birthdayYear: birthdayYear,

        email: email,

        numberAddress: numberAddress,
        nameAddress: nameAddress,
        postalCode: postalCode,
        cityAddress: cityAddress,
        countryAddress: countryAddress,

        secuNumber: secuNumber,

        hospitalName: hospitalName,
        causeHosp: causeHosp,
      }),
    };
    const response = await fetch(`/hospForm/form/${id}`, requestOptions);
    if (!response.ok) {
      setErrorMessage("Une erreur a été détectée lors du chargement du formulaire");
    } else {
      cleanFormData();
      handleModal();
    }
  };

  return (
    <div className={`modal ${active && "is-active"}`}>
      <div className="modal-background" onClick={handleModal}></div>
      <div className="modal-card">
        <header className="modal-card-head has-background-primary-light">
          <h1 className="modal-card-title">
            {id ? "Télécharger un formulaire" : "Créer un formulaire"}
          </h1>
        </header>
        <section className="modal-card-body">
          <form>
            <div className="field">
              <label className="label">Prénom</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Entrez votre prénom"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  className="input"
                  required
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Nom de famille</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Entrez votre nom de famille"
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                  className="input"
                  required
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Nom précédent</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Entrez votre nom de jeune fille"
                  value={maidenName}
                  onChange={(e) => setMaidenName(e.target.value)}
                  className="input"
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Jour de naissance</label>
              <div className="control">
                <input
                  type="int"
                  placeholder="JJ"
                  value={birthdayDay}
                  onChange={(e) => setBirthdayDay(e.target.value)}
                  className="input"
                  required               
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Mois de naissance</label>
              <div className="control">
                <input
                  type="int"
                  placeholder="MM"
                  value={birthdayMonth}
                  onChange={(e) => setBirthdayMonth(e.target.value)}
                  className="input"
                  required               
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Année de naissance</label>
              <div className="control">
                <input
                  type="int"
                  placeholder="YYYY"
                  value={birthdayYear}
                  onChange={(e) => setBirthdayYear(e.target.value)}
                  className="input"
                  required               
                  />
              </div>
            </div>
            <div className="field">
              <label className="label">Email</label>
              <div className="control">
                <input
                  type="email"
                  placeholder="Enter email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="input"
                  required               
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Numéro de rue</label>
              <div className="control">
                <input
                  type="int"
                  placeholder="Entrez votre numéro de rue"
                  value={numberAddress}
                  onChange={(e) => setNumberAddress(e.target.value)}
                  className="input"
                  required               
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Nom de rue</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Entrez votre nom de rue"
                  value={nameAddress}
                  onChange={(e) => setNameAddress(e.target.value)}
                  className="input"
                  required 
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Code Postal</label>
              <div className="control">
                <input
                  type="int"
                  placeholder="Entrez votre code postal"
                  value={postalCode}
                  onChange={(e) => setPostalCode(e.target.value)}
                  className="input"
                  required 
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Ville de résidence</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Entrez votre ville de résidence"
                  value={cityAddress}
                  onChange={(e) => setCityAddress(e.target.value)}
                  className="input"
                  required 
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Pays de résidence</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Entrez votre pays de résidence"
                  value={countryAddress}
                  onChange={(e) => setCountryAddress(e.target.value)}
                  className="input"
                  required 
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Numéro de sécurité sociale</label>
              <div className="control">
                <input
                  type="int"
                  placeholder="Entrez votre numéro de sécurité sociale"
                  value={secuNumber}
                  onChange={(e) => setSecuNumber(e.target.value)}
                  className="input"
                  required 
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Nom de l'hopital</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Entrez le nom de l'hopital"
                  value={hospitalName}
                  onChange={(e) => setHospitalName(e.target.value)}
                  className="input"
                  required 
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Cause de votre visite</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Entrez la cause de votre visite"
                  value={causeHosp}
                  onChange={(e) => setCauseHosp(e.target.value)}
                  className="input"
                  required 
                />
              </div>
            </div>
          </form>
        </section>
        <footer className="modal-card-foot has-background-primary-light">
          {id ? (
            <button className="button is-info" onClick={handleUpdateLead}>
              Update
            </button>
          ) : (
            <button className="button is-primary" onClick={handleCreateLead}>
              Create
            </button>
          )}
          <button className="button" onClick={handleModal}>
            Cancel
          </button>
        </footer>
      </div>
    </div>
  );
};

export default HospForm;
