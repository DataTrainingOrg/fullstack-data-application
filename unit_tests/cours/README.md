# Tests unitaires

## Pourquoi écrire des tests unitaires ?

Quand on commence à écrire du code, généralement, il fonctionne très bien. On l'a testé nous-mêmes assez facilement et on ne rencontre aucun bug. 
Mais, au fur et à mesure que le code évolue, il devient de plus en plus difficile de tout tester "à la main". 
Lorsque notre application s'aggrandit, certains bout de code vont etre partagés entre des certaines, classes, fonctions, point d'API, etc.
Si on effectue une modification dans un de ces bout de code, on ne peut pas être sûr que cela n'aura pas d'impact sur le reste de l'application.
Les tests unitaires permettent de vérifier que le code fonctionne toujours correctement, même après des modifications.

## Qu'est-ce qu'un test unitaire ?

Un test unitaire est un morceau de code qui teste une autre partie de code.
Il est écrit pour vérifier que le code fonctionne correctement. En général, il s'agit de tester une fonction ou une méthode individuelle pour s'assurer qu'elle produit le résultat attendu dans des conditions spécifiques.
L'objectif est de :
- s'assurer que chaque unité de code fonctionne comme prévu.
- détecter les erreurs et les bugs dans le code avant qu'ils n'apparaissent en situation réelle.
- faciliter la maintenance du code en permettant de vérifier que les modifications apportées n'ont pas d'impact sur le reste de l'application (non-regression).
- documenter le code en fournissant des exemples d'utilisation.

## Comment écrire un test unitaire ?

Pour écrire un test unitaire, il faut :
- définir un cas de test : c'est une situation particulière dans laquelle on va tester le code.
- exécuter le code à tester avec les paramètres du cas de test.
- vérifier que le résultat obtenu est celui attendu.
- si le résultat obtenu est différent de celui attendu, le test échoue.

Un test unitaire doit pouvoir être exécuté de manière automatique, sans intervention humaine. 
Il doit être reproductible, c'est-à-dire qu'il doit donner le même résultat à chaque exécution (déterministe).
Il doit être indépendant des autres tests, c'est-à-dire qu'il ne doit pas dépendre du résultat d'un autre test pour fonctionner.
Enfin, un test unitaire doit être rapide à exécuter. Lorsque notre application grandit, le nombre de tests unitaires va augmenter. 
Il est donc important que ces tests s'exécutent rapidement pour ne pas ralentir le développement.

## Exemple de test unitaire

Voici un exemple de test unitaire:
Imaginons que j'ai une fonction `addition` qui prend deux paramètres `a` et `b` et qui retourne la somme de ces deux paramètres.

```python

def addition(a: int, b: int) -> int:
    return a + b

```

Un test unitaire pour cette fonction pourrait ressembler à ceci:

```python
def test_addition():
    assert addition(1, 2) == 3
```

Ici, mon cas de test est l'addition de deux entiers positifs.
Je veux pouvoir aussi m'assurer que l'addition de deux entiers négatifs fonctionne correctement.
Dans ce cas j'ajouterai un deuxième test:

```python
def test_addition_negative_number():
    assert addition(-1, -2) == -3
```

## Frameworks de tests unitaires

Il existe de nombreux frameworks de tests unitaires pour de nombreux langages de programmation.
En Python, le framework de test unitaire le plus utilisé est `unittest`.
`unittest` est un module de la bibliothèque standard de Python qui permet d'écrire des tests unitaires.
Il fournit des classes et des méthodes pour créer des cas de test, exécuter les tests et vérifier les résultats.

Il existe également d'autres frameworks de tests unitaires pour Python, tels que `pytest`, `nose`, `doctest`, etc.

### Pytest

`pytest` est un framework de test unitaire pour Python qui est plus simple et plus flexible que `unittest`.
Il permet d'écrire des tests de manière plus concise et plus lisible.
Il fournit également des fonctionnalités supplémentaires telles que la découverte automatique des tests, la paramétrisation des tests, les fixtures, etc.

