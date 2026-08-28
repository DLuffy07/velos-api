# 3. Indices · ta boussole, pas ton corrigé

> 🎯 **À quoi sert ce fichier** : t'aider à te débloquer **sans te donner la réponse**. Pour chaque moment délicat du projet, tu trouves une **question**, puis des indices repliés, du plus léger (où regarder) au plus précis (quel geste du cours réutiliser). **Aucune commande n'est écrite ici.** C'est toi qui la tapes.

> 🔑 **Règle du jeu** : déplie **un indice à la fois**, et seulement après avoir vraiment cherché. Un indice ouvert trop tôt, c'est de l'apprentissage en moins. Et surtout : le meilleur indice de tous reste **le TP correspondant**, que tu as le droit de rouvrir.

> 🧰 **À garder ouverts à côté de toi**
>
> - `../Jour-1/part-01-pratique.md` et `../Jour-1/part-02-pratique.md` : Git, local puis distant
> - `../Jour-2/part-01-pratique.md` et `../Jour-2/part-02-pratique.md` : Docker, conteneurs puis image et pile
> - `../Jour-3/part-01-pratique.md` : Kubernetes
> - `../Jour-3/part-02-pratique.md` : Jenkins
> - Les fichiers `*-theorie.md` : quand la question commence par « pourquoi »

---

## 🚦 Avant tout : les trois réflexes des trois jours

Quand quelque chose ne marche pas, tu n'improvises pas, tu déroules :

```
   1. QUEL EST L'ETAT REEL ?        lister, decrire, comparer avec ce que j'ai demande
   2. QUE DIT LA MACHINE ?          lire les journaux, en entier, du haut vers le bas
   3. OU SE COUPE LA CHAINE ?       tester chaque maillon separement, du plus proche au plus loin
```

Quatre-vingt-dix pour cent des blocages de la journée se règlent avec ces trois réflexes, sans aide extérieure.

---

## Jalon 1 · Git

**Q1.1** Comment démarrer proprement, sachant que le code fourni doit se retrouver dans un dépôt neuf ?

<details><summary>💡 Indice 1</summary>

Deux ordres possibles : créer le dépôt distant d'abord, ou le dépôt local d'abord. Les deux marchent, mais l'un des deux t'expose au piège des historiques sans ancêtre commun rencontré au TP 2, étape 8. Choisis en connaissance de cause.

</details>

<details><summary>💡 Indice 2</summary>

Le premier commit ne doit contenir que ce qui mérite d'être versionné. Le fichier d'exclusion arrive donc **très tôt**, pas à la fin.

</details>

**Q1.2** Comment provoquer un conflit qui ait un sens, plutôt qu'un conflit artificiel bricolé en deux minutes ?

<details><summary>💡 Indice 1</summary>

Un conflit apparaît quand **la même ligne** du même fichier a été modifiée de deux façons différentes dans deux branches, et qu'on les rassemble. Le TP 1, partie G, décrit exactement la mise en scène.

</details>

<details><summary>💡 Indice 2</summary>

Choisis une ligne où deux décisions plausibles s'affrontent, par exemple le seuil d'alerte du parc de vélos, ou le texte d'une réponse de l'API. Ton rapport doit pouvoir expliquer **pourquoi** il y avait deux avis.

</details>

**Q1.3** La protection de la branche principale refuse tes envois directs, et tu es bloqué. Est-ce un problème ?

<details><summary>💡 Indice</summary>

Non, c'est exactement l'effet recherché. Relis le TP 2, étape 22 : à partir de là, le chemin normal vers la branche principale passe par une branche et une pull request. Prends l'habitude tout de suite, sinon le jalon 4 te le rappellera violemment.

</details>

**Q1.4** Comment être sûr qu'aucun secret ne traîne dans l'historique ?

<details><summary>💡 Indice 1</summary>

Regarder les fichiers **présents** ne suffit pas. Git conserve le passé : un mot de passe supprimé dans le dernier commit reste lisible dans les commits précédents.

</details>

<details><summary>💡 Indice 2</summary>

Git sait chercher un motif dans l'ensemble de l'historique, pas seulement dans l'état courant. Cherche du côté des commandes de recherche de Git. Si tu trouves quelque chose, la seule vraie réponse est de considérer le secret comme compromis et de le changer.

</details>

---

## Jalon 2 · Docker

**Q2.1** Comment prouver, chiffres à l'appui, que l'ordre des instructions change quelque chose au cache ?

<details><summary>💡 Indice 1</summary>

Il faut **mesurer deux fois** : une construction avec le mauvais ordre, puis une construction avec le bon, en modifiant à chaque fois une ligne de code entre les deux, pour simuler la vraie vie. Le TP 4, partie C, détaille le protocole.

</details>

<details><summary>💡 Indice 2</summary>

