# Python Programming for the Humanities

Le langage de programmation [Python](https://www.python.org) est beaucoup utilisé dans de nombreux domaines scientifiques aujourd'hui et le langage est assez accessible pour les universitaires des humanités. Python est un excellent choix quand il s'agit de gérer des données textuelles, ce qui est typique des humanités, mais aussi quand il faut écrire un site web, gérer des données numériques, écrire un script pour faire des transformations, etc. Dans ce cahier virtuel d'exercices, nous vous présenterons le langage et apprendrons les basiques liées à l'algorithmique. Ce livre n'attend de vous aucun prérequis de programmation, même si nous espérons qu'il soit intéressant pour des personnes plus avancées. Ce livre est une tradiction et adaptation de 4 chapitres de Matt Munson issus de 10 chapitres écrits par Folgert Karsdorp du KNAW.

Ce document décrit une procédure d'installation pour l'ensemble des logiciels nécessaires pour le cours de python. Si vous êtes bloqués, contactez votre professeur.

## Sublime text ou PyCharm

Nous vous recommandons d'installer un bon éditeur de texte voire un bon IDE pour ce cours. Nous vous conseillons [Sublime Text](https://www.sublimetext.com) ou [PyCharm](https://www.jetbrains.com/pycharm)

Dans ce cours, nous utiliserons un logiciel qui fonctionne très bien avec Firefox et Chrome. Safari fonctionnera aussi, Internet Explorer peut poser des problèmes 

## Python X ?

Nous utiserons Python 3 dans notre cours. Des versions précédentes peuvent poser des problèmes.


## Installation

### OS X

**Nous vous conseillons d'installar la distribution Anaconda**. Elle per contient tous les modules et packages nécessaires pour ce cours. Elle est disponible pour toutes les plateformes et possède une procédure d'installation assez simple. Vous pouvez la télécharger de http://continuum.io/downloads.  Des détails pour l'installation peuvent être trouvés ici : http://docs.continuum.io/anaconda/install.html 

Utilisez bien la version 3.6 proposée. Une fois installée, tapez ensuite

```shell
conda create -n cours-python
```

suivi de

```shell
source activate cours-python
```

Cette dernière active un environnement de python qui nous permet de ne pas modifier l'environnement général de votre ordinateur. 

Allez dans le repository git puis tapez dans terminal dans ce dossier

```shell
pip install -r requirements.txt
```

Tapez désormais

```shell
ipython notebook --matplotlib=inline
```

Si tout va bien, cela devrait ouvrir votre navigateur sur la page http://127.0.0.1:8888/ qui s'appelle IP[y]: Notebook.

### Linux (Ubuntu/Debian)

Vous aurez besoin des droits d'administrateurs pour faire ce qui suit.

Ouvrez un terminal et tapez :

```shell
sudo apt-get install python3 libfreetype6-dev
```

Puis, une fois cela installé, faites :

```shell
virtualenv ~/.cours-python -p python3
```
Cela créera un environnement virtuel dans lequel nous pourrons installer l'ensemble des informations nécessaires. Allez, dans le terminal, dans le dossier git du cours que vous avez cloné localement et tapez :

```shell
source ~/.cours-python/bin/activate
```

Cette commande sera obligatoire à chaque fois que vous voudrez travailler avec le cours. Dans le même terminal, tapez maintenant

```shell
pip install -r requirements.txt
```

Cela installera les packages nécessaires pour le cours. Une fois ces packages installés, il suffira de taper 

```shell
ipython3 notebook
```

Si tout va bien, cela devrait ouvrir votre navigateur sur la page http://127.0.0.1:8888/ qui s'appelle IP[y]: Notebook.

## Contributors
- Folgert Karsdorp
- Maarten van Gompel
- Matt Munson
- Thibault Clérice
