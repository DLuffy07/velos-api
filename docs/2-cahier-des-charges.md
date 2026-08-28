# 2. Cahier des charges · les exigences, une par une

> 📋 **Comment lire ce fichier** : c'est ta **liste à cocher** et c'est aussi la **grille de correction**. Chaque ligne doit être **réellement faite** et **prouvée** dans ton `RAPPORT.md`, par une capture d'écran ou par un fichier présent dans le dépôt. Une exigence faite mais non prouvée compte comme non faite.
>
> La colonne « TP source » te dit où retrouver le geste. Tu as le droit de rouvrir ces fichiers.

---

## Jalon 1 · Git : versionner et collaborer · **4 points**

| ✅ | Exigence | Ce qui est attendu | TP source |
| -- | --- | --- | --- |
| ☐ | **Dépôt local initialisé** | Un dépôt `velos-api` sur ta machine, avec le code fourni comme point de départ | Jour 1 matin, TP 1 partie C |
| ☐ | **Identité correcte** | Tes commits portent ton vrai nom et une adresse cohérente, pas `root` ni un nom générique | Jour 1 matin, TP 1 partie B |
| ☐ | **Historique lisible** | Au moins **six** commits, avec des messages qui décrivent un changement et pas « update » ou « fix » | Jour 1 matin, TP 1 partie D |
| ☐ | **Fichier d'exclusion** | Un `.gitignore` adapté à un projet Python, qui écarte au minimum l'environnement virtuel, les fichiers compilés et tout fichier de secrets | Jour 1 matin, TP 1 partie E |
| ☐ | **Travail sur branche** | Le travail est mené sur des branches nommées, pas directement sur la branche principale | Jour 1 matin, TP 1 partie F |
| ☐ | **Conflit résolu** | Un conflit réellement provoqué puis résolu, dont on voit la trace dans l'historique | Jour 1 matin, TP 1 partie G |
| ☐ | **Dépôt distant en SSH** | Le dépôt est sur GitHub, et le lien vers le distant utilise SSH, pas HTTPS | Jour 1 après-midi, TP 2 parties B et C |
| ☐ | **Pull request complète** | Une branche poussée, une pull request ouverte, **au moins un commentaire de revue**, puis la fusion | Jour 1 après-midi, TP 2 partie D |
| ☐ | **Version étiquetée** | Un tag `v1.0.0` posé sur la version conteneurisée, visible sur GitHub | Jour 1 après-midi, TP 2 partie F |
| ☐ | **Branche principale protégée** | Une règle de protection active sur la branche principale, et la preuve qu'un envoi direct est refusé | Jour 1 après-midi, TP 2 partie F |
| ☐ | **Aucun secret dans l'historique** | Pas de mot de passe, pas de jeton, pas de clé privée, ni dans les fichiers présents ni dans les commits passés | Jour 1, tout le TP 2 |

---

## Jalon 2 · Docker : conteneuriser · **5 points**

| ✅ | Exigence | Ce qui est attendu | TP source |
| -- | --- | --- | --- |
| ☐ | **Recette de construction** | Un `Dockerfile` versionné qui construit l'application à partir d'une image de base officielle et légère | Jour 2 après-midi, TP 4 partie B |
| ☐ | **Cache de construction exploité** | Les dépendances sont installées **avant** la copie du code, et tu sais **chiffrer** ce que cela fait gagner. Le rapport donne les deux durées mesurées | Jour 2 après-midi, TP 4 partie C |
| ☐ | **Fichier d'exclusion de construction** | Un `.dockerignore` présent, et tu sais dire ce qu'il évite d'envoyer | Jour 2 après-midi, TP 4 partie C |
| ☐ | **Construction en plusieurs étages** | L'image finale ne contient pas l'outillage de construction. Le rapport compare la taille de la version naïve et de la version finale | Jour 2 après-midi, TP 4 partie D |
| ☐ | **Exécution sans privilèges** | Le processus dans le conteneur ne tourne pas en superutilisateur, et tu le prouves | Jour 2 après-midi, TP 4 partie D |
| ☐ | **Pile complète en un fichier** | Un fichier de composition monte l'API **et** sa base de données, sur un réseau interne, l'API joignant la base par son **nom de service** | Jour 2 après-midi, TP 4 partie E |
| ☐ | **Démarrage ordonné** | L'API ne démarre pas avant que la base soit réellement prête. Une sonde de bonne santé le garantit | Jour 2 après-midi, TP 4 partie E |
| ☐ | **Base non publiée** | Le port de la base de données n'est **pas** exposé sur ta machine | Jour 2 après-midi, TP 4 partie E |
| ☐ | **Données persistantes** | Une donnée ajoutée survit à l'arrêt **et** à la suppression des conteneurs. Tu le démontres | Jour 2 matin, TP 3 partie E |
| ☐ | **API servie par la base** | Sur le port imposé `8001`, la réponse indique que les données viennent de la base et non du jeu de secours | Jour 2 après-midi, TP 4 partie E |
| ☐ | **Image publiée** | L'image est publiée sur un registre sous ton identifiant, étiquetée `1.0`, et tu vérifies qu'on peut la récupérer | Jour 2 après-midi, TP 4 partie F |

