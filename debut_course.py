"""
On veut faire une course sur un parcours aléatoirement construit et des participants aléatoires. Pour cela on va faire deux classes TrackPart et Track pour modéliser une piste hétérogène et deux classes Pilot et Car pour faire un combo participant de course.

Voici les attributs et méthodes des classes à faire.

Class TrackPart, liste des attributs:
- length: Un entier entre 0 et 10
- terrain: Un des 4 choix suivants "asphalt", "sand", "mud", "rocky"
- complexity: Un des 3 choix suivants "normal", "rapid", "subtle"

Class Track, liste des attributs:
- parts: Liste de TrackParts (par défaut on en génère 20)

Class Pilot, liste des attributs:
- name: Une lettre majuscule
- normal_speed: Un nombre flottant entre 0.5 et 1.5
- rapid_speed: Un nombre flottant entre 0.5 et 1.5
- subtle_speed: Un nombre flottant entre 0.5 et 1.5

Class Car, liste des attributs:
- name: Un numéro entre 1 et 20
- pilot: Un pilote (on peut le générer à la volée)
- asphalt_speed: Un nombre flottant entre 0.5 et 1.5
- sand_speed: Un nombre flottant entre 0.5 et 1.5
- mud_speed: Un nombre flottant entre 0.5 et 1.5
- rocky_speed: Un nombre flottant entre 0.5 et 1.5
Et il faut aussi faire les méthodes d'instance suivantes:
- time_for_part: prends comme argument un TrackPart et donne le temps pour la voiture/pilote sur le tronçon
                 il faut prendre en compte le terrain (et vitesse de voiture sur ce terrain)
                 et aussi la complexité (et la vitesse de pilote pour ce genre de complexité)
                 on multiplie les vitesses (en partant d'une vitesse de 1) avec la longueur du tronçon
- time_for_track: prends comme argument un Track et utilise time_for_part sur les différents tronçons
                  renvoie le temps total sur la piste

Faire un print pour chacun des éléments suivants
1) Générer une piste avec 20 tronçons
2) Générer 5 voitures avec pilotes
3) Calculer les temps pour chaque voiture sur la piste
4) Indiquer le vainqueur

En lançant le script on devrait avoir un affichage du genre qui suit:
Using track: rapid sand (3) + subtle rocky (4) + rapid asphalt (6) + rapid asphalt (9) + subtle rocky (9) + normal rocky (8) + rapid mud (4) + rapid sand (6) + subtle rocky (9) + normal rocky (6) + normal asphalt (3) + subtle asphalt (6) + rapid rocky (4) + rapid asphalt (6) + rapid rocky (4) + normal asphalt (7) + subtle rocky (8) + normal sand (6) + normal rocky (7) + subtle asphalt (8)
With cars: Car 9 with Pilot G, Car 20 with Pilot G, Car 4 with Pilot N, Car 4 with Pilot W, Car 4 with Pilot B
The times are: [[96.73751345520175, Car 9 with Pilot G], [92.91817878332827, Car 20 with Pilot G], [102.3473766304071, Car 4 with Pilot N], [148.79336249531696, Car 4 with Pilot W], [139.66958580936762, Car 4 with Pilot B]]
THE WINNER IS Car 20 with Pilot G

IMPORTANT: essayer de faire un commit git pour l'ajout de chaque Classe (avec sa méthode __init__) et un commit par méthode de classe / méthode d'instance. On devrait donc avoir minimum 6-8 commits, une douzaine de commits est correct mais une vingtaine ferait un peu beaucoup (à moins que ce soit pour rajouter des améliorations hors-sujet).

Voici le début du programme pour se lancer:
"""

from string import ascii_uppercase
from random import random, randint, choice as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

class TrackPart: