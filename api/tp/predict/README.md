# Prediction

Le but de se TP est de mettre en production un modèle de machine Learning. Pour rendre un modèle utilisable par des clients externes il faut le servir derrière une API.

- Loader un modele
- Route de prédict
- Route de re training avec background task
- Route de feedback
- Monitoring ?

## Loader le modèle

Nous utiliserons la même méthode que pour la création du schéma, nous allons écoute l'event `startup`. Et loader le modèle à ce moment là.

```python
@app.on_event('startup')
async def load_model():
    global clf
    all_model_paths = glob.glob("./data/iris_*")
    last_model = sorted(all_model_paths, reverse=True)[0]
    clf = load(last_model)
```

Il ne faut pas oublier de spécifier le mot clé global devant clf qui permet de rendre accessible cet objet de manière globale dans le projet.

on a ajouté une petite mécanique afin de récupérer toujours le dernier modèle entrainé. La mécanique permet de récupérer l'ensemble des modèles stockés et ensuite de récupérer le plus récent.

Ensuite nous avons besoin de créer un schéma permettant de lire les données provenant de l'exterieur. Ces données doivent être comptatible avec le format attendu par le modèle.

```python
from pydantic import BaseModel
from typing import List


class IrisPredict(BaseModel):
    data: List[float]
```

Dans ce cas, on ne demande uniquement une liste de float representant les différentes features. Ici dans l'ordre `['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']` 

Il nous suffit ensuite d'utiliser ce schema en entré d'une route qui permettra de renvoyer le résultat.

```python
@app.post("/iris/predict")
async def create_post(iris: IrisPredict):
    return {
        "predicted_classes" : clf.predict(np.asarray([iris.data])).tolist(),
        "predicted_probas" : clf.predict_proba(np.asarray([iris.data])).tolist(), 
        "classes" : CLASSES
    }
```

### Ré-entrainement avec Background task

### Route de feedback


## Exercices

1. Changer le type de donnée attendu en entré de la route pour envoyer un json avec les features nommée et plus une liste de floats.

2. Ajouter un autre modèle à l'API avec un modèle de votre choix que vous avez potentiellement déjà utilisé en cours.

3. 