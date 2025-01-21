# Concernant les exercices formatifs

Les exercices formatifs seront pour la plupart des exercices de programmation en
Python. Ces exercices contiendront des tests unitaires qui permettront de
vérifier si votre code fonctionne correctement. Voici quelques conseils pour
bien travailler sur ces exercices.

## Utiliser un environnement virtuel

### Qu'est-ce qu'un environnement virtuel?
Python est un langage qui est souvent utilisé et vous aurez donc à installer
plusieurs librairies pour travailler sur vos divers projets. Il fort probable
que ceux-ci utilisent des versions différentes de ces librairies voir même des
versions différentes de Python (ex: 3.10, 3.11, etc.). Pour éviter les conflits
entre ces différentes versions, il est possible de créer un environnement
virtuel. Un environnement virtuel est simplement un dossier qui contient une
version de Python et des librairies spécifiques à votre projet. Une fois
l'environnement virtuel activé, Python et votre environnement de développement
(VSCode ou PyCharm) utilisera les librairies et la version de Python contenues
dans cet environnement.

Ainsi, si chaque projet a son propre environnement virtuel, il n'y aura pas de
conflits entre les différentes versions de Python et les librairies.


### Comment créer un environnement virtuel?

Créer un dossier sur votre machine dans lequel vous mettrez tous vos fichiers
d'exercices pour ce cours. PyCharm ou VSCode propose parfois de créer un
environnement virtuel pour vous. Il suffit alors simplement de vous laisser
guider par ces outils.

Si ce n'est pas le cas, vous pouvez créer un




```bash
python3 -m venv .venv
```

Activez ensuite votre environnement virtuel avec la commande suivante:
```bash
.venv/bin/activate
```