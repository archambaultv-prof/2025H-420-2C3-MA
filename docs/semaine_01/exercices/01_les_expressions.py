# ##############################################################################
# Consigne : Vous devez remplacer None par la valeur attendue
# ##############################################################################

# Les commentaires 'noqa: E711' sont pour ignorer l'erreur "comparison to None
# should be 'if cond is None:'" de flake8)

def test_expressions_simples():
    assert (3 + 4 * 2) == None  # noqa: E711
    assert (not ((5 > 3) and (2 < 1))) == None  # noqa: E711
    assert ("Hello" + " " + "World") == None  # noqa: E711
    assert (10 % 3 == 1) == None  # noqa: E711


def test_identifier_les_types():
    x = 42
    y = 3.14
    z = "Bonjour"
    a = [1, 2, 3]
    b = {"clé": "valeur"}
    c = False

    assert isinstance(x, None)
    assert isinstance(y, None)
    assert isinstance(z, None)
    assert isinstance(a, None)
    assert isinstance(b, None)
    assert isinstance(c, None)