---

## Jalon 3 · Kubernetes : déployer · **5 points**

| ✅ | Exigence | Ce qui est attendu | TP source |
| -- | --- | --- | --- |
| ☐ | **Cluster opérationnel** | Un cluster local à plusieurs nœuds, tous prêts, et **le port 8081 de ta machine ouvert vers le cluster** | Jour 3 matin, TP 5 parties A et B |
| ☐ | **Manifestes versionnés** | Tous les fichiers de description du déploiement sont dans le dépôt, dans un dossier dédié | Jour 3 matin, TP 5 partie D |
| ☐ | **Base de données déployée** | La base tourne dans le cluster, avec son jeu de données initial injecté depuis une ressource de configuration | Jour 3 matin, TP 5 partie D |
| ☐ | **Secret hors du dépôt** | Le mot de passe vit dans une ressource dédiée du cluster, créée sans passer par un fichier commité. Tu sais dire pourquoi cette ressource n'est **pas** un coffre-fort | Jour 3 matin, TP 5 partie D |
| ☐ | **Déploiement de l'API** | L'API est déclarée avec un nombre d'exemplaires supérieur à un, et l'image est bien celle que **tu** as publiée | Jour 3 matin, TP 5 partie D |
| ☐ | **Exposition réseau** | Deux expositions distinctes : la base joignable **uniquement** depuis l'intérieur du cluster, l'API joignable depuis ta machine sur `8081` | Jour 3 matin, TP 5 partie D |
| ☐ | **Sonde de disponibilité** | L'API n'est mise en service que lorsqu'elle répond réellement. La route prévue pour cela est utilisée | Jour 3 matin, TP 5 partie D |
| ☐ | **Passage à l'échelle** | Le nombre d'exemplaires est monté à **quatre**, et tu montres qu'ils ne sont pas tous sur le même nœud | Jour 3 matin, TP 5 partie E |
| ☐ | **Résistance à la panne** | Un exemplaire est supprimé **pendant que le trafic passe**, et le service ne s'interrompt pas. Tu expliques pourquoi il revient | Jour 3 matin, TP 5 partie E |
| ☐ | **Évolution en version 2** | La route `/alertes` est ajoutée par tes soins, testée, et publiée sous l'étiquette `2.0` | Énoncé §3, jalon 3 |
| ☐ | **Mise à jour sans coupure** | Le passage de la version 1 à la version 2 se fait pendant que le trafic passe, sans erreur côté client | Jour 3 matin, TP 5 partie F |
| ☐ | **Retour arrière** | Un retour arrière ramène la version précédente, et tu montres l'historique des révisions | Jour 3 matin, TP 5 partie F |

---

## Jalon 4 · Jenkins : automatiser · **4 points**

