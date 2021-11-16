import logo from './logo.svg';
import './App.css';
//import Webpages from './webpage';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Cette application a pour objectif de fluidifier la prise en charge de patients dans les hopitaux. Chaque patient doit remplir un formulaire (E112) dès son arrivée aux urgences.
          Ce formulaire peut être virtuel et utiliser une auto-complétion pour faciliter la prise en charge et les soins des patients.
        </p>
        <p>
          Il existe un formulaire (trouvable et remplissable sur internet) qui regroupe différentes prises en charge. Cependant, ce formulaire n'est pas optimisé, et ne prodigue aucune auto-complétion.
        </p>
        <a
          className="App-link"
          href="https://www.kvg.org/api/rm/EES95SG28X64996/versicherer-koordinationsrecht-dokumente-e112-fr.pdf"
          target="_blank"
          rel="noopener noreferrer"
        >
          Voir à quoi ressemble ce formulaire, version papier
        </a>
        <p></p>
        <a
          className="App-link"
          href="/signin"
          target="_blank"
          rel="noopener noreferrer"
        >
          C'est parti pour remplir ce formulaire, version numérique !
        </a>
      </header>
      <body>
      </body>
    </div>
  );
}

/*function Apps() {
  return (
    <div>
      <Webpages />
    </div>
  );
}*/

export default App;
