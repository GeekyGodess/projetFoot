# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:38:40 2017

@author: 3407073
"""
from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from StrategiesCreees import RandomStrategy, StrikerStrategy, DefenderStrategy, GoalKeeperStrategy

#import simple_exemple_commun
#ou from teams import team1, team2
## Creation d'une equipe
serpentar= SoccerTeam(name="team1",login="etu1")
gryfondor= SoccerTeam(name="team2",login="etu2")

#team 1

#team1.add("Helmut",StrikerStrategy())
#team1.add("Joe",GoalKeeperStrategy())
##team1.add("John",DefenderStrategy()) 
#
##team 2
#
#team2.add("Patrick",GoalKeeperStrategy())
#team2.add("John",StrikerStrategy()) #Strategie qui defend pb quand il y a que ce joueur comme attaquant 
#team2.add("Paul",DefenderStrategy())   #Strategie attaque

#team2.add("A",GoalKeeperStrategy())

def get_team(i): 
   # s = SoccerSimulator("") 
    serpentard= SoccerTeam(name="serpentard",login="etu1")
    if i== 1: 
        serpentard.add("Itachi", StrikerStrategy())
        return serpentard
    if i ==4: 
        serpentard.add("Itachi",StrikerStrategy())
        serpentard.add("Orochimaru",GoalKeeperStrategy())
        serpentard.add("Hel",StrikerStrategy())
        serpentard.add("Malfoy",StrikerStrategy())
        return serpentard
    if i == 2: 
        serpentard.add("Goyle",GoalKeeperStrategy())
        serpentard.add("Crabe",StrikerStrategy())
        
        return serpentard

#def get_team2(i): 
#   # s = SoccerSimulator("") 
#    conoha= SoccerTeam(name="conoha",login="etu1")
#    if i== 1: 
#        conoha.add("I", StrikerStrategy())
#        return serpentar
#    if i ==4: 
#        conoha.add("Itachi",StrikerStrategy())
#        conoha.add("Orochimaru",GoalKeeperStrategy())
#        conoha.add("Hel",StrikerStrategy())
#        conoha.add("azaikcez",StrikerStrategy())
#        return conoha
#    if i == 2: 
#        conoha.add("Joe",GoalKeeperStrategy())
#        conoha.add("Pecvze",StrikerStrategy())
#        
#        return conoha
