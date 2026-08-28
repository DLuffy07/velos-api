# 4. Captures attendues · la preuve, étape par étape

> 📸 **Pourquoi ce fichier** : ton correcteur ne sera pas assis derrière toi. Une exigence non prouvée est une exigence non faite. Ce fichier liste **exactement** les captures attendues, et surtout **ce qui doit être lisible dessus**.

---

## Les règles de la capture

1. **Une capture par ligne du tableau.** Vingt-quatre captures au total. Ni plus, ni beaucoup moins.
2. **Nommage imposé** : `captures/C07-cache-mesure.png`. Le code d'abord, puis un mot ou deux. Un mauvais nommage fait perdre du temps au correcteur, donc des points à toi.
3. **Rangement imposé** : toutes dans le dossier `captures/` de ton dépôt.
4. **Format** : image `.png` ou `.jpg`. Pas de photo d'écran prise au téléphone, pas de document de traitement de texte contenant des images.
5. **Lisibilité** : on doit pouvoir lire le texte sans zoomer. Capture la fenêtre concernée, pas ton bureau entier avec la météo et tes notifications.
6. **Authenticité** : ton nom d'utilisateur, ton identifiant de registre ou ton pseudo GitHub doivent apparaître au moins sur cinq captures. C'est ce qui distingue ton rendu de celui du voisin.
7. **Chaque capture est appelée dans le rapport**, à l'endroit où elle prouve quelque chose. Une capture orpheline ne compte pas.

> 💡 **Astuce** : ne garde pas les captures pour la fin. Elles se prennent **au moment où la chose se produit**. Un déploiement sans coupure ne se rejoue pas facilement une fois qu'il est terminé.

---

## Jalon 1 · Git (5 captures)

| Code | Nom suggéré | Ce qui doit être visible | Ce que ça prouve |
| --- | --- | --- | --- |
| **C01** | `C01-historique.png` | L'historique du dépôt sous forme de graphe, avec au moins six commits, les branches et une fusion | Historique lisible, travail sur branches |
| **C02** | `C02-conflit.png` | Le fichier en conflit avec les marqueurs de conflit visibles, **avant** résolution | Un conflit réellement vécu et non simulé |
| **C03** | `C03-pull-request.png` | La pull request sur GitHub, fermée par une fusion, avec au moins un commentaire de revue visible | Cycle de collaboration complet |
| **C04** | `C04-tag.png` | La page des versions ou des étiquettes de ton dépôt GitHub, où l'on lit `v1.0.0` | Version livrée et identifiée |
| **C05** | `C05-protection.png` | Le refus d'un envoi direct sur la branche principale, message d'erreur compris | La protection est réellement active |

---

## Jalon 2 · Docker (6 captures)

| Code | Nom suggéré | Ce qui doit être visible | Ce que ça prouve |
| --- | --- | --- | --- |
| **C06** | `C06-images-taille.png` | La liste de tes images, où l'on compare la taille de la version naïve et celle de la version finale | Le gain de la construction en plusieurs étages |
| **C07** | `C07-cache-mesure.png` | Les **deux durées** de construction mesurées, avant et après réordonnancement | Le cache exploité, et mesuré |
| **C08** | `C08-non-root.png` | La réponse à la question « qui suis je » exécutée **dans** le conteneur | Exécution sans privilèges |
| **C09** | `C09-pile-demarree.png` | L'état des deux services de la pile, avec l'état de santé de la base | Démarrage ordonné, sonde de bonne santé |
| **C10** | `C10-api-base.png` | La réponse de l'API sur le port `8001`, où l'on lit que la source est la base et où l'on voit les stations | La chaîne application vers base fonctionne |
| **C11** | `C11-persistance.png` | La donnée que tu as ajoutée, toujours présente **après** destruction et remontée de la pile | Les volumes font leur travail |

À cela s'ajoute une preuve qui n'est pas une capture d'écran : ton image publiée doit être visible publiquement sur le registre, et son adresse est citée dans le rapport.

---

## Jalon 3 · Kubernetes (7 captures)

| Code | Nom suggéré | Ce qui doit être visible | Ce que ça prouve |
| --- | --- | --- | --- |
| **C12** | `C12-cluster.png` | Les nœuds du cluster, tous prêts | Le cluster est opérationnel |
| **C13** | `C13-ressources.png` | Les pods, les services et les déploiements en une vue, avec l'exposition de l'API | L'application est déclarée correctement |
| **C14** | `C14-api-cluster.png` | La réponse de l'API sur le port `8081`, avec la source `base` | L'application est servie **par le cluster** |
| **C15** | `C15-echelle.png` | Quatre exemplaires de l'API, avec la colonne indiquant sur **quel nœud** chacun tourne | Passage à l'échelle et répartition |
| **C16** | `C16-panne.png` | Un exemplaire supprimé, son remplaçant en train d'arriver, et le flot de requêtes qui continue | Le cluster répare tout seul |
| **C17** | `C17-mise-a-jour.png` | Le trafic qui passe **sans erreur** pendant le remplacement des exemplaires par la version 2 | Mise à jour sans coupure |
| **C18** | `C18-retour-arriere.png` | L'historique des révisions du déploiement, et la version revenue en arrière | Retour arrière maîtrisé |

---

## Jalon 4 · Jenkins (6 captures)

| Code | Nom suggéré | Ce qui doit être visible | Ce que ça prouve |
| --- | --- | --- | --- |
| **C19** | `C19-identifiants.png` | La liste des identifiants enregistrés dans Jenkins, **sans jamais montrer leur valeur** | Les secrets ne sont pas en clair dans le pipeline |
| **C20** | `C20-pipeline-vert.png` | La vue par étapes du pipeline, les quatre étapes au vert | La chaîne complète fonctionne |
| **C21** | `C21-declenchement.png` | L'exécution déclenchée par un envoi vers GitHub, avec la cause du déclenchement affichée | L'automatisation est réelle |
| **C22** | `C22-pipeline-rouge.png` | L'étape de test en rouge, et les étapes suivantes **non exécutées** | Le rouge bloque bien la suite |
| **C23** | `C23-cause-echec.png` | L'extrait du journal d'exécution où l'on lit la cause exacte de l'échec | Tu sais lire un échec |
| **C24** | `C24-image-deployee.png` | L'image réellement en service dans le cluster, portant l'étiquette produite par le pipeline | C'est bien **la machine** qui a déployé |

> ⚠️ **Sur C19** : si la valeur d'un secret apparaît sur une capture, considère le comme compromis, change le, et refais la capture. C'est vrai en cours comme en entreprise.

---

## Récapitulatif à cocher avant l'envoi

- [ ] Mes 24 captures sont dans `captures/`
- [ ] Elles sont nommées `C01-...` à `C24-...`
- [ ] Chacune est appelée au moins une fois dans `RAPPORT.md`
- [ ] Aucune ne laisse voir un mot de passe, un jeton ou une clé privée
- [ ] Mon identité (pseudo GitHub, identifiant de registre, nom d'utilisateur) apparaît sur au moins cinq d'entre elles
- [ ] Mon dépôt est **public**, et le lien fonctionne depuis une fenêtre de navigation privée
