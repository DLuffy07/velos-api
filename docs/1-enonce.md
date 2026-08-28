# 1. Énoncé · `velos-api`, de la première ligne d'historique au déploiement automatique

> 🎯 **En une phrase** : reprendre, seul, sur une application que tu n'as jamais vue, la chaîne complète des trois jours. Je versionne, je conteneurise, je déploie, j'automatise, je prouve.

---

## 1. Le contexte

Une communauté de communes met en service un système de vélos en libre-service. Une petite équipe a écrit une application qui expose l'état des stations : combien de vélos sont disponibles, dans quel quartier, et quelles stations sont presque vides.

Cette application fonctionne. Sur le portable d'un développeur.

Il n'y a **aucun dépôt Git**, **aucune image**, **aucun déploiement**, **aucune automatisation**. La collectivité te recrute comme ingénieur DevOps junior et te confie une seule mission :

> **Rendre cette application livrable, reproductible et déployable par une machine, et le prouver.**

Le code de l'application t'est **fourni** dans [`ressources/`](./ressources/). Tu n'as pas à le réécrire : ce n'est pas ce qui est évalué. Une seule évolution fonctionnelle te sera demandée en cours de route, et elle tient en quelques lignes.

---

## 2. L'application qu'on te confie

`velos-api` est une petite API HTTP en Python (Flask), volontairement minuscule.

| Route | Ce qu'elle renvoie |
| --- | --- |
| `/sante` | Un état de santé, destiné aux **machines** et pas aux humains |
| `/stations` | La liste des stations, avec leur quartier et leurs vélos disponibles |
| `/disponibilite` | Le taux d'occupation moyen du parc |
| `/alertes` | **Cette route n'existe pas encore. C'est toi qui l'ajouteras** (jalon 3) |

Deux comportements à comprendre avant de commencer, parce qu'ils commandent tout le reste :

1. L'application lit sa configuration dans des **variables d'environnement**. Si une base de données est configurée, elle l'utilise. Sinon, elle se rabat sur un jeu de données en mémoire et l'annonce dans sa réponse. La même image tournera donc en local, dans une pile de conteneurs, dans le cluster et dans le pipeline, **sans jamais être reconstruite**. Seule la configuration change.
2. Elle écoute sur toutes les interfaces, et pas seulement sur la boucle locale. Tu sais depuis le Jour 2 pourquoi cela compte dès qu'un conteneur entre en jeu.

Un jeu de données initial (`init.sql`) est fourni : huit stations, quatre quartiers.

---

## 3. Ta mission, en cinq jalons

Chaque jalon rejoue un TP de la formation, sur ce nouveau sujet. L'ordre n'est pas négociable : chaque jalon s'appuie sur le précédent.

```
   JALON 1 · Git            JALON 2 · Docker         JALON 3 · Kubernetes      JALON 4 · Jenkins        JALON 5 · Preuve
   ┌───────────────┐        ┌───────────────┐        ┌───────────────┐        ┌───────────────┐        ┌───────────────┐
   │ Un depot,     │        │ Une image     │        │ L'application │        │ Un push       │        │ Un rapport,   │
   │ un historique │  ───▶  │ propre, une   │  ───▶  │ tourne dans   │  ───▶  │ suffit a      │  ───▶  │ des captures, │
   │ propre, une   │        │ pile qui monte│        │ un cluster,   │        │ tester,       │        │ un QCM,       │
   │ collaboration │        │ toute seule   │        │ survit, se    │        │ construire,   │        │ une chaine    │
   │ tracee        │        │               │        │ met a jour    │        │ publier,      │        │ qu'on sait    │
   │               │        │               │        │ sans coupure  │        │ deployer      │        │ expliquer     │
   └───────────────┘        └───────────────┘        └───────────────┘        └───────────────┘        └───────────────┘
      TP 1 et TP 2              TP 3 et TP 4              TP 5                     TP 6                   Tous
```

### Jalon 1 · Versionner et collaborer (rappel : TP 1 et TP 2)

Tu pars d'un dossier vide. À la fin du jalon, le projet vit sur GitHub avec un historique qui raconte quelque chose : des commits lisibles, du travail mené sur des branches, au moins une pull request relue, un conflit rencontré et résolu, une version étiquetée, une branche principale protégée, et **aucun secret** dans l'historique.

