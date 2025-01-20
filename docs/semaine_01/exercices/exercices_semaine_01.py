# Exercices de la semaine 1

# Les exercices sont accompagnés de tests unitaires pour vérifier votre
# solution. Vous pouvez exécuter les tests avec le package pytest.


# Vous devez remplacer None par la valeur attendue
def test_expressions_simples():
    assert (3 + 4 * 2) == None  # noqa: E711
    assert (not ((5 > 3) and (2 < 1))) == None  # noqa: E711
    assert ("Hello" + " " + "World") == None  # noqa: E711
    assert (10 % 3 == 1) == None  # noqa: E711


# Vous devez remplacer None par la valeur attendue
def test_identifier_les_types():
    x = 42
    y = 3.14
    z = "Bonjour"
    a = [1, 2, 3]
    b = {"clé": "valeur"}
    c = False

    # ex: int, float, str, list, dict, bool
    assert isinstance(x, None)
    assert isinstance(y, None)
    assert isinstance(z, None)
    assert isinstance(a, None)
    assert isinstance(b, None)
    assert isinstance(c, None)


def test_conditions_complexes():
    x = 10
    y = 5
    z = 15
    assert ((x > y) and (z > x)) == None  # noqa: E711
    assert ((x < y) or (z > x)) == None  # noqa: E711
    assert (not (x < y)) == None  # noqa: E711
    assert ((x == 10) and (y == 5) and (z == 15)) == None  # noqa: E711


def test_conditions_ternaires():
    x = 10
    y = 5
    message = "x est supérieur à y" if x > y else "x est inférieur ou égal à y"
    assert message == None  # noqa: E711


def test_chaines_caracteres():
    assert "Bonjour".upper() == None  # noqa: E711
    assert "BONJOUR".lower() == None  # noqa: E711
    assert "  bonjour  ".strip() == None  # noqa: E711
    assert "bonjour tout le monde".find("tout") == None  # noqa: E711
    assert "bonjour tout le monde".replace("bonjour", "salut") \
        == None  # noqa: E711
    assert "bonjour tout le monde".split(" ") == None  # noqa: E711
    assert " ".join(["bonjour", "tout", "le", "monde"]) == None  # noqa: E711
    assert "bonjour tout le monde".count("o") == None  # noqa: E711


# Écrire une fonction qui accepte un nombre entier et retourne True si le
# nombre est un multiple de 2 ou 5, sinon False.
def multiple_deux_ou_cinq(n: int) -> bool:
    pass


def test_multiple_deux_ou_cinq():
    assert multiple_deux_ou_cinq(2) is True
    assert multiple_deux_ou_cinq(5) is True
    assert multiple_deux_ou_cinq(10) is True
    assert multiple_deux_ou_cinq(3) is False
    assert multiple_deux_ou_cinq(7) is False
    assert multiple_deux_ou_cinq(11) is False


# Écrire une fonction qui accepte un nombre entier n et retourne une liste de
# listes représentant une table de multiplication de n x n. Par exemple, si n
# est 3, la fonction doit retourner:
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]] qui représente la table de multiplication
# [[1 * 1, 1 * 2, 1 * 3],
#  [2 * 1, 2 * 2, 2 * 3],
#  [3 * 1, 3 * 2, 3 * 3]]
def table_multiplication(n: int) -> list:
    pass


def test_table_multiplication():
    assert table_multiplication(2) == [[1, 2], [2, 4]]
    assert table_multiplication(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert table_multiplication(1) == [[1]]
    assert table_multiplication(4) == [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 6, 9, 12],
        [4, 8, 12, 16],
    ]


# Écrire une fonction qui accepte une chaîne de caractères et qui retourne une
# adresse courriel. Les informations prénom, nom et domaine sont séparées par
# des virgules. Par exemple, si la chaîne est "Alice,Bouchard,example.com", la
# fonction doit retourner "alice.bouchard@example.com". L'adresse courriel doit
# être en minuscules.
def adresse_courriel(s: str) -> str:
    pass


def test_adresse_courriel():
    assert adresse_courriel("Alice,Bouchard,example.com") == \
        "alice.bouchard@example.com"
    assert adresse_courriel("Bob,Marley,example.com") == \
        "bob.marley@example.com"
    assert adresse_courriel("Charlie,Brown,example.com") == \
        "charlie.brown@example.com"


# Écrire une fonction qui calcule la liste des nombres pairs entre 0 et n
# inclusivement. Par exemple, si n est 10, la fonction doit retourner
# [0, 2, 4, 6, 8, 10].

# Utiliser une boucle while
def nombres_pairs_while(n: int) -> list:
    pass


# Utiliser une boucle for
def nombres_pairs_for(n: int) -> list:
    pass


def test_nombres_pairs():
    def helper(foo):
        assert foo(10) == [0, 2, 4, 6, 8, 10]
        assert foo(5) == [0, 2, 4]
        assert foo(0) == [0]

    helper(nombres_pairs_while)
    helper(nombres_pairs_for)


# Écrire une fonction qui accepte deux listes et retourne une liste contenant
# des tuples avec les éléments correspondants des deux listes. Par exemple, si
# les deux listes sont [1, 2, 3] et ['a', 'b', 'c'], la fonction doit
# retourner [(1, 'a'), (2, 'b'), (3, 'c')]. Si les listes n'ont pas la même
# longueur, la fonction doit retourner autant de tuples que possible.
def zip_listes(liste1: list, liste2: list) -> list:
    pass


def test_zip_listes():
    assert zip_listes([1, 2, 3], ['a', 'b', 'c']) == \
        [(1, 'a'), (2, 'b'), (3, 'c')]
    assert zip_listes([1, 2], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b')]
    assert zip_listes([1, 2, 3], ['a', 'b']) == [(1, 'a'), (2, 'b')]
    assert zip_listes([], []) == []
    assert zip_listes([1], ['a']) == [(1, 'a')]
    assert zip_listes([], [1, 2]) == []
    assert zip_listes([1, 2], []) == []


# Écrire une fonction qui, à partir de deux listes de nombres, retourne une 3e
# liste comprenant uniquement les nombres qui se retrouvent dans les deux
# premières listes.
def intersection_listes(liste1: list, liste2: list) -> list:
    pass


def test_intersection_listes():
    assert intersection_listes([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersection_listes([1, 2, 3], [4, 5, 6]) == []
    assert intersection_listes([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert intersection_listes([], []) == []
    assert intersection_listes([1, 2, 3], []) == []
    assert intersection_listes([], [1, 2, 3]) == []


# Écrire une fonction qui accepte deux listes et retourne la liste des éléments
# en commun entre les deux listes, mais sans doublons. Par exemple, si les deux
# listes sont [1, 2, 2, 3] et [2, 3, 4], la fonction doit retourner [2, 3].
def intersection_listes_sans_doublons(liste1: list, liste2: list) -> list:
    pass


def test_intersection_listes_sans_doublons():
    assert intersection_listes_sans_doublons([1, 2, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersection_listes_sans_doublons([1, 2, 3], [4, 5, 6]) == []
    assert intersection_listes_sans_doublons([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert intersection_listes_sans_doublons([], []) == []
    assert intersection_listes_sans_doublons([1, 2, 3], []) == []
    assert intersection_listes_sans_doublons([3], [1, 2, 3]) == [3]
