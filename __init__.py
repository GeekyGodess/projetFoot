# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:38:40 2017

@author: 3407073
"""
from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
<<<<<<< HEAD
from StrategiesCreees import RandomStrategy,StrikerStrategy,passeur,attend,passeur_aller_vers, StrikerStrategy_de_base,Attaquant1, Striker1 ,DefenderStrategy_de_base, GoalKeeperStrategy,DefenderStrategy
=======
from StrategiesCreees import RandomStrategy,StrikerStrategy, StrikerStrategy_de_base,Attaquant1, Striker1 ,DefenderStrategy_de_base, GoalKeeperStrategy,DefenderStrategy
>>>>>>> 11ce44acedc4696eb6c0452e9fb2ea242fc6e4ad

#import simple_exemple_commun
#ou from teams import team1, team2
## Creation d'une equipe

serpentar= SoccerTeam(name="team1",login="etu1")
gryfondor= SoccerTeam(name="team2",login="etu2")


def get_team(i):
    if i ==1:
        g= SoccerTeam(name="Gryffondor")
<<<<<<< HEAD
        g.add("Attaquant1",passeur())#+DefenderStrategy()) 

=======
        g.add("Attaquant1",Attaquant1())#+DefenderStrategy()) 
>>>>>>> 11ce44acedc4696eb6c0452e9fb2ea242fc6e4ad
        return g
    if i ==2:
        g= SoccerTeam(name="Gryffondor")
        g.add("Weasley",Attaquant1())
        g.add("celine",StrikerStrategy_de_base())
        #g.add("Granger",GoalKeeperStrategy())
        return g
    if i ==4:
        g= SoccerTeam(name="Gryffondor")
<<<<<<< HEAD
        g.add("Potter",passeur())
        g.add("Weasley",passeur())
        g.add("Granger",passeur())
        g.add("Dumbledore",passeur_aller_vers())
=======
        g.add("Potter",StrikerStrategy())
        g.add("Weasley",GoalKeeperStrategy())
        g.add("Granger",DefenderStrategy_de_base())
        g.add("Dumbledore",Attaquant1())
>>>>>>> 11ce44acedc4696eb6c0452e9fb2ea242fc6e4ad
        return g

def get_team_adv(i):
    if i ==1:
        s= SoccerTeam(name="Serpentard")
        s.add("Malfoy",StrikerStrategy()) 
        return s
    if i ==2:
        s= SoccerTeam(name="Serpentard")
        s.add("Crabe",DefenderStrategy_de_base())
        s.add("Goyle",StrikerStrategy_de_base())
        return s
    if i ==4:
        s= SoccerTeam(name="Serpentard")
        s.add("orochimaru",attend())
        s.add("Crabe",attend())
        s.add("Goyle",attend())
        s.add("Voldemort",attend())
        return s