Ton système sait chronométrer une commande. Ce sont ces deux durées que le cahier des charges attend dans ton rapport, pas une impression.

</details>

**Q2.2** Comment vérifier que ton image ne tourne pas avec les privilèges du superutilisateur ?

<details><summary>💡 Indice</summary>

Il existe une commande qui répond, en un mot, à la question « qui suis je ». Exécute la **à l'intérieur du conteneur en marche**, pas sur ta machine. TP 4, étape 10.

</details>

**Q2.3** L'API démarre, mais elle répond que ses données viennent du jeu de secours au lieu de la base. Que regarder ?

<details><summary>💡 Indice 1</summary>

L'application choisit sa source en lisant une variable d'environnement. Si elle se rabat sur le secours, c'est que cette variable est absente ou vide **du point de vue du conteneur**, ce qui n'est pas la même chose que du point de vue de ton terminal.

</details>

<details><summary>💡 Indice 2</summary>

Dans une pile de conteneurs, une base ne se joint jamais par `localhost` : `localhost`, pour un conteneur, c'est lui même. Elle se joint par le **nom du service**, résolu par le service de noms interne du réseau créé automatiquement. TP 4, étape 13.

</details>

**Q2.4** La base démarre mais le jeu de données initial n'a jamais été chargé, et l'application se plaint que la table n'existe pas.

<details><summary>💡 Indice</summary>

Le script d'initialisation d'une base PostgreSQL en conteneur n'est joué **qu'une seule fois**, à la toute première initialisation du stockage. Si un volume de la veille traîne, la base se considère déjà initialisée. Le piège numéro deux du TP 4, et sa solution, sont dans la note de fin de TP.

</details>

**Q2.5** Comment démontrer la persistance sans se raconter d'histoires ?

<details><summary>💡 Indice</summary>

Une démonstration honnête, c'est : j'ajoute une donnée reconnaissable, je détruis les conteneurs, je remonte la pile, la donnée est toujours là. Détruire uniquement le conteneur de l'API ne prouve rien. Et attention : certaines façons de tout arrêter suppriment aussi les volumes. Sache laquelle.

</details>

---

## Jalon 3 · Kubernetes

**Q3.1** Le cahier des charges impose de joindre l'application sur le port 8081 de ta machine, alors que ton cluster n'expose que 8080. Comment t'en sortir ?

<details><summary>💡 Indice 1</summary>

Le lien entre un port de ta machine et un port du cluster est décrit dans le **fichier de configuration du cluster**, celui que tu as écrit au TP 5, étape 2. Ce n'est pas une option qu'on ajoute après coup à un cluster déjà né.

</details>

<details><summary>💡 Indice 2</summary>

Un cluster local se supprime et se recrée en quelques minutes. C'est même sa raison d'être : c'est du jetable. Sauvegarde ton fichier de configuration dans le dépôt, ajuste le, recrée.

</details>

<details><summary>⚠️ Conséquence à anticiper</summary>

Recréer le cluster invalide ce que Jenkins savait de lui, et le rattachement réseau entre les deux. Tu devras refaire les deux gestes du TP 6, partie C, **après** la recréation. Fais donc le jalon 3 en entier avant d'attaquer le jalon 4, sinon tu le referas deux fois.

</details>

**Q3.2** Tes pods restent bloqués et n'arrivent pas à récupérer l'image. Pourquoi ?

<details><summary>💡 Indice 1</summary>

Deux causes possibles, et une seule question à te poser : **d'où le cluster tire il cette image ?** Soit d'un registre public, soit d'un stock local que tu as alimenté toi même.

</details>

<details><summary>💡 Indice 2</summary>

Le réflexe martelé au TP 5 tient en trois temps : je construis, **je charge**, je déploie. Si tu préfères passer par ton registre, alors le dépôt d'images doit être public, et l'étiquette doit exister vraiment.

</details>

**Q3.3** Le service ne répond pas, alors que les pods tournent.

<details><summary>💡 Indice 1</summary>

Un service ne connaît pas les pods par leur nom : il les trouve par leurs **étiquettes**. Si le sélecteur du service et les étiquettes des pods ne se correspondent pas au caractère près, le service ne dessert personne.

</details>

<details><summary>💡 Indice 2</summary>

Il existe une ressource qui te dit, en une ligne, si le service a trouvé quelqu'un ou non. Si elle est vide, tu tiens ton diagnostic. C'est l'erreur numéro un en configuration Kubernetes, et le TP 5, partie G, en fait sa première question.

</details>

**Q3.4** Comment démontrer une mise à jour **sans coupure**, et pas seulement une mise à jour ?

<details><summary>💡 Indice 1</summary>

Sans trafic pendant l'opération, tu ne démontres rien. Il te faut une boucle qui interroge l'API en continu, dans un terminal, pendant que la mise à jour se déroule dans un autre.

