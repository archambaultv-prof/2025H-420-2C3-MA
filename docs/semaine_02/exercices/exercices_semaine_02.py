# Exercices de la semaine 2

# Les exercices sont accompagnés de tests unitaires pour vérifier votre
# solution. Vous pouvez exécuter les tests avec le package pytest.

import numpy as np


# a. Tableau vide []
tab1 = None


# b. Tableau de zéros [0, 0, 0, 0, 0] avec np.zeros()
tab2 = None


# c. Tableau de uns [1, 1, 1] avec np.ones()
tab3 = None


# d. Tableau de dix [10, 10, 10] avec np.ones()
tab4 = None


# e. Tableau aléatoire de 5 chiffres entre 0 et 1
#    avec np.random
tab5 = None


# f. Tableau aléatoire de 5 chiffres entre 0 et 5
#    avec np.random
tab6 = None


# g. Tableau aléatoire de 5 chiffres entre 5 et 10
#    avec np.random
tab7 = None


# h. Matrice 2x2 de zéros avec np.zeros
tab8 = None


# i. Matrice 10x5 de uns avec np.ones
tab9 = None


# k. Matrice 5x5 avec comme valeur de diagonale 10. Utiliser np.eye
tab10 = None


# l. Tableau avec éléments entiers de 20 à 80
tab11 = None


# m. Tableau avec éléments pairs de 20 à 80
tab12 = None


# n. Tableau avec 100 éléments entre 0 et 5
tab13 = None


