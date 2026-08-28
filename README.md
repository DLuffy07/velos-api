# velos-api - projet DevOps

Ce dossier est prepare a partir des TP des Jours 1, 2 et 3 et du sujet du projet.
Il fournit le socle technique, mais les preuves personnelles (historique Git, PR, conflit, mesures, captures, identifiants Jenkins et secrets) doivent etre realisees sur ta machine.

## 1\. Avant de commencer

1. Remplace `TON\_PSEUDO` dans `k8s/api.yaml` et `Jenkinsfile` par ton identifiant Docker Hub/registre.
2. Copie `.env.example` vers `.env` et mets un vrai mot de passe local. `.env` est ignore par Git.
3. Configure ton identite Git avant les commits.

## 2\. Docker Compose

```bash
cp .env.example .env
# editer .env
docker compose up -d --build
curl http://localhost:8001/sante
curl http://localhost:8001/stations
curl http://localhost:8001/alertes
```

La base n'a volontairement aucun `ports:`. Les donnees PostgreSQL persistent dans le volume `donnees-pg`.

## 3\. Tests et image

```bash
docker build --target test -t velos-api:test .
docker build -t velos-api:1.0 .
docker run --rm velos-api:1.0 whoami
```

## 4\. Kubernetes sur le port impose 8081

```bash
kind create cluster --name devops --config k8s/kind-cluster.yaml
kubectl create secret generic velos-secret \\
  --from-literal=postgres\_password='TON\_MOT\_DE\_PASSE' \\
  --from-literal=database\_url='postgresql://postgres:TON\_MOT\_DE\_PASSE@velos-db:5432/velos'
kubectl create configmap velos-init --from-file=init.sql=db/init.sql
kubectl apply -f k8s/base.yaml
kubectl apply -f k8s/api.yaml
kubectl rollout status deployment/velos-api
curl http://localhost:8081/stations
```

Le secret est cree en ligne de commande pour ne jamais etre commite. Kubernetes l'encode en base64 : ce n'est pas un chiffrement.

## 5\. Version 2, mise a jour et retour arriere

La route `/alertes` est deja implementee dans ce socle. Pour ton historique note, organise tes commits/branches de facon a ce que cette evolution apparaisse au jalon 3, puis publie une image `2.0`.

```bash
kubectl set image deployment/velos-api api=TON\_PSEUDO/velos-api:2.0
kubectl rollout status deployment/velos-api
kubectl rollout history deployment/velos-api
kubectl rollout undo deployment/velos-api
kubectl rollout status deployment/velos-api
```

Pour prouver l'absence de coupure, garde une boucle `curl` active dans un autre terminal pendant le rollout.

## 6\. Jenkins

Le `Jenkinsfile` contient les quatre etapes imposees : Tester, Construire, Publier, Deployer. Il attend la fin reelle avec `kubectl rollout status`.

Dans Jenkins, cree les identifiants `docker-hub` et `kubeconfig-kind`. Le kubeconfig doit etre la version interne :

```bash
kind get kubeconfig --name devops --internal > /tmp/kubeconfig-interne
docker network connect kind jenkins
```

Ne committe jamais le kubeconfig ni les identifiants.

## 7\. Ce qui reste obligatoirement a faire toi-meme

Les 24 captures C01 a C24, les six commits minimum, le conflit reel, la pull request avec commentaire, le tag `v1.0.0`, la protection de `main`, les mesures de cache/taille, la publication sur ton registre, le rouge utile Jenkins et le remplissage honnete de `RAPPORT.md` ne peuvent pas etre fabriques a l'avance. Le detail exact est dans `docs/2-cahier-des-charges.md` et `docs/4-captures-attendues.md`.



\## Intégration continue



Le projet utilise Jenkins pour tester, construire, publier et déployer automatiquement l'API.

