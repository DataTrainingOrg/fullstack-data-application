# TP

L'objectif du TP est d'apprendre les bases du frontend moderne.
Les exercices sont:
- d'apprendre et pratiquer la syntaxe JavaScript
- installer un framework au choix, client-side ou server-side
- depuis ce framework, consommer des APIs et afficher leurs résultats dans une page
- livrer le projet en production

## Préparation

- Installer l'environnement NodeJS comme indiqué dans le [cours](../FRONTEND.md), partie `Préparation > NodeJS > Environnement de développment`
- Lire la documentation sur les bases de JavaScript
- Installer un framework au choix, client-side ou server-side

## Exercices de JavaScript
  
1. Définir une fonction qui prend une string en paramètre et retourne la string en lettres majuscules
2. Définir une fonction qui prend deux paramètres: une array d'integer et un facteur de multiplication. La fonction doit retourner cette array avec chacun de ses élements multipliés par le facteur.<br>Exemple: array `[2, 7, 5, 3, 13, 11]` et multiplicateur `3`
3. Définir une fonction qui prend une array d'integer en paramètre. La fonction doit retourner un integer égal à la somme des éléments de cette array.
4. Définir une fonction qui prend une array en paramètre. La fonction doit afficher pour chaque élément de l'array un message "Position {index}: {élément}".

## Consommation d'API

### API publique

On se sert d'une API publique dont la description est ici: https://jsonplaceholder.typicode.com/guide/. 

1. Faire une requête GET sur cette URI 'https://jsonplaceholder.typicode.com/posts/1' et afficher le résultat dans le frontend
2. Requêter 'https://jsonplaceholder.typicode.com/posts/1/comments' et afficher le résultat sous la forme d'un tableau
3. Requêter 'https://jsonplaceholder.typicode.com/albums/1/photos?id=1' et afficher l'image `thumbnailUrl` de la réponse
4. Faire une requête POST sur 'https://jsonplaceholder.typicode.com/posts' avec comme paramètres de body: string `title`, string `body`, integer `userId`

### API locale

On se sert de l'API créée lors du dernier TP. Il n'y pas d'exercice en particulier, le but est de réussir à se connecter à cette API et faire des requêtes.


## Suite du TP 
## [TP2](README_TP2.md)