def test_tableaux():
    assert np.array_equal(tab1, np.array([]))
    assert np.array_equal(tab2, np.array([0, 0, 0, 0, 0]))
    assert np.array_equal(tab3, np.array([1, 1, 1]))
    assert np.array_equal(tab4, np.array([10, 10, 10]))
    assert len(tab5) == 5
    assert np.all(tab5 >= 0) and np.all(tab5 <= 1)
    assert len(tab6) == 5
    assert np.all(tab6 >= 0) and np.all(tab6 <= 5)
    assert len(tab7) == 5
    assert np.all(tab7 >= 5) and np.all(tab7 <= 10)
    assert np.array_equal(tab8, np.array([[0, 0], [0, 0]]))
    assert np.array_equal(tab9, np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                                          [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                                          [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                                          [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                                          [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
    assert np.array_equal(tab10, np.array([[10, 0, 0, 0, 0], [0, 10, 0, 0, 0],
                                           [0, 0, 10, 0, 0], [0, 0, 0, 10, 0],
                                           [0, 0, 0, 0, 10]]))
    assert np.all(tab11 >= 20) and np.all(tab11 <= 80) and len(tab11) == 61
    assert (np.all(tab12 % 2 == 0) and np.all(tab12 >= 20)
            and np.all(tab12 <= 80) and len(tab12) == 31)
    assert np.all(tab13 >= 0) and np.all(tab13 <= 5) and len(tab13) == 100


# Écrire une fonction qui trouvera les indices des éléments non nuls d'un
# tableau numpy.
def valeurs_non_nuls(tableau):
    pass


def test_valeurs_non_nuls():
    assert np.array_equal(
        valeurs_non_nuls(np.array([1, 0, 2, 0, 3, 0, 4, 0])),
        np.array([0, 2, 4, 6])
    )
    assert np.array_equal(
        valeurs_non_nuls(np.array([0, 0, 0, 0])),
        np.array([])
    )
    assert np.array_equal(
        valeurs_non_nuls(np.array([1, 2, 3, 4])),
        np.array([0, 1, 2, 3])
    )
    assert np.array_equal(
        valeurs_non_nuls(np.array([])),
        np.array([])
    )


def valeurs_plus_grand_que(tableau, valeur):
    pass


def test_indices_plus_grand_que():
    assert np.array_equal(
        valeurs_plus_grand_que(np.array([1, 2, 3, 4]), 2),
        np.array([2, 3])
    )
    assert np.array_equal(
        valeurs_plus_grand_que(np.array([1, 2, 3, 4]), 4),
        np.array([])
    )
    assert np.array_equal(
        valeurs_plus_grand_que(np.array([1, 2, 3, 4]), 0),
        np.array([0, 1, 2, 3])
    )
    assert np.array_equal(
        valeurs_plus_grand_que(np.array([]), 0),
        np.array([])
    )


# Ecrivez un programme numpy pour convertir les valeurs des degrés Fahrenheit
# en degrés celcius. Les valeurs en Fahrenheit sont stockées dans un tableau
# numpy. Formule de conversion : C = (F - 32) * (5/9). Essayez de ne pas
# utiliser de boucles !
def fahrenheit_to_celsius(fahrenheit):
    pass


def test_fahrenheit_to_celsius():
    assert np.allclose(
        fahrenheit_to_celsius(np.array([0, 32, 100])),
        np.array([-17.77777778, 0., 37.77777778]),
        atol=1e-7
    )
    assert np.allclose(
        fahrenheit_to_celsius(np.array([0])),
        np.array([-17.77777778]),
        atol=1e-7
    )
    assert np.allclose(
        fahrenheit_to_celsius(np.array([])),
        np.array([]),
        atol=1e-7
    )


# Ecrivez un programme NumPy pour trouver des valeurs communes entre deux
# tableaux (pensez à utiliser la fonction intersect1d).
def valeurs_communes(tableau1, tableau2):
    pass


def test_valeurs_communes():
    assert np.array_equal(
        valeurs_communes(np.array([1, 2, 3, 4]), np.array([3, 4, 5, 6])),
        np.array([3, 4])
    )
    assert np.array_equal(
        valeurs_communes(np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8])),
        np.array([])
    )
    assert np.array_equal(
        valeurs_communes(np.array([1, 2, 3, 4]), np.array([1, 2, 3, 4])),
        np.array([1, 2, 3, 4])
    )
    assert np.array_equal(
        valeurs_communes(np.array([]), np.array([])),
        np.array([])
    )


# Écrivez une fonction pour inverser un tableau numpy 1D (le premier élément
# devient le dernier).
def inverser_tableau(tableau):
    pass


def test_inverser_tableau():
    assert np.array_equal(
        inverser_tableau(np.array([1, 2, 3])),
        np.array([3, 2, 1])
    )
    assert np.array_equal(
        inverser_tableau(np.array([1, 2, 3, 4])),
        np.array([4, 3, 2, 1])
    )
    assert np.array_equal(
        inverser_tableau(np.array([1])),
        np.array([1])
    )
    assert np.array_equal(
        inverser_tableau(np.array([])),
        np.array([])
    )


# Écrivez une fonction pour inverser un tableau numpy à plusieurs dimensions.
def inverser_tableau_multi(tableau):
    pass


def test_inverser_tableau_multi():
    assert np.array_equal(
        inverser_tableau_multi(np.array([[1, 2, 3], [4, 5, 6]])),
        np.array([[6, 5, 4], [3, 2, 1]])
    )
    assert np.array_equal(
        inverser_tableau_multi(np.array([[9, 8], [7, 6], [5, 4], [3, 2]])),
        np.array([[2, 3], [4, 5], [6, 7], [8, 9]])
    )
    assert np.array_equal(
        inverser_tableau_multi(np.array([[1]])),
        np.array([[1]])
    )
    assert np.array_equal(
        inverser_tableau_multi(np.array([])),
        np.array([])
    )


# Vous avez un tableau de notes d'étudiants et vous devez calculer les
# statistiques suivantes :
# Moyenne : La moyenne des notes.
# Médiane : La valeur médiane des notes.
# Écart-type : Une mesure de la dispersion des notes par rapport à la moyenne.
# Votre fonction doit retourner un dictionnaire avec ces statistiques.
# Les clés du dictionnaire sont 'moyenne', 'mediane' et 'ecart_type'.
def statistiques_notes(notes):
    pass


def test_statistiques_notes():
    notes = np.array([1, 2, 3, 3, 4, 5, 6])
    stats = statistiques_notes(notes)
    assert np.isclose(stats['moyenne'], 3.42857143, atol=1e-6)
    assert np.isclose(stats['mediane'], 3)
    assert np.isclose(stats['ecart_type'], 1.590789, atol=1e-6)
