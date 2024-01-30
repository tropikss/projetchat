
Le code de ce projet s'est déroulé en plusieurs étape.
Premiérement on a travaillé a faire fonctionner tout les capteurs que l'on devait utiliser. On a du réinstaller
certaines librairies etc...

Ensuite est venu le moment de découvrir tout ce que l'on pouvait faire avec la caméra.
L'idée d'upload les photos directement sur le cloud semblait très intéressante mais assez compliqué a mettre
en place. Finalement l'api google est très bien faite et on a réussi assez rapidement a recevoir les autorisations
nécessaire pour pouvoir consulter et rajouter des fichiers sur le google drive.
Dans le fichier "drive.py", il existe plusieurs fonction permettant d'accéder au google drive.
Le plus compliqué dans cette étape a été de trouver comment créer correctement les requetes a l'api google.
Ca demande de beaucoup lire les documentations sur le site de l'api google drive, heuresement tout est très bien
documenté et on comprend vite.

Une fois que l'upload des photos sur google drive fonctionnait, on devais réussir a prendre nos propre photos
avec le raspberry. Pour ca, il existait différent parametres sur lesquels jouer pour prendre des photos qui
correspondrait au mieux a notre projet. Nous avons besoin de pouvoir prendre des photos assez rapidement, dans
une bonne qualité. La camera du raspberry nous permet de prendre des photos de réolution maximale 3280 x 2464.
On a testé avec cette qualité, et la photo prenait environ 3 secondes a se prendre, ce qui est beaucoup trop long.
On a mesuré le temps en mesurant le temps écoulé avant le début de la prise, et une fois la photo crée.
On a donc essayé avec une résolution plus basse. Avec du 720 x 480, la photo met environ 0.8 secondes. 
Mais la qualité est assez mediocre. En réalité la qualité de la photo ne change pas, il n'y a pas de zone "flou".
C'est la taille du champs de vision qui change. La qualité maximale capturera tout le champs de vision possible
par la camera, tandis qu'une qualité moindre n'en prendra qu'une partie. le 1920 x 1080 ne prenait que 1 seconde
a peu près, ca semble assez etonnant la différence de temps entre 480p et 1080p. Du coup on est parti sur du 1080p

Ensuite on devait réussir a savoir quand prendre les photos, on a pensé a utiliser un capteur a ultrason, pour 
savoir quand le chat se trouve devant le distributeur. Malheuresement, le capteur a ultrason semble assez
inadapté. On avait beaucoup de faux positif. On a tenté de faire une moyenne des valeurs du capteurs mais 
sans résultat notables.

On a donc décidé de tenter une nouvelle approche, en oubliant le cpateur a ultrason. La caméra nous permet 
d'analyser des images, on a donc dans un premier temps fais une detection de mouvement via les images.
Le concept est simple, on prend une photo, puis une deuxieme, on compare les deux, et si il y a une trop 
grosse différence, alors il y a eu un mouvement, donc on sauvegarde les photos. Ensuite on supprime la 
première photo, et la deuxième photo devient la première. On effectue la comparaison d'images avec openCV.
On peut se demander quelle photo sauvegarder. On a choisi pour ce système de sauvegarder la deuxième. En effet,
si il y a mouvement, alors la deuxième contiendra le changement. Néanmoins ca pose un problème, si on a le chat
devant, alors les différences entre les photos ne seront pas très grandes, donc il n'y a aura qu'une seule photo
qui sera prise, entre le moment sans chat et avec. Il y en aura auss iune deuxième, entre le moment ou le chat est
la, es tquand il part. On se retrouve donc avec deux photos environ, une du chat, et l'autre de notre piece 
sans le chat. Ce système semble donc pas ultra parfait.

On a donc décidé de s'intéresser a la reconnaissance d'image. OpenCV est une bibliotheque extremement complète,
qui permet de tester une image et de la comparer a un modèle pré-entrainé afin de détecter si un motif revient.
Il existe des modèle pré-entrainé pour détecter un chat. On utilise pour ca l'algorithme haar cascade.
L'algorithme Haar Cascade compare les différences de luminosité entre des moyennes de pixels sur un 
grand échantillon d'images et apprend à détecter des objets en utilisant ces caractéristiques. 
Après mise en place des fonctions nécessaire a son utilisation, on a pu tester grace a des photos de chat,
et ca fonctionnaut assez mal. On a du régler certains parametre, comme le taux de tolérance etc...
Et après modification, ca fonctionnait plutot bien, mieux que l'ancien système.

Restait a fixer un dernier problème, le temps pour upload une photo sur google drive est assez long, du a la 
quantité d'informations a envoyer. Le fait que le temps d'upload soit long, réduisait le nombre de photo 
de notre chat. 
Pour contrer cela, on peut simplement marquer les photos a envoyer sur le google drive (les photos du chat donc)
et les envoyer lorsque le chat est parti. Comment détécter que le chat est parti ? La caméra ne detecte plus le 
chat pendant un certain temps, ou un certain nombre de photos, par exemple 10.

Donc en résumé, notre caméra prend une photo, un algorithme l'analyse, si il détecte un chat, il déplace la photo
dans un fichier spécial, sinon il la supprime. Dés qu'il détecte un chat, il remet un compteur a zero, sinon il
l'incrémente. Si ce compteur atteint un nombre fixé, le chat est parti depuis un moment, on peut donc upload. On
envoie une requete a l'api pour envoyer chaque fichier présente dans le dossier spécial. 

Ensuite restait plus qu'a faire fonctionner l'écran pour afficher tout ca, et la led.

Bibliothèques utilisée :

    picamera2
    libcamera
    openCV
    groveI2Cmotor
    groveI2Clcd
    google.auth
    OAuth2