| ✅ | Exigence | Ce qui est attendu | TP source |
| -- | --- | --- | --- |
| ☐ | **Tests automatisés** | Au moins **deux** tests, dont un qui couvre la route `/alertes`. Ils tournent sans base de données | Jour 3 après-midi, TP 6 partie D |
| ☐ | **Tests intégrés à la construction** | Les tests s'exécutent dans un étage dédié de la construction de l'image, et non sur ta machine | Jour 3 après-midi, TP 6 partie D |
| ☐ | **Pipeline versionné** | La description du pipeline est un fichier **du dépôt**, pas un texte collé dans l'interface | Jour 3 après-midi, TP 6 partie F |
| ☐ | **Quatre étapes enchaînées** | Tester, puis construire, puis publier, puis déployer. Dans cet ordre | Jour 3 après-midi, TP 6 partie F |
| ☐ | **Identifiants protégés** | Les accès au registre et au cluster passent par le gestionnaire d'identifiants de Jenkins, jamais en clair dans le fichier de pipeline | Jour 3 après-midi, TP 6 parties C et F |
| ☐ | **Étiquetage traçable** | Chaque exécution produit une image portant une étiquette **unique**, qui permet de relier l'image à l'exécution qui l'a produite | Jour 3 après-midi, TP 6 partie F |
| ☐ | **Déclenchement automatique** | Un envoi vers GitHub déclenche l'exécution sans que tu cliques | Jour 3 après-midi, TP 6 partie F |
| ☐ | **Déploiement honnête** | Le pipeline attend la fin réelle du déploiement avant de se déclarer vert. Tu sais dire quelle ligne fait cela et ce qu'il se passerait sans elle | Jour 3 après-midi, TP 6 partie F |
| ☐ | **Le rouge utile** | Une erreur volontaire fait échouer l'étape de test, la publication et le déploiement **n'ont pas lieu**, et la version en service reste intacte. Puis tu répares et le vert revient | Jour 3 après-midi, TP 6 partie G |
| ☐ | **Lecture d'un échec** | Ton rapport cite l'extrait de journal qui donne la cause de l'échec, pas seulement la capture de l'étape rouge | Jour 3 après-midi, TP 6 partie G |

---

## Jalon 5 · Rapport, preuves et compréhension · **2 points**

| ✅ | Exigence | Ce qui est attendu |
| -- | --- | --- |
| ☐ | **Rapport complet** | `RAPPORT.md` à la racine du dépôt, construit à partir du gabarit fourni, sans section vide |
| ☐ | **Captures conformes** | Toutes les captures demandées dans [`4-captures-attendues.md`](./4-captures-attendues.md), nommées selon la convention, lisibles, non rognées sur l'essentiel |
| ☐ | **Le trajet d'une requête** | Ton rapport décrit, en quelques lignes ou par un schéma, le trajet complet d'une requête depuis ton navigateur jusqu'à la base, dans le cluster |
| ☐ | **Trois difficultés** | Trois problèmes réellement rencontrés, avec le symptôme, la cause trouvée et la correction |
| ☐ | **Usage de l'assistance** | La section prévue est remplie honnêtement : outils utilisés, pour quoi faire |

---

## Le barème

| Jalon | Points |
| --- | --- |
| Jalon 1 · Git | 4 |
| Jalon 2 · Docker | 5 |
| Jalon 3 · Kubernetes | 5 |
| Jalon 4 · Jenkins | 4 |
| Jalon 5 · Rapport et preuves | 2 |
| **Total projet** | **20** |

Le **QCM** est noté séparément, sur 40 points ramenés à 20.

### Ce qui fait perdre des points, même si « ça marche »

- Un secret présent dans le dépôt, y compris dans un commit ancien : **retrait direct de 2 points**, parce que c'est la faute qui coûte le plus cher en entreprise.
- Un geste fait à la main et non reproductible, alors qu'il aurait dû devenir un fichier versionné.
- Des captures illisibles, non nommées, ou qui ne montrent pas ce qu'elles sont censées prouver.
- Un rendu que tu ne sais pas expliquer lors de la soutenance éclair.

### Ce qui rapporte des points bonus (jusqu'à 2 points, dans la limite de 20)

- Une sonde de vivacité en plus de la sonde de disponibilité, avec l'explication de la différence.
- Des limites de ressources déclarées sur les conteneurs du cluster.
- Une étape supplémentaire pertinente dans le pipeline, par exemple une analyse de qualité ou une vérification de vulnérabilités de l'image.
- Une étiquette d'image qui référence le commit plutôt que le seul numéro d'exécution.

➡️ Si tu bloques : **[`3-indices.md`](./3-indices.md)**. Si tu avances : garde **[`4-captures-attendues.md`](./4-captures-attendues.md)** ouvert.