Tu n'as pas de binôme imposé pour la pull request : tu peux relire et fusionner ta propre pull request, mais tu dois montrer le cycle complet (branche, pull request, commentaire de revue, fusion). Si tu travailles avec un camarade sur vos deux dépôts respectifs, encore mieux : dis le dans ton rapport.

### Jalon 2 · Conteneuriser (rappel : TP 3 et TP 4)

À la fin du jalon, l'application est une **image** que tu sais reconstruire à l'identique, et une **pile** qui démarre d'une seule commande, application et base de données comprises. L'image doit être propre au sens du Jour 2 : construction en plusieurs étages, exécution sans les privilèges du superutilisateur, fichiers inutiles écartés de la construction, dépendances placées de façon à ce que le cache serve vraiment.

La donnée doit survivre à l'arrêt et à la suppression des conteneurs. L'image doit être publiée sur un registre, sous un nom qui t'appartient.

### Jalon 3 · Déployer dans un cluster (rappel : TP 5)

À la fin du jalon, l'application tourne dans ton cluster local, avec sa base, sa configuration, ses sondes, et son mot de passe **hors du dépôt Git**. Elle est joignable depuis ton navigateur.

C'est aussi le jalon où tu fais évoluer l'application : tu ajoutes la route `/alertes`, qui liste les stations dont le nombre de vélos disponibles est inférieur ou égal à deux. Cette évolution devient la **version 2** de l'image, et te sert à démontrer deux choses que tu as vues au Jour 3 : une mise à jour progressive **sans coupure de service**, puis un **retour arrière**.

Tu dois enfin montrer que le cluster répare tout seul : monter le nombre d'exemplaires, en supprimer un pendant que le trafic passe, et constater ce qu'il se passe.

### Jalon 4 · Automatiser (rappel : TP 6)

À la fin du jalon, tu ne construis plus rien à la main. Un `git push` déclenche un pipeline qui **teste**, **construit**, **publie** et **déploie**, dans cet ordre, et qui refuse de publier si les tests échouent.

Tu dois écrire au moins deux tests automatisés, dont un qui couvre la route `/alertes` que tu as ajoutée. Le pipeline est décrit dans un fichier versionné dans ton dépôt, jamais collé dans l'interface de Jenkins.

Et surtout : tu dois faire la démonstration du **rouge utile**. Casser volontairement quelque chose, montrer que le pipeline s'arrête, montrer que rien n'a été publié ni déployé, puis réparer et montrer le vert revenir.

### Jalon 5 · Prouver

Un rendu qui n'est pas prouvé n'existe pas. Tu écris un `RAPPORT.md` à partir du gabarit fourni, tu y ranges tes captures, et tu réponds au QCM.

---

## 4. Les contraintes techniques imposées

Elles ne sont pas décoratives : elles t'obligent à comprendre au lieu de recopier, et elles évitent que le projet entre en collision avec la maquette `meteo-api` des trois derniers jours, qui tourne peut être encore sur ta machine.

| Contrainte | Valeur imposée |
| --- | --- |
| Nom du dépôt et du dossier de travail | `velos-api` |
| Nom de l'image | `velos-api`, publiée sous ton identifiant de registre |
| Port de l'API dans le conteneur | `8000` |
| Port publié par la pile de conteneurs, sur ta machine | **`8001`** |
| Port par lequel tu joins l'application dans le cluster, sur ta machine | **`8081`** |
| Jenkins | reste sur `8090`, celui du TP 6 |
| Mot de passe de la base | ne doit apparaître **dans aucun fichier commité** |

> ⚠️ **Le piège annoncé** : le cluster du TP 5 n'expose que le port 8080 de ta machine. Il faudra donc que tu t'occupes de ce point avant de pouvoir joindre ton application sur 8081. Le [fichier d'indices](./3-indices.md) t'aiguille, sans faire le travail à ta place. Anticipe le, car ce geste a une conséquence directe sur le jalon 4.

---

## 5. Ce qui est évalué, en une phrase

Pas la beauté du code de l'application, qui t'est donné. Pas ta vitesse.

**Ta capacité à reprendre les gestes des six TP sur un sujet que tu n'as jamais vu, à expliquer pourquoi tu les fais, et à en apporter la preuve.**

➡️ Passe maintenant au cahier des charges : **[`2-cahier-des-charges.md`](./2-cahier-des-charges.md)**.
