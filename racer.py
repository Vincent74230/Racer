from random import random, randint, choice as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]
PILOT = ["A","B","C","D","E"]

class TrackPart:
    def __init__(self):
        self.length = randint (0,10)
        self.terrain = TERRAINS[randint(0,3)]
        self.complexity = COMPLEXITIES[randint(0,2)]
    def __str__(self):
        return "{} {} et {}".format(self.length,self.terrain,self.complexity)

class Track:
    def __init__(self):
        self.parts = []
        i=0
        while i<20:
            (self.parts).append(TrackPart())
            i +=1
    def __getitem__(self,index):
        return self.parts[index]

class Pilot:
    compteur = 0
    def __init__(self):
        self.name = PILOT[Pilot.compteur]
        self.normal_speed = random()+0.5
        self.rapid_speed = random()+0.5
        self.subtle_speed = random()+0.5
        Pilot.compteur += 1

class Car:
    def __init__(self):
        self.name = randint(1,20)
        self.pilot = Pilot()
        self.asphalt_speed = random()+0.5
        self.sand_speed = random()+0.5
        self.mud_speed = random()+0.5
        self.rocky_speed = random()+0.5
    def __str__(self):
        return "voiture {} avec pilot {}".format(self.name,self.pilot.name)
    def time_for_part(self,trackpart):
        time_for_part = 0
        vitesse_voiture=0
        vitesse_pilote=0
        if trackpart.complexity == 'normal':
            vitesse_pilote = self.pilot.normal_speed
        if trackpart.complexity == 'rapid':
            vitesse_pilote = self.pilot.rapid_speed
        if trackpart.complexity == 'subtle':
            vitesse_pilote = self.pilot.subtle_speed
        if trackpart.terrain == 'asphalt':
            vitesse_voiture = self.asphalt_speed
        if trackpart.terrain == 'sand':
            vitesse_voiture = self.sand_speed
        if trackpart.terrain == 'mud':
            vitesse_voiture = self.mud_speed
        if trackpart.terrain == 'rocky':
            vitesse_voiture = self.rocky_speed
        time_for_part = trackpart.length * (1+vitesse_pilote*vitesse_voiture)
        return time_for_part
    def time_for_track(self,track):
        time_for_track = 0
        i=0
        while i<20:
            time_for_track += self.time_for_part(track[i])
            i+=1
        return time_for_track,self.name,self.pilot.name

track = Track()#generation du circuit
print ("Voici le circuit:\n")#affichage du circuit
i=0
while i<20:
    print (track[i])
    i +=1

combo_car_pilot = [] #generation d'une liste de 5 voitures avec pilote
i = 0
while i<5:
    nom_du_pilote = PILOT[i]
    nom_du_pilote = Car()
    combo_car_pilot.append(nom_du_pilote)
    i += 1
print ("\nEt les participants:\n")#affichage combo car/pilote
i=0 
while i<5:
    print (combo_car_pilot[i])
    i +=1

Resultats = []#creation d'une liste comprenant : des listes de trio : temps par tronçon, n°voiture et pilote
i=0
while i<5:
    Resultats.append(combo_car_pilot[i].time_for_track(track))
    i+=1

print ("\nVoici les temps sur l'ensemble du circuit:\n")#affichage des temps par voiture et pilote
i=0
while i<5:
    print ("{} avec {}".format(Resultats[i],combo_car_pilot[i]))
    i += 1

liste = sorted(Resultats)#on désigne le vainqueur
listette = liste[0]
print("\nAnd the winner is :Car {} with pilot {}, time : {}".format(listette[1],listette[2],listette[0]))