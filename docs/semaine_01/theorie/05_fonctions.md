# Les fonctions

## Utilité des fonctions
Les fonctions sont des blocs de code réutilisables qui permettent de structurer et d'organiser le code de manière logique. Elles facilitent la maintenance, la lisibilité et la réutilisation du code. En encapsulant des tâches spécifiques dans des fonctions, on peut éviter la duplication de code et rendre le programme plus modulaire.

## Retourner plusieurs valeurs
En Python, une fonction peut retourner plus d'une valeur en utilisant des tuples. Cela permet de renvoyer plusieurs résultats à partir d'une seule fonction.

```python
def calculer(a, b):
    somme = a + b
    produit = a * b
    return somme, produit

s, p = calculer(3, 4)
print(f"Somme: {s}, Produit: {p}")  # Affiche "Somme: 7, Produit: 12"
```

## Appeler une fonction depuis une autre fonction
Une fonction peut appeler une autre fonction. Cela permet de décomposer des tâches complexes en sous-tâches plus simples et de réutiliser des fonctions existantes.

=== "Python"
    ```python
    def chauffer_eau(temperature):
        print(f"Chauffage de l'eau à {temperature} degrés.")
        return f"eau à {temperature} degrés"

    def moudre_grains():
        print("Mouture des grains de café.")
        return "café moulu"

    def preparer_cafe():
        eau = chauffer_eau(90)
        cafe = moudre_grains()
        print(f"Préparation du café avec {eau} et {cafe}.")
        return "café prêt"

    cafe = preparer_cafe()
    print(cafe)
    ```
=== "Résultat"
    ```
    Chauffage de l'eau à 90 degrés.
    Mouture des grains de café.
    Préparation du café avec eau à 90 degrés et café moulu.
    café prêt
    ```

## Paramètres d'une fonction

### 0 ou plusieurs paramètres
Une fonction peut être définie sans paramètres ou avec plusieurs paramètres. 

```python
def saluer():
    print("Bonjour!")

def additionner(a, b):
    return a + b

saluer()  # Affiche "Bonjour!"
print(additionner(3, 4))  # Affiche 7
```

### Valeur par défaut
Les paramètres peuvent avoir des valeurs par défaut, ce qui permet de les omettre lors de l'appel de la fonction.

```python
def saluer(nom="tout le monde"):
    print(f"Bonjour, {nom}!")

saluer()  # Affiche "Bonjour, tout le monde!"
saluer("Alice")  # Affiche "Bonjour, Alice!"
```

!!! warning "Attention"
    Les objets mutables (comme les listes ou les dictionnaires) utilisés comme valeurs par défaut peuvent poser des problèmes. Ils sont partagés entre les appels de la fonction, ce qui peut entraîner des effets de bord inattendus.
    Mieux vaut utiliser `None` comme valeur par défaut et initialiser l'objet à l'intérieur de la fonction.

```python linenums="1"
def ajouter_element(element, liste=[]):
    liste.append(element)
    return liste

print(ajouter_element(1))  # Affiche [1]
print(ajouter_element(2))  # Affiche [1, 2]

def ajouter_element2(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

print(ajouter_element2(1))  # Affiche [1]
print(ajouter_element2(2))  # Affiche [2]
```

### Paramètres variables avec `*args`
Une fonction peut accepter un nombre variable de paramètres en utilisant `*args`.

```python
def additionner_tout(*args):
    return sum(args)

print(additionner_tout(1, 2, 3))  # Affiche 6
print(additionner_tout(5, 10, 15, 20))  # Affiche 50
```

### Appel avec mot clé
Les paramètres peuvent être passés par mot clé, ce qui permet de les spécifier dans n'importe quel ordre.

```python
def decrire_personne(nom, age, ville):
    print(f"{nom} a {age} ans et habite à {ville}.")

decrire_personne(age=30, ville="Paris", nom="Alice")
# Affiche "Alice a 30 ans et habite à Paris."
```

## Portée locale et globale
La portée d'une variable détermine où elle peut être utilisée dans le code. En
Python, les variables peuvent avoir une portée locale ou globale.

### Variables locales
Les variables définies à l'intérieur d'une fonction sont locales à cette
fonction et ne peuvent pas être utilisées en dehors de celle-ci.

```python
def ma_fonction():
    x = 10  # Variable locale
    print(x)

ma_fonction()  # Affiche 10
print(x)  # Erreur : x n'est pas défini en dehors de la fonction
```

### Variables globales
Les variables définies en dehors de toutes les fonctions sont globales et
peuvent être utilisées dans n'importe quelle fonction. Pour modifier une
variable globale à l'intérieur d'une fonction, on doit utiliser le mot-clé
`global`.

```python
x = 10  # Variable globale

def ma_fonction():
    global x
    x = 20  # Modification de la variable globale
    print(x)

ma_fonction()  # Affiche 20
print(x)  # Affiche 20
```

!!! warning "Attention"
    L'utilisation excessive de variables globales peut rendre le code difficile à comprendre et à maintenir. Il est recommandé de limiter l'utilisation des variables globales et de préférer les variables locales autant que possible.

### Variables locales et globales avec le même nom
Si une variable locale et une variable globale ont le même nom, la variable
locale masque la variable globale à l'intérieur de la fonction.

```python
x = 10  # Variable globale

def ma_fonction():
    x = 20  # Variable locale
    print(x)  # Affiche 20

ma_fonction()
print(x)  # Affiche 10
```