</details>

<details><summary>💡 Indice 2</summary>

La preuve attendue, c'est une capture où l'on voit, dans la même image, le flot de réponses **sans erreur** et l'avancement du remplacement des exemplaires. Le TP 5, étape 14, met en scène exactement cela.

</details>

**Q3.5** Où mettre le mot de passe de la base, sachant qu'il ne doit apparaître dans aucun fichier commité ?

<details><summary>💡 Indice 1</summary>

Kubernetes a une ressource dédiée. Elle peut se créer **directement en ligne de commande**, sans passer par un fichier, et c'est justement pour cela qu'on l'a créée ainsi au TP 5.

</details>

<details><summary>💡 Indice 2</summary>

Attention au contresens que le cours a pris soin de démonter : cette ressource **n'est pas chiffrée**, elle est simplement encodée. Ton rapport doit le dire, sinon la question reviendra à la soutenance.

</details>

---

## Jalon 4 · Jenkins

**Q4.1** Tes tests passent sur ta machine mais échouent dans le pipeline.

<details><summary>💡 Indice</summary>

Un test qui a besoin d'une base de données, d'un port libre ou d'un fichier posé sur ton bureau n'est pas un test, c'est une dépendance déguisée. Les deux tests du TP 6 tournent **sans rien** : ils interrogent l'application en mémoire, ce qui explique la source qu'ils attendent en réponse.

</details>

**Q4.2** Jenkins n'arrive pas à parler au cluster.

<details><summary>💡 Indice 1</summary>

C'est **le** blocage annoncé du TP 6. Jenkins est un conteneur : ce que ta machine appelle « chez moi » ne désigne pas le cluster vu depuis l'intérieur d'un conteneur.

</details>

<details><summary>💡 Indice 2</summary>

Deux choses sont nécessaires, et il en manque souvent une : le fichier d'accès doit être exporté dans sa variante **interne**, et le conteneur Jenkins doit être **rattaché au même réseau** que le cluster. TP 6, étapes 6 et 7.

</details>

**Q4.3** La publication de l'image est refusée par le registre.

<details><summary>💡 Indice</summary>

Trois causes, dans l'ordre de fréquence observé en salle : le nom d'image contient encore l'identifiant d'exemple au lieu du tien, l'identifiant enregistré dans Jenkins n'est pas un jeton d'accès, ou le dépôt d'images visé ne t'appartient pas. Vérifie le nom **avant** de lancer la première exécution.

</details>

**Q4.4** Le pipeline est vert, mais l'application déployée n'a pas changé.

<details><summary>💡 Indice 1</summary>

C'est le cœur du TP 6. Demander une mise à jour et **attendre qu'elle aboutisse** sont deux choses différentes. Sans l'attente, la machine rend la main immédiatement et déclare une victoire qu'elle n'a pas vérifiée.

</details>

<details><summary>💡 Indice 2</summary>

Il existe une sous-commande qui suit un déploiement jusqu'à son terme et qui échoue si le délai est dépassé. C'est elle qui rend ton pipeline honnête. Le cahier des charges te demande de savoir la citer et d'expliquer ce qu'il se passerait sans elle.

</details>

**Q4.5** Comment mettre en scène un « rouge utile » qui prouve quelque chose ?

<details><summary>💡 Indice 1</summary>

Casse le **code**, pas le pipeline. Une erreur de syntaxe dans la description du pipeline prouve seulement que tu sais faire une faute de frappe. Une valeur de retour fausse dans l'application prouve que les tests servent à quelque chose.

</details>

<details><summary>💡 Indice 2</summary>

La démonstration complète tient en trois preuves : l'étape de test est rouge, les étapes suivantes **n'ont pas été exécutées**, et la version en service dans le cluster est **toujours l'ancienne**. Cette troisième preuve est celle que tout le monde oublie, et c'est la plus importante.

</details>

---

## 🆘 Et si vraiment tu es bloqué

Dans l'ordre, avant de lever la main :

1. Relis le message d'erreur **en entier**. La cause est écrite dedans neuf fois sur dix.
2. Cherche le symptôme dans les encarts de dépannage du TP correspondant : les pièges de ce projet sont **exactement** ceux que la salle a rencontrés pendant trois jours.
3. Isole le maillon. Le problème est il dans l'application, dans l'image, dans le réseau, dans le cluster ou dans le pipeline ? Teste le maillon le plus proche de toi d'abord.
4. Note ce que tu as tenté. Ce sera une de tes trois difficultés dans le rapport, et elle vaut des points.

> 🧠 **Le seul vrai raccourci** : tu as déjà fait tout cela cette semaine. Ce projet ne demande aucun geste nouveau, il demande de retrouver les bons gestes tout seul.
