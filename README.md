# velos-api - Projet DevOps

`velos-api` est un projet DevOps construit autour d'une API Flask de stations de vélos.

L'objectif est de mettre en place une chaîne CI/CD complète :

```text
GitHub -> Jenkins -> Docker Hub -> Kubernetes
```

L'application utilise PostgreSQL pour la persistance des données et est déployée dans un cluster Kubernetes Kind multi-nœuds.

---

## Technologies utilisées

- Python / Flask
- PostgreSQL
- Pytest
- Docker
- Docker Compose
- Kubernetes
- Kind
- Jenkins
- Docker Hub
- Git / GitHub

---

## Organisation du dépôt

```text
velos-api/
|
|-- app.py
|   API Flask
|
|-- tests/
|   Tests automatisés Pytest
|
|-- db/
|   Initialisation de PostgreSQL
|
|-- k8s/
|   Manifests Kubernetes et configuration Kind
|
|-- ci/
|   Éléments liés à l'intégration continue
|
|-- captures/
|   Captures C01 à C24 utilisées dans le rapport
|
|-- docs/
|   Documentation, énoncé et QCM
|
|-- Dockerfile
|   Construction et tests de l'image Docker
|
|-- compose.yaml
|   Environnement local API + PostgreSQL
|
|-- Jenkinsfile
|   Pipeline CI/CD
|
|-- requirements.txt
|   Dépendances Python
|
|-- requirements-dev.txt
|   Dépendances de développement et de test
|
`-- RAPPORT.md
    Rapport final du projet
```

---

## Architecture

### En local avec Docker Compose

```text
Utilisateur
    |
    | localhost:8001
    v
API Flask
    |
    | service "db"
    v
PostgreSQL
```

PostgreSQL n'est pas directement exposé sur la machine hôte.

Un volume Docker permet de conserver les données après la recréation des conteneurs.

### Dans Kubernetes

Le cluster Kind `velos` contient :

```text
1 control-plane
2 workers
```

Le trajet d'une requête est :

```text
localhost:8081
      |
      v
Kind : 30081
      |
      v
Service velos-api
      |
      v
Pods Flask
      |
      v
Service velos-db
      |
      v
PostgreSQL
```

L'API peut fonctionner avec plusieurs réplicas. Le projet démontre notamment le scaling à 4 réplicas, l'auto-réparation, le rolling update et le rollback.

---

## API

L'application écoute sur le port `8000` dans son conteneur.

Routes principales :

```text
/sante
/stations
/alertes
```

Avec Docker Compose :

```text
http://localhost:8001
```

Avec Kubernetes :

```text
http://localhost:8081
```

---

## Pipeline CI/CD

Le pipeline est défini dans `Jenkinsfile`.

Il contient quatre étapes :

```text
Tester -> Construire -> Publier -> Deployer
```

### 1. Tester

Les tests Pytest sont exécutés dans une étape dédiée du Dockerfile.

### 2. Construire

Jenkins construit l'image Docker finale.

### 3. Publier

L'image est publiée sur Docker Hub :

```text
charlic109/velos-api
```

Chaque build Jenkins utilise un tag unique basé sur son numéro.

Exemple :

```text
charlic109/velos-api:7
```

### 4. Deployer

Jenkins met à jour le Deployment Kubernetes puis attend la réussite du rollout.

La version finale validée a été déployée avec :

```text
charlic109/velos-api:7
```

---

## Sécurité du pipeline

Les identifiants Docker Hub et le kubeconfig Kubernetes sont gérés avec Jenkins Credentials.

Le mot de passe PostgreSQL n'est pas stocké dans les fichiers versionnés du dépôt.

La branche `main` est également protégée et les modifications passent par des Pull Requests.

---

## Démonstration d'un pipeline en échec

Une régression volontaire a été introduite sur `/sante` afin de vérifier le comportement de la CI.

Le build Jenkins `#6` a échoué pendant :

```text
Tester
```

Les étapes suivantes ont alors été bloquées :

```text
Construire
Publier
Deployer
```

L'ancienne image fonctionnelle est donc restée déployée dans Kubernetes.

Après correction, le build `#7` est passé au vert et a déployé la nouvelle image.

---

# Branches du dépôt

Les branches ont été conservées afin de rendre visible le workflow Git utilisé pendant le projet.

## `main`

Branche principale.

Elle contient la version finale et stable du projet.

Elle est protégée : les modifications sont intégrées par Pull Request.

---

## `docs/rendu-final`

Branche utilisée pour finaliser :

- le rapport ;
- les captures C01 à C24 ;
- le README ;
- l'organisation finale du rendu.

Son contenu final est destiné à être fusionné dans `main`.

---

## `docs/qcm`

Branche utilisée pour compléter les réponses au QCM.

---

## `ci/kubeconfig-velos`

Branche utilisée pour modifier Jenkins afin qu'il déploie sur le cluster Kind final :

```text
velos
```

Elle remplace l'utilisation de l'ancien kubeconfig par `kubeconfig-velos`.

---

## `ci/demo-test-rouge`

Branche de démonstration.

Une régression volontaire a été introduite dans `/sante` afin de provoquer l'échec des tests Jenkins.

Elle permet de montrer qu'une version défectueuse n'est ni publiée ni déployée.

---

## `ci/corrige-sante`

Branche créée après le test rouge.

Elle corrige la régression de `/sante` et permet au pipeline Jenkins de redevenir vert.

---

## Autres branches

D'autres branches de travail ont été utilisées pendant les jalons Git, Docker et Kubernetes.

Elles sont conservées pour montrer l'historique de réalisation du projet, les merges et les expérimentations effectuées.

---

# Workflow Git

Le développement suit le principe :

```text
Création d'une branche
        |
        v
     Commits
        |
        v
       Push
        |
        v
  Pull Request
        |
        v
      Review
        |
        v
   Merge dans main
```

Un véritable conflit Git a également été créé puis résolu pendant le projet.

La protection de `main` a été vérifiée en tentant volontairement un push direct, refusé par GitHub.

---

## Version

Le tag :

```text
v1.0.0
```

correspond à la première version stable créée pendant le projet.

---

# Rapport et preuves

Le rapport complet est disponible ici :

```text
RAPPORT.md
```

Les captures servant de preuves sont dans :

```text
captures/
```

Elles sont organisées par jalon :

| Captures | Jalon |
|---|---|
| C01 à C05 | Git |
| C06 à C11 | Docker / Docker Compose |
| C12 à C18 | Kubernetes |
| C19 à C24 | Jenkins / CI-CD |

Le dossier `docs/` contient également la documentation du projet et le QCM.

---

# Résultat final

Le projet permet de partir d'une modification du code et d'aller jusqu'à son déploiement automatisé :

```text
GitHub
   |
   v
Jenkins
   |
   +--> Tests
   |
   +--> Docker Build
   |
   +--> Docker Hub
   |
   `--> Kubernetes
```

Si les tests échouent, la chaîne s'arrête avant la publication et le déploiement.