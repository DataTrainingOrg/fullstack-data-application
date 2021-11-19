import React, { useContext, useEffect, useState } from "react";

import ErrorMessage from "./ErrorMessage";
import HospForm from "./HospForm";
import { UserContext } from "../context/UserContext";

const Table = () => {
  const [token] = useContext(UserContext);
  const [patientforms, setPatientForms] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [loaded, setLoaded] = useState(false);
  const [activeModal, setActiveModal] = useState(false);
  const [id, setId] = useState(null);

  const handleUpdate = async (id) => {
    setId(id);
    setActiveModal(true);
  };

  const handleDelete = async (id) => {
    const requestOptions = {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
    };
    const response = await fetch(`/hospForm/form/${id}`, requestOptions);
    if (!response.ok) {
      setErrorMessage("Failed to delete lead");
    }

    getPatientForms();
  };

  const getPatientForms = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
    };
    const response = await fetch("/hospForm/form", requestOptions);
    if (!response.ok) {
      setErrorMessage("Something went wrong. Couldn't load the leads");
    } else {
      const data = await response.json();
      setPatientForms(data);
      setLoaded(true);
    }
  };

  useEffect(() => {
    getPatientForms();;
  }, []);

  const handleModal = () => {
    setActiveModal(!activeModal);
    getPatientForms();;
    setId(null);
  };

  return (
    <>
      <HospForm
        active={activeModal}
        handleModal={handleModal}
        token={token}
        id={id}
        setErrorMessage={setErrorMessage}
      />
      <button
        className="button is-fullwidth mb-5 is-primary"
        onClick={() => setActiveModal(true)}
      >
        Create a form
      </button>
      <ErrorMessage message={errorMessage} />
      {loaded && patientforms ? (
        <table className="table is-fullwidth">
          <thead>
            <tr>
              <th>Prénom</th>
              <th>Nom de famille</th>
              <th>Email</th>
              <th>Nom de l'hopital</th>
              <th>Raison de visite</th>
              <th>Date de visite</th>
            </tr>
          </thead>
          <tbody>
            {patientforms.map((patientform) => (
              <tr key={patientform.id}>
                <td>{patientform.first_name}</td>
                <td>{patientform.last_name}</td>
                <td>{patientform.email}</td>
                <td>{patientform.hospitalName}</td>
                <td>{patientform.causeHosp}</td>
                <td>{patientform.dateHosp}</td>
                <td>
                  <button
                    className="button mr-2 is-info is-light"
                    onClick={() => handleUpdate(patientform.id)}
                  >
                    Update
                  </button>
                  <button
                    className="button mr-2 is-danger is-light"
                    onClick={() => handleDelete(patientform.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Loading</p>
      )}
    </>
  );
};

export default Table;
