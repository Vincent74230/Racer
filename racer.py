"""Little programm of an imaginary race between 5 imaginary cars
in an imaginary track made of 20 imaginary trackparts:
it's neverland"""
from random import random, randint

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]
PILOT = ["A", "B", "C", "D", "E"]

class TrackPart:#pylint: disable=R0903
    """This class generate one track-part, 20 of it will be created"""
    def __init__(self):
        self.length = randint(0, 10)
        self.terrain = TERRAINS[randint(0, 3)]
        self.complexity = COMPLEXITIES[randint(0, 2)]
    def __str__(self):
        return "{} {} et {}".format(self.length, self.terrain, self.complexity)

class Track:#pylint: disable=R0903
    """This class generate a track made of 20 trackparts"""
    def __init__(self):
        self.parts = []
        j = 0
        while j < 20:
            (self.parts).append(TrackPart())
            j += 1
    def __getitem__(self, index):
        return self.parts[index]

class Pilot:#pylint: disable=R0903
    """Set up a pilot with a name"""
    compteur = 0
    def __init__(self):
        self.name = PILOT[Pilot.compteur]
        self.normal_speed = random()+0.5
        self.rapid_speed = random()+0.5
        self.subtle_speed = random()+0.5
        Pilot.compteur += 1

class Car:
    """This class makes a car, a pilot inside(with Pilot class), and
    2 classmethods that calculates how much time a combo car/pilot makes in a single
    part, and finally, time the combo made in a all track"""
    def __init__(self):
        """ In this constructor we create our car"""
        self.name = randint(1, 20)
        self.pilot = Pilot()
        self.asphalt_speed = random()+0.5
        self.sand_speed = random()+0.5
        self.mud_speed = random()+0.5
        self.rocky_speed = random()+0.5
    def __str__(self):
        return "voiture {} avec pilot {}".format(self.name, self.pilot.name)
    def time_for_part(self, trackpart):
        """
        Calculates time each combo car/pilot makes within a trackpart
        """
        time_for_part = 0
        vitesse_voiture = 0
        vitesse_pilote = 0
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
    def time_for_track(self, track):
        """
        Calculates time each pilot makes in a track
        """
        time_for_track = 0
        i = 0
        while i < 20:
            time_for_track += self.time_for_part(track[i])
            i += 1
        return time_for_track, self.name, self.pilot.name

TRACK = Track()#track generation
print("Voici le circuit:\n")#print the whole track
K = 0
while K < 20:
    print(TRACK[K])
    K += 1

COMBO_CAR_PILOT = [] # list of 5 combo car/pilot
L = 0
while L < 5:
    PILOT_NAME = PILOT[L]
    PILOT_NAME = Car()
    COMBO_CAR_PILOT.append(PILOT_NAME)
    L += 1
print("\nEt les participants:\n")#print car/pilot combo
M = 0
while M < 5:
    print(COMBO_CAR_PILOT[M])
    M += 1

RESULTATS = []#creates a list with : car/pilot/time for track
N = 0
while N < 5:
    RESULTATS.append(COMBO_CAR_PILOT[N].time_for_track(TRACK))
    N += 1

print("\nVoici les temps sur l'ensemble du circuit:\n")#display time combo car/pilot
O = 0
while O < 5:
    print("{} avec {}".format(RESULTATS[O], COMBO_CAR_PILOT[O]))
    O += 1

LISTE = sorted(RESULTATS)#the winner is
LISTETTE = LISTE[0]
print("\nWinner is :Car {} with pilot {}, time : {}".format(LISTETTE[1], LISTETTE[2], LISTETTE[0]))
