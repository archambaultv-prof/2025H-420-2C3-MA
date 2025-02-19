# Travail pratique 1 : Module de gestion des finances personnelles

## Objectif

L’objectif de ce TP est de vous familiariser avec la programmation objet,
l’écriture de tests unitaires et la rédaction d’une documentation. Vous allez
développer un module destiné à gérer des finances personnelles. Ce projet vous
permettra de consolider vos connaissances en Python et de développer votre
autonomie.

## Informations générales

- Ce travail pratique est à réaliser individuellement.
- Ce travail vaut 15% de la note finale.
- La date de remise est le mercredi 5 mars 2025 à 23h59.
- L'utilisation de l'IA est permise selon les règles de la PDÉA.

## Contexte

Vous devez créer un module en Python pour gérer des finances personnelles. En
plus du module lui-même, l'écriture des tests unitaires à la rédaction de la
documentation sont des éléments importants de ce travail pratique.

Les consignes sont volontairement ouvertes pour vous laisser une certaine
liberté, comme ce serait le cas dans un contexte professionnel. Vous devez donc
faire preuve de débrouillardise et d'autonomie pour mener à bien ce projet.

## Consignes

### 1. Créer un module Python

Pour simplifier le travail pratique, vous n'avez pas besoin de créer un module
complet qui pourrait être publié sur [PyPI](https://pypi.org/). Vous devez
toutefois avoir tout votre code et vos tests sous un même répertoire.

Votre répertoire devrait pouvoir être utilisé localement comme un package
Python.

### 2. Conception du module

Votre module doit permettre de gérer des finances personnelles. Il devra
inclure, au minimum, les classes et fonctionalités suivantes :

#### a. Comptes (`Compte`)

Les classes `Compte` et ses dérivées représentent des comptes bancaires ou de
l'argent comptant. La classe mère possède l'attribut suivant :

- `nom`  : le nom du compte.

Vous devez aussi créer des classes dérivées pour deux types de comptes :

- **Compte bancaire** : un compte bancaire classique. Il possède un attribut
  `banque` qui représente la banque associée et un attribut `numero` qui
  représente le numéro de compte.
- **Argent comptant** : un compte qui représente de l'argent liquide. Il n'a
  pas de banque associée et ne possède pas de numéro de compte. Toutefois, il
    possède un attribut `maximum` qui représente le montant maximum d'argent
    liquide que l'on devrait y conserver.

#### b. Catégories (`Categorie`)

- **Description** : Permet de catégoriser les transactions (ex. : alimentation, transport, loisirs).
- **Propriétés suggérées** :
  - `nom`  : le nom de la catégorie.
  - `description`  : une description de la catégorie.
  
#### c. Transactions (`Transaction`)

Une transaction représente une opération financière. L'idée est que les
catégories permettent de classer les transactions qui représentent des dépenses
ou des revenus. Une dépense est une transaction qui diminue le solde d'un
compte, comme le paiement d'une facture ou un achat en ligne. Un revenu est une
transaction qui augmente le solde d'un compte, comme un salaire. Les transferts
ne sont pas catégorisables et représentent un mouvement d'argent d'un compte à un
autre, comme le paiement d'une carte de crédit ou un virement entre deux
comptes. Ainsi, il existe trois types de transactions : transfert, dépenses et
revenus. Il faut définir une classe de base `Transaction` et des classes
dérivées pour les différents types de transactions.

Les propriétés communes à toutes les transactions seront définies dans la
classe de base `Transaction`. Par exemple, la date de la transaction et le
montant. Les propriétés spécifiques à chaque type de transaction seront
définies dans les classes dérivées. Par exemple un transfert possède un compte
source et un compte destination. Une dépense possède un compte source et une
catégorie. Un revenu possède aussi un compte source et une catégorie, mais par
exemple son constructeur doit vérifier que le montant est positif. Vous pouvez même
ajouter une classe intermédiaire pour mettre en commun des propriétés communes
aux dépenses et aux revenus.

#### d. Création de comptes

Une fonction qui peut lire un fichier CSV contenant des informations sur les
comptes et les créer. Une ligne du fichier permet de créer un compte. Utilisez
le module `csv` de Python pour lire le fichier. Par exemple, le fichier CSV
pourrait contenir les colonnes suivantes :

- `nom`, `type`, `banque`, `numero`, `maximum`.

Le type permet de déterminer si le compte est un compte bancaire ou de l'argent
comptant. Le traitement des autres colonnes dépend du type de compte.

#### e. Création de transactions

Une fonction qui peut lire un fichier CSV contenant des informations sur les
transactions et les créer. Par exemple, le fichier CSV pourrait contenir les
colonnes suivantes :

- `date`, `montant`, `type`, `compte_source`, `compte_destination`, `categorie`.

#### f. Création de catégories

Une fonction qui peut lire un fichier CSV contenant des informations sur les
catégories et les créer. Une ligne du fichier permet de créer une catégorie.

#### g. Solde d'un compte

Une fonction qui permet de calculer le solde d'un compte à une date donnée.
Cette fonction accepte une liste de transactions, le nom du compte et une date.
Elle doit retourner le solde du compte à la date donnée.

#### h. Flux monétaire d'une catégorie

Une fonction qui permet de calculer le flux monétaire d'une catégorie entre deux
dates (inclusivement). Elle permet de répondre à la question : combien d'argent
ai-je dépensé en nourriture entre le 1er janvier et le 31 décembre 2024 ?

Cette fonction accepte une liste de transactions, le nom de la catégorie, une
date de début et une date de fin. Elle doit retourner le montant total dépensé
dans la catégorie entre les deux dates (incluses).

#### i. Points bonus (3 points sur 15)

Créez une classe `Solde` qui permet de spécifier un solde pour un compte à une
date donnée. Comme pour les classes précédentes, vous devez écrire un fonction pour lire
un fichier CSV contenant des informations sur les soldes et les créer. Ce fichier
pourrait contenir les colonnes suivantes :

- `date`, `nom`, `solde`.

Vous devez aussi écrire une fonction qui permet de vérifier le solde d'un compte.
Cette fonction accepte une liste de soldes et une liste de transactions. Elle doit
retourner les soldes qui ne correspondent pas aux transactions.

### 5. Tests unitaires

- **Objectif** : Vérifier que vos classes et méthodes fonctionnent comme attendu.
- Utilisez le framework `pytest`.
- Veillez à tester à la fois les cas normaux et les cas limites (ex. : fichier
  vide, liste vide, valeur manquante, listes de transactions non triées par date, etc.).

### 6. Documentation

- Utilisez des docstrings pour documenter votre code.
- Créez un fichier `README.md` qui présente votre projet. **Vous pouvez
    utiliser le README.md pour attirer mon attention sur des points importants
    de votre code.**
- La documentation doit être claire et suffisante pour que quelqu’un puisse
  utiliser votre module sans regarder le code source.

### 7. Utilisation de Git

- Je vous suggère fortement d’utiliser Git pour versionner votre code. Vous ne
  serez pas évalué sur l'utilisation de Git, mais c'est une bonne pratique à
  adopter.

## Livrables

- **Code source** : L’ensemble du code de votre module, y compris les tests
  unitaires.

Vous devez remettre sur Omnivox votre dossier. L'historique de Git n'est pas
nécessaire.

## Grille d’évaluation

La grille est sur 20 points. La note finale sera ramenée sur 15 points.

| Critère | Excellent (20 à 18) | Très bien (17 à 16) | Bien (15 à 14) | Passable (13 à 12) | Insuffisant (11 et moins) |
|---------|---------------------|---------------------|----------------|--------------------|--------------------------|
Fonctionnalité (30%) | Toutes les fonctionnalités demandées sont implémentées et fonctionnent correctement. | La plupart des fonctionnalités demandées sont implémentées et fonctionnent correctement. | Certaines fonctionnalités demandées sont implémentées et fonctionnent correctement. | Certaines fonctionnalités demandées sont implémentées mais ne fonctionnent pas correctement. | Peu de fonctionnalités demandées sont implémentées et ne fonctionnent pas correctement. |
Qualité du code (25%) | Le code est bien structuré, modulaire et facile à lire. | Le code est bien structuré et modulaire. | Le code est structuré mais manque de modularité. | Le code est mal structuré et difficile à lire. | Le code est mal structuré et difficile à lire. |
Tests unitaires (20%) | Toutes les classes et méthodes sont testées et les tests passent. Les cas limites sont testés. | La plupart des classes et méthodes sont testées et les tests passent. | Certaines classes et méthodes sont testées et les tests passent. | Certaines classes et méthodes sont testées mais les tests ne passent pas. | Peu de classes et méthodes sont testées et les tests ne passent pas. |
Documentation (25%) | La documentation est complète, claire, concise et bien rédigée. | La documentation est complète et claire. Certains points pourraient être améliorés. | La documentation est complète mais manque de clarté. | La documentation est incomplète et manque de clarté. | La documentation est absente ou inexistante. |
Points bonus (20%) | Les points bonus sont implémentés et fonctionnent correctement. | Les points bonus sont implémentés mais ne fonctionnent pas correctement. | Les points bonus sont partiellement implémentés. | Les points bonus sont mal implémentés. | Les points bonus ne sont pas implémentés. |

## Conseils et recommandations

- **Planification** : Prenez quelques minutes pour planifier l’architecture de
  votre projet avant de commencer à coder.
- **Modularité** : Organisez votre code en modules pour faciliter la maintenance
  et la compréhension.
- **Tests** : N’attendez pas la fin du développement pour écrire vos tests,
  faites-le au fur et à mesure.
- **Documentation** : Investissez du temps dans la rédaction d’une bonne
  documentation, cela facilitera l’utilisation de votre module.
- **Collaboration** : Travaillez de manière autonome, mais n’hésitez pas à
  échanger avec vos camarades pour résoudre des problèmes.

## Ressources utiles

- [Documentation Python](https://docs.python.org/3/)
- [pytest](https://docs.pytest.org/en/stable/)

---

Bonne chance et bon travail !